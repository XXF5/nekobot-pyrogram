import requests, zipfile, os, re, html
from bs4 import BeautifulSoup
from flask import send_file, after_this_request

DOWNLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', '..', 'downloads')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

DL_BASE = "https://es.3hentai.net/d"

def sanitize(name):
    return re.sub(r'[\\/*?:"<>|]', '', name)

def extract_title(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    title_tag = soup.find('title')
    if title_tag:
        return sanitize(html.unescape(title_tag.text.strip()))
    return "SinTitulo"

def fetch_images_3hentai(code):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    
    base_url = f"{DL_BASE}/{code}"
    
    try:
        res = requests.get(base_url, headers=headers)
        if res.status_code == 404:
            return None, []

        title = extract_title(res.text)
        images = []
        index = 1

        while True:
            page_url = f"{base_url}/{index}/"
            res = requests.get(page_url, headers=headers)
            if res.status_code == 404:
                break
            soup = BeautifulSoup(res.content, "html.parser")
            found = re.findall(r'https?://[^"\']+\.(?:jpg|jpeg|png|webp)', str(soup))
            images.extend(found)
            index += 1

        return title, images
    except Exception as e:
        print(f"Error al acceder {base_url}: {e}")
        return None, []

def create_3hentai_cbz(code):
    title, images = fetch_images_3hentai(code)
    if not images:
        raise Exception(f"No se encontraron imágenes para el código {code}")
    
    filename = f"{code} - {title}.cbz"
    path = os.path.join(DOWNLOAD_FOLDER, filename)
    
    with zipfile.ZipFile(path, "w") as zipf:
        for i, url in enumerate(images):
            try:
                img = requests.get(url).content
                ext = url.split('.')[-1].split('?')[0]
                fname = f"{i+1}.{ext}"
                temp_path = os.path.join(DOWNLOAD_FOLDER, fname)
                with open(temp_path, "wb") as f: 
                    f.write(img)
                zipf.write(temp_path, fname)
                os.remove(temp_path)
            except Exception as e:
                print(f"Error procesando imagen {url}: {e}")
                continue
    
    return path, filename

def serve_and_clean(filepath):
    filename = os.path.basename(filepath)

    @after_this_request
    def cleanup(resp):
        try:
            os.remove(filepath)
        except:
            pass
        return resp

    return send_file(
        filepath,
        as_attachment=True,
        download_name=filename,
        mimetype="application/vnd.comicbook+zip"
    )
