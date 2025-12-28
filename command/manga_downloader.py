import os
import subprocess
import uuid
import json
from datetime import datetime
import re

class MangaDexDownloader:
    def __init__(self, base_path="vault_files/Mangas"):
        self.base_path = base_path
        if not os.path.exists(base_path):
            os.makedirs(base_path, exist_ok=True)
        
        self.downloads = {}
        self.downloads_file = os.path.join(base_path, "downloads.json")
        self.load_downloads()
    
    def load_downloads(self):
        if os.path.exists(self.downloads_file):
            try:
                with open(self.downloads_file, 'r', encoding='utf-8') as f:
                    self.downloads = json.load(f)
            except:
                self.downloads = {}
    
    def save_downloads(self):
        with open(self.downloads_file, 'w', encoding='utf-8') as f:
            json.dump(self.downloads, f, indent=2)
    
    def get_download_progress(self, download_id):
        return self.downloads.get(download_id, {})
    
    def build_command(self, url, download_range, format_type, start_value=None, end_value=None):
        cmd = ["mangadex-dl"]
        
        cmd.extend(["--path", self.base_path])
        
        format_map = {
            "cbz": ["--save-as", "cbz"],
            "cbz-volume": ["--save-as", "cbz-volume"],
            "cbz-single": ["--save-as", "cbz-single"],
            "pdf": ["--save-as", "pdf"],
            "pdf-volume": ["--save-as", "pdf-volume"],
            "pdf-single": ["--save-as", "pdf-single"],
            "raw": ["--save-as", "raw"],
            "raw-volume": ["--save-as", "raw-volume"],
            "raw-single": ["--save-as", "raw-single"],
            "cb7": ["--save-as", "cb7"],
            "cb7-volume": ["--save-as", "cb7-volume"],
            "cb7-single": ["--save-as", "cb7-single"],
            "epub": ["--save-as", "epub"],
            "epub-volume": ["--save-as", "epub-volume"],
            "epub-single": ["--save-as", "epub-single"],
        }
        
        if format_type in format_map:
            cmd.extend(format_map[format_type])
        
        if download_range == "all":
            pass
        elif download_range == "from-chapter" and start_value:
            cmd.extend(["--start-chapter", start_value])
        elif download_range == "from-volume" and start_value:
            cmd.extend(["--start-volume", start_value])
        elif download_range == "chapters-range" and start_value and end_value:
            cmd.extend(["--start-chapter", start_value, "--end-chapter", end_value])
        elif download_range == "chapter-to-volume" and start_value and end_value:
            cmd.extend(["--start-chapter", start_value, "--end-volume", end_value])
        elif download_range == "volumes-range" and start_value and end_value:
            cmd.extend(["--start-volume", start_value, "--end-volume", end_value])
        elif download_range == "volume-to-chapter" and start_value and end_value:
            cmd.extend(["--start-volume", start_value, "--end-chapter", end_value])
        elif download_range == "specific-chapter" and start_value:
            cmd.extend(["--start-chapter", start_value, "--end-chapter", start_value])
        elif download_range == "specific-volume" and start_value:
            cmd.extend(["--start-volume", start_value, "--end-volume", start_value])
        
        cmd.append(url)
        
        return cmd
    
    def start_download(self, url, download_range="all", format_type="cbz-volume", 
                      start_value=None, end_value=None):
        download_id = str(uuid.uuid4())
        
        self.downloads[download_id] = {
            "id": download_id,
            "url": url,
            "range": download_range,
            "format": format_type,
            "start": start_value,
            "end": end_value,
            "state": "processing",
            "progress": 0,
            "message": "Iniciando descarga...",
            "start_time": datetime.now().isoformat(),
            "output": "",
            "error": ""
        }
        self.save_downloads()
        
        cmd = self.build_command(url, download_range, format_type, start_value, end_value)
        
        def run_download():
            try:
                self.downloads[download_id]["message"] = "Ejecutando comando..."
                self.downloads[download_id]["command"] = " ".join(cmd)
                self.save_downloads()
                
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding='utf-8',
                    errors='replace'
                )
                
                stdout_lines = []
                stderr_lines = []
                
                while True:
                    output = process.stdout.readline()
                    if output:
                        stdout_lines.append(output)
                        self.downloads[download_id]["output"] += output
                        
                        if "Downloading chapter" in output or "Progreso" in output:
                            self.downloads[download_id]["message"] = output.strip()
                        
                        if "100%" in output:
                            match = re.search(r'(\d+)%', output)
                            if match:
                                self.downloads[download_id]["progress"] = int(match.group(1))
                        
                        self.save_downloads()
                    
                    err = process.stderr.readline()
                    if err:
                        stderr_lines.append(err)
                        self.downloads[download_id]["error"] += err
                        self.save_downloads()
                    
                    if output == '' and err == '' and process.poll() is not None:
                        break
                
                return_code = process.wait()
                
                if return_code == 0:
                    self.downloads[download_id]["state"] = "completed"
                    self.downloads[download_id]["message"] = "✅ Descarga completada"
                    self.downloads[download_id]["progress"] = 100
                else:
                    self.downloads[download_id]["state"] = "error"
                    self.downloads[download_id]["message"] = f"❌ Error en descarga (código: {return_code})"
                
                self.downloads[download_id]["end_time"] = datetime.now().isoformat()
                self.downloads[download_id]["stdout"] = "".join(stdout_lines)
                self.downloads[download_id]["stderr"] = "".join(stderr_lines)
                self.save_downloads()
                
            except Exception as e:
                self.downloads[download_id]["state"] = "error"
                self.downloads[download_id]["message"] = f"❌ Excepción: {str(e)}"
                self.downloads[download_id]["end_time"] = datetime.now().isoformat()
                self.downloads[download_id]["error"] = str(e)
                self.save_downloads()
        
        import threading
        thread = threading.Thread(target=run_download)
        thread.daemon = True
        thread.start()
        
        return download_id
    
    def cleanup_old_downloads(self, hours=24):
        current_time = datetime.now()
        to_delete = []
        
        for download_id, download_info in self.downloads.items():
            if "end_time" in download_info:
                end_time = datetime.fromisoformat(download_info["end_time"])
                if (current_time - end_time).total_seconds() > hours * 3600:
                    to_delete.append(download_id)
        
        for download_id in to_delete:
            del self.downloads[download_id]
        
        self.save_downloads()
    
    def get_all_downloads(self):
        self.cleanup_old_downloads()
        return self.downloads
