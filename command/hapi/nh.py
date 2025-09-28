import random
import time
import os
import re
import zipfile
import html
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

DOWNLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', '..', 'downloads')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def sanitize(name):
    return re.sub(r'[\\/*?:"<>|]', '', name)

def scrape_nhentai(gallery_number):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36')
    chrome_options.add_argument('--accept-language=en-US,en;q=0.9')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    
    chrome_binary_path = "selenium/chrome-linux64/chrome"
    chromedriver_path = "selenium/chromedriver-linux64/chromedriver"
    chrome_options.binary_location = chrome_binary_path

    try:
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        url = f"https://nhentai.net/g/{gallery_number}/"
        print(f"🌐 Accediendo a: {url}")
        
        driver.get(url)
        
        max_attempts = 3
        for attempt in range(max_attempts):
            time.sleep(3 + attempt * 2)
            
            page_source = driver.page_source
            if "Just a moment" in page_source or "Verifying you are human" in page_source:
                print(f"⚠️  Cloudflare detectado (intento {attempt + 1}/{max_attempts}), esperando más...")
                time.sleep(5)
                continue
            
            if "gallery" in page_source.lower() or "cover" in page_source.lower():
                break
        
        html_content = driver.page_source
        
        if not html_content or len(html_content) < 100:
            raise Exception("El contenido HTML parece estar vacío o es muy corto")
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        title_element = soup.find('h1', class_='title')
        if title_element:
            title_parts = []
            for span in title_element.find_all('span', class_=True):
                title_parts.append(span.get_text(strip=True))
            full_title = ' '.join(title_parts)
        else:
            full_title = f"nhentai_{gallery_number}"
        
        gallery_id = None
        image_links = []
        pattern = re.compile(r'//t[1249]\.nhentai\.net/galleries/(\d+)/(\d+)t\.(webp|jpg|png)')
        
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src', '')
            if src:
                match = pattern.search(src)
                if match:
                    gallery_id = match.group(1)
                    break
        
        if gallery_id:
            print(f"🔍 ID real de la galería encontrado: {gallery_id}")
            for img in soup.find_all('img'):
                src = img.get('src') or img.get('data-src', '')
                if src:
                    match = pattern.search(src)
                    if match:
                        page_num = match.group(2)
                        ext = match.group(3)
                        new_link = f"https://i2.nhentai.net/galleries/{gallery_id}/{page_num}.{ext}"
                        image_links.append(new_link)
        else:
            print("❌ No se pudo encontrar el ID real de la galería")
            return None, []
        
        unique_links = []
        for link in image_links:
            if link not in unique_links:
                unique_links.append(link)
        
        unique_links.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
        
        return sanitize(html.unescape(full_title)), unique_links
        
    except Exception as e:
        print(f"❌ Error durante el scraping: {str(e)}")
        return None, []
        
    finally:
        try:
            driver.quit()
            print("🚪 Driver cerrado correctamente")
        except:
            pass

def create_nhentai_cbz(code):
    title, images = scrape_nhentai(code)
    if not images:
        raise Exception(f"No se encontraron imágenes para el código nhentai {code}")
    
    filename = f"{code} - {title}.cbz"
    path = os.path.join(DOWNLOAD_FOLDER, filename)
    
    with zipfile.ZipFile(path, "w") as zipf:
        for i, url in enumerate(images):
            try:
                print(f"📥 Descargando imagen {i+1}/{len(images)}...")
                img_data = requests.get(url, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                    "Referer": "https://nhentai.net/"
                }).content
                
                ext = url.split('.')[-1].split('?')[0]
                fname = f"{i+1:03d}.{ext}"
                temp_path = os.path.join(DOWNLOAD_FOLDER, fname)
                
                with open(temp_path, "wb") as f: 
                    f.write(img_data)
                zipf.write(temp_path, fname)
                os.remove(temp_path)
                
            except Exception as e:
                print(f"❌ Error procesando imagen {url}: {e}")
                continue
    
    print(f"✅ CBZ creado exitosamente: {filename}")
    return path, filename
