import argparse
import time
import os
import math
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

CHROME_BINARY_PATH = "selenium/chrome-linux64/chrome"
CHROMEDRIVER_PATH = "selenium/chromedriver-linux64/chromedriver"
COOKIES_FILE = "nhentai_cookies.json"

def save_cookies(driver):
    try:
        cookies = driver.get_cookies()
        with open(COOKIES_FILE, 'w') as f:
            json.dump(cookies, f)
        print("🍪 Cookies guardadas correctamente")
    except Exception as e:
        print(f"⚠️ No se pudieron guardar las cookies: {e}")

def load_cookies(driver):
    try:
        if os.path.exists(COOKIES_FILE):
            with open(COOKIES_FILE, 'r') as f:
                cookies = json.load(f)
            
            driver.get("https://nhentai.net/")
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except:
                    continue
            print("🍪 Cookies cargadas correctamente")
            return True
    except Exception as e:
        print(f"⚠️ No se pudieron cargar las cookies: {e}")
    return False

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    chrome_options.add_argument('--accept-language=en-US,en;q=0.9')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-plugins')
    chrome_options.binary_location = CHROME_BINARY_PATH

    try:
        service = Service(executable_path=CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
    except Exception as e:
        print(f"Error al configurar el driver: {e}")
        return None

def bypass_cloudflare(driver, url):
    max_attempts = 3
    for attempt in range(max_attempts):
        driver.get(url)
        time.sleep(5 + attempt * 2)
        
        page_source = driver.page_source
        if "Just a moment" in page_source or "Verifying" in page_source:
            print(f"⚠️  Cloudflare detectado (intento {attempt + 1}/{max_attempts}), esperando...")
            time.sleep(8)
            continue
        
        if "gallery" in page_source.lower() or "search" in page_source.lower():
            save_cookies(driver)
            return True
    
    return False

def scrape_nhentai_with_selenium(search_term, page=1):
    driver = setup_driver()
    if not driver:
        return {"results": [], "total_pages": 1}
    
    try:
        cookies_loaded = load_cookies(driver)
        
        url = f"https://nhentai.net/search/?q={search_term.replace(' ', '+')}&page={page}"
        print(f"🌐 Accediendo a: {url}")
        
        if not cookies_loaded or not bypass_cloudflare(driver, url):
            print("❌ No se pudo superar Cloudflare")
            return {"results": [], "total_pages": 1}
        
        time.sleep(3)
        
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "gallery"))
            )
        except:
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            except:
                return {"results": [], "total_pages": 1}
        
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        total_results = 0
        total_pages = 1
        
        h1_element = soup.find('h1')
        if h1_element:
            h1_text = h1_element.get_text(strip=True)
            if "results" in h1_text:
                try:
                    total_results = int(h1_text.split()[0])
                    total_pages = max(1, math.ceil(total_results / 25))
                except:
                    pass
        
        pagination = soup.find('section', class_='pagination')
        if pagination:
            page_links = pagination.find_all('a', class_='page')
            if page_links:
                try:
                    last_page = int(page_links[-1].get_text())
                    total_pages = max(total_pages, last_page)
                except:
                    pass
        
        gallery_divs = soup.find_all('div', class_='gallery')
        
        results = []
        
        for gallery in gallery_divs:
            try:
                link_tag = gallery.find('a', class_='cover')
                if not link_tag:
                    continue
                
                href = link_tag.get('href', '')
                gallery_code = href.split('/')[-2] if href.startswith('/g/') else 'N/A'
                
                img_tag = gallery.find('img')
                image_links = []
                
                if img_tag:
                    src = img_tag.get('src', '')
                    data_src = img_tag.get('data-src', '')
                    
                    possible_sources = [src, data_src]
                    
                    for img_source in possible_sources:
                        if img_source and not img_source.startswith('data:image/gif'):
                            if img_source.startswith('//'):
                                img_source = 'https:' + img_source
                            elif img_source.startswith('/'):
                                img_source = 'https://nhentai.net' + img_source
                            
                            if img_source.startswith('https://') and not img_source.startswith('https://t.nhentai.net/galleries/'):
                                image_links.append(img_source)
                    
                    if not image_links and src and src.startswith('https://t.nhentai.net/galleries/'):
                        image_links.append(src)
                
                caption_div = gallery.find('div', class_='caption')
                name = caption_div.text.strip() if caption_div else 'N/A'
                
                result = {
                    'image_links': image_links,
                    'name': name,
                    'code': gallery_code,
                    'tags': gallery.get('data-tags', '').split()
                }
                
                results.append(result)
                
            except Exception as e:
                continue
        
        return {
            "results": results,
            "total_pages": total_pages,
            "total_results": total_results,
            "current_page": page
        }
        
    except Exception as e:
        return {"results": [], "total_pages": 1}
    
    finally:
        try:
            driver.quit()
        except:
            pass

def main():
    parser = argparse.ArgumentParser(description='Web scraping de nhentai usando Selenium')
    parser.add_argument('-s', '--search', required=True, help='Termino de busqueda')
    parser.add_argument('-p', '--page', type=int, default=1, help='Numero de pagina')
    
    args = parser.parse_args()
    
    data = scrape_nhentai_with_selenium(args.search, args.page)
    results = data["results"]
    total_pages = data["total_pages"]
    
    if results:
        print(f"Resultados obtenidos: {len(results)}")
        print(f"Total de paginas: {total_pages}")
        
        for i, result in enumerate(results, 1):
            print(f"Resultado {i}:")
            print(f"   Codigo: {result['code']}")
            print(f"   Nombre: {result['name']}")
            print(f"   Imagenes: {result['image_links']}")
    else:
        print("No se obtuvieron resultados")

if __name__ == "__main__":
    main()
