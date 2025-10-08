LOGIN_TEMPLATE = """
<!doctype html>
<html><head><title>Login</title><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body { 
        font-family: Arial; 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2em; 
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .login-container {
        background: white;
        padding: 2em;
        border-radius: 15px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        width: 100%;
        max-width: 400px;
    }
    h2 {
        text-align: center;
        color: #333;
        margin-bottom: 1.5em;
        font-size: 1.8em;
    }
    input {
        width: 100%;
        padding: 12px;
        margin-bottom: 1em;
        border: 2px solid #ddd;
        border-radius: 8px;
        font-size: 1em;
        transition: border-color 0.3s;
        box-sizing: border-box;
    }
    input:focus {
        border-color: #667eea;
        outline: none;
    }
    input[type="submit"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        cursor: pointer;
        font-weight: bold;
        padding: 12px;
        transition: transform 0.2s;
    }
    input[type="submit"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    .error-message {
        background: #ffebee;
        color: #c62828;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 1em;
        text-align: center;
        border: 1px solid #ffcdd2;
        display: none;
    }
</style></head>
<body>
    <div class="login-container">
        <h2>🔐 Iniciar sesión</h2>
        
        <div class="error-message" id="errorMessage">
            ❌ Credenciales incorrectas
        </div>
        
        <form method="post">
            <input name="username" placeholder="Usuario" required>
            <input type="password" name="password" placeholder="Contraseña" required>
            <input type="submit" value="Ingresar">
        </form>
    </div>

    <script>
        // Mostrar mensaje de error si hay parámetro de error en la URL
        if (window.location.search.includes('error=1')) {
            document.getElementById('errorMessage').style.display = 'block';
        }
    </script>
</body></html>
"""


UTILS_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Utilidades</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { 
            font-family: Arial; 
            margin: 0; 
            padding: 0; 
            box-sizing: border-box; 
            background-color: #f8f9fa;
        }
        .header { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            padding: 1em; 
            text-align: center; 
            position: relative;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header-title { 
            font-size: 1.2em; 
            margin-bottom: 10px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }
        .nav-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 10px;
        }
        .nav-btn {
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            color: white;
            text-decoration: none;
            font-size: 0.9em;
            transition: background 0.3s;
            border: 1px solid rgba(255,255,255,0.3);
        }
        .nav-btn:hover {
            background: rgba(255,255,255,0.3);
        }
        .content { 
            padding: 2em; 
            max-width: 800px;
            margin: 0 auto;
        }
        .section {
            background: white;
            padding: 1.5em;
            border-radius: 10px;
            margin-bottom: 2em;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h2 {
            color: #333;
            margin-top: 0;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5em;
        }
        form { 
            margin-bottom: 1em; 
            display: flex; 
            flex-direction: column; 
            gap: 0.8em; 
        }
        input[type="text"], select { 
            padding: 0.8em; 
            font-size: 1em; 
            border: 2px solid #ddd;
            border-radius: 6px;
            transition: border-color 0.3s;
        }
        input[type="text"]:focus, select:focus {
            border-color: #667eea;
            outline: none;
        }
        button { 
            padding: 0.8em; 
            font-size: 1em; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            border: none; 
            border-radius: 6px; 
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
        }
        .info-text {
            background: #e3f2fd;
            padding: 10px;
            border-radius: 6px;
            border-left: 4px solid #2196f3;
            margin-top: 10px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-title">
            Utilidades - Servidor Flask de Neko Bot
        </div>
        <div class="nav-buttons">
            <a href="/" class="nav-btn">🏠 Inicio</a>
            <a href="/utils" class="nav-btn">🛠️ Utilidades</a>
            <a href="/downloads" class="nav-btn">📥 Descargas</a>
        </div>
    </div>
    
    <div class="content">
        <div class="section">
            <h2>🔗 Descargar desde Magnet Link</h2>
            <form action="/magnet" method="post">
                <input type="text" name="magnet" placeholder="Magnet link o URL .torrent" required>
                <button type="submit">Iniciar descarga</button>
            </form>
        </div>

        <div class="section">
            <h2>🔞 Descargar Doujin(s)</h2>
            <form action="/crear_cbz" method="post">
                <input type="text" name="codigo" placeholder="Código(s) separados por coma (ej: 123,456,789)" required>
                <select name="tipo" required>
                    <option value="nh">NHentai</option>
                    <option value="h3">3Hentai</option>
                    <option value="hito">Hitomi.la</option>
                </select>
                <button type="submit">Crear CBZ(s)</button>
            </form>
            <div class="info-text">
                💡 Puedes ingresar múltiples códigos separados por comas (ej: 123456,789012,345678).
                La descarga se procesará en segundo plano y podrás ver el progreso en la página de descargas.
            </div>
        </div>
    </div>
</body>
</html>
"""

DOWNLOADS_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Descargas Activas</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container { 
            max-width: 1200px; 
            margin: 0 auto; 
            background: white; 
            padding: 20px; 
            border-radius: 15px; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1em;
            text-align: center;
            border-radius: 10px 10px 0 0;
            margin: -20px -20px 20px -20px;
        }
        h1 { 
            color: white; 
            text-align: center; 
            margin: 0;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }
        .nav { 
            margin-bottom: 20px; 
            text-align: center;
            padding: 10px;
        }
        .nav a { 
            margin: 0 10px; 
            text-decoration: none; 
            color: #667eea;
            font-weight: bold;
            padding: 8px 16px;
            border-radius: 20px;
            background: rgba(102, 126, 234, 0.1);
            transition: background 0.3s;
        }
        .nav a:hover {
            background: rgba(102, 126, 234, 0.2);
        }
        .download-card { 
            border: 1px solid #e0e0e0; 
            padding: 20px; 
            margin: 15px 0; 
            border-radius: 10px; 
            background: #fafafa;
            transition: transform 0.2s;
        }
        .download-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .progress-bar { 
            background: #e0e0e0; 
            height: 20px; 
            border-radius: 10px; 
            overflow: hidden; 
            margin: 15px 0; 
        }
        .progress-fill { 
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            height: 100%; 
            transition: width 0.3s; 
        }
        .stats { 
            display: flex; 
            justify-content: space-between; 
            flex-wrap: wrap; 
            gap: 10px;
        }
        .stat-item { 
            margin: 5px 0;
            padding: 8px;
            background: white;
            border-radius: 6px;
            border-left: 3px solid #667eea;
            flex: 1;
            min-width: 150px;
            text-align: center;
        }
        .completed { 
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
            border-color: #28a745;
        }
        .error { 
            background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
            border-color: #dc3545;
        }
        .processing { 
            background: linear-gradient(135deg, #cce7ff 0%, #b3d9ff 100%);
            border-color: #007bff;
        }
        .controls {
            display: flex;
            gap: 10px;
            margin: 15px 0;
            flex-wrap: wrap;
        }
        .refresh-btn { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            border: none; 
            padding: 10px 20px; 
            border-radius: 6px; 
            cursor: pointer;
            transition: transform 0.2s;
        }
        .refresh-btn:hover {
            transform: translateY(-2px);
        }
        .new-download-form {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border: 2px dashed #667eea;
        }
        .new-download-form input {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 1em;
            box-sizing: border-box;
        }
        .new-download-form button {
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        }
        .auto-refresh { 
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px;
            background: #e9ecef;
            border-radius: 6px;
        }
        .doujin-progress {
            font-size: 1.1em;
            font-weight: bold;
            margin: 10px 0;
            color: #495057;
        }
        .current-item {
            font-style: italic;
            color: #6c757d;
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📥 Descargas Activas</h1>
        </div>
        
        <div class="nav">
            <a href="/">🏠 Inicio</a>
            <a href="/utils">🛠️ Utilidades</a>
            <a href="/downloads">📥 Descargas</a>
        </div>

        <div class="new-download-form">
            <h3>➕ Nueva descarga Torrent/Magnet</h3>
            <form action="/magnet" method="post">
                <input type="text" name="magnet" placeholder="Magnet link o URL .torrent" required>
                <button type="submit" class="refresh-btn">Iniciar descarga</button>
            </form>
        </div>

        <div class="controls">
            <button class="refresh-btn" onclick="location.reload()">🔄 Actualizar</button>
            <div class="auto-refresh">
                <input type="checkbox" id="autoRefresh" onchange="toggleAutoRefresh()">
                <label for="autoRefresh">Actualizar página automáticamente</label>
            </div>
        </div>
        
        <!-- Sección de descargas de Doujins -->
        {% if doujin_downloads %}
            <h2>📚 Descargas de Doujins</h2>
            {% for id, download in doujin_downloads.items() %}
                <div class="download-card {% if download.state == 'completed' %}completed{% elif download.state == 'error' %}error{% else %}processing{% endif %}">
                    <h3>📖 Creando CBZ{{ 's' if download.total > 1 else '' }} ({{ download.tipo|upper }})</h3>
                    
                    <div class="doujin-progress">
                        Progreso: {{ download.progress }} de {{ download.total }} CBZ{{ 's' if download.total > 1 else '' }}
                    </div>
                    
                    {% if download.state == 'processing' %}
                    <div class="current-item">
                        📋 {{ download.current_item }}
                    </div>
                    {% endif %}
                    
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {{ (download.progress / download.total * 100) | round(1) }}%"></div>
                    </div>
                    
                    <p><strong>Estado:</strong> 
                        <span style="color: 
                            {% if download.state == 'completed' %}#28a745
                            {% elif download.state == 'error' %}#dc3545
                            {% else %}#007bff{% endif %};">
                            {{ download.state }}
                        </span>
                    </p>
                    
                    <div class="stats">
                        <div class="stat-item"><strong>✅ Completados:</strong> {{ download.completados }}</div>
                        <div class="stat-item"><strong>❌ Errores:</strong> {{ download.errores }}</div>
                        <div class="stat-item"><strong>📊 Total:</strong> {{ download.total }}</div>
                        <div class="stat-item"><strong>⏰ Iniciado:</strong> {{ download.start_time[:19] }}</div>
                        {% if download.end_time %}
                        <div class="stat-item"><strong>🏁 Finalizado:</strong> {{ download.end_time[:19] }}</div>
                        {% endif %}
                    </div>
                    
                    {% if download.state == 'completed' and download.resultados %}
                    <div style="margin-top: 15px;">
                        <strong>📋 Resultados:</strong>
                        <div style="max-height: 200px; overflow-y: auto; margin-top: 10px;">
                            {% for resultado in download.resultados %}
                            <div style="padding: 5px; border-bottom: 1px solid #eee;">
                                {{ resultado.codigo }}: 
                                <span style="color: {% if resultado.estado == 'completado' %}#28a745{% else %}#dc3545{% endif %};">
                                    {{ resultado.estado }}
                                </span>
                                {% if resultado.error %}
                                - {{ resultado.error }}
                                {% endif %}
                            </div>
                            {% endfor %}
                        </div>
                    </div>
                    {% endif %}
                    
                    {% if download.error %}
                    <p style="color: #dc3545; background: #f8d7da; padding: 10px; border-radius: 5px;">
                        <strong>❌ Error:</strong> {{ download.error }}
                    </p>
                    {% endif %}
                </div>
            {% endfor %}
        {% endif %}
        
        <!-- Sección de descargas de Torrents -->
        {% if downloads %}
            <h2>📦 Descargas Torrent</h2>
            {% for id, download in downloads.items() %}
                <div class="download-card {% if download.state == 'completed' %}completed{% elif download.state == 'error' %}error{% endif %}">
                    <h3>{{ download.filename }}</h3>
                    <p><strong>Estado:</strong> 
                        <span style="color: 
                            {% if download.state == 'completed' %}#28a745
                            {% elif download.state == 'error' %}#dc3545
                            {% else %}#007bff{% endif %};">
                            {{ download.state }}
                        </span>
                    </p>
                    <p><strong>Enlace:</strong> <a href="{{ download.link }}" target="_blank">{{ download.link[:50] }}...</a></p>
                    
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {{ download.percent }}%"></div>
                    </div>
                    <p><strong>Progreso:</strong> {{ download.percent }}%</p>
                    
                    <div class="stats">
                        <div class="stat-item"><strong>📦 Descargado:</strong> {{ (download.downloaded / (1024*1024)) | round(2) }} MB</div>
                        <div class="stat-item"><strong>📊 Total:</strong> {{ (download.total_size / (1024*1024)) | round(2) if download.total_size > 0 else 'Calculando...' }} MB</div>
                        <div class="stat-item"><strong>🚀 Velocidad:</strong> {{ (download.speed / (1024*1024)) | round(2) }} MB/s</div>
                        <div class="stat-item"><strong>⏰ Iniciado:</strong> {{ download.start_time[:19] }}</div>
                        {% if download.end_time %}
                        <div class="stat-item"><strong>✅ Completado:</strong> {{ download.end_time[:19] }}</div>
                        {% endif %}
                    </div>
                    
                    {% if download.error %}
                    <p style="color: #dc3545; background: #f8d7da; padding: 10px; border-radius: 5px;">
                        <strong>❌ Error:</strong> {{ download.error }}
                    </p>
                    {% endif %}
                </div>
            {% endfor %}
        {% endif %}

        {% if not downloads and not doujin_downloads %}
            <div style="text-align: center; padding: 40px; color: #6c757d;">
                <h3>📭 No hay descargas activas</h3>
                <p>Inicia una nueva descarga usando el formulario superior</p>
            </div>
        {% endif %}

        <!-- Formulario para nueva descarga al final -->
        <div class="new-download-form">
            <h3>➕ Nueva descarga Torrent/Magnet</h3>
            <form action="/magnet" method="post">
                <input type="text" name="magnet" placeholder="Magnet link o URL .torrent" required>
                <button type="submit" class="refresh-btn">Iniciar descarga</button>
            </form>
        </div>
    </div>

    <script>
        let autoRefreshInterval;

        function toggleAutoRefresh() {
            if (document.getElementById('autoRefresh').checked) {
                autoRefreshInterval = setInterval(() => {
                    location.reload();
                }, 5000); // 5 segundos
            } else {
                clearInterval(autoRefreshInterval);
            }
        }

        // No auto-activación al cargar la página
        document.addEventListener('DOMContentLoaded', function() {
            // El checkbox está desactivado por defecto
        });
    </script>
</body>
</html>
"""

MAIN_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Explorador de Archivos</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial; margin: 0; padding: 0; box-sizing: border-box; background-color: #f8f9fa; }
        .header { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            padding: 1em; 
            text-align: center; 
            position: relative;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header-title { 
            font-size: 1.2em; 
            margin-bottom: 10px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }
        .header a { 
            color: white; 
            text-decoration: none;
            font-weight: bold;
            transition: opacity 0.3s;
        }
        .header a:hover { opacity: 0.8; }
        .nav-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 10px;
        }
        .nav-btn {
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            color: white;
            text-decoration: none;
            font-size: 0.9em;
            transition: background 0.3s;
            border: 1px solid rgba(255,255,255,0.3);
        }
        .nav-btn:hover {
            background: rgba(255,255,255,0.3);
        }
        .content { 
            padding: 2em; 
            max-width: 1200px;
            margin: 0 auto;
        }
        .section {
            background: white;
            padding: 1.5em;
            border-radius: 10px;
            margin-bottom: 2em;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h2 {
            color: #333;
            margin-top: 0;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5em;
        }
        form { margin-bottom: 1em; display: flex; flex-direction: column; gap: 0.5em; }
        input[type="file"], input[type="text"], select { 
            padding: 0.8em; 
            font-size: 1em; 
            border: 2px solid #ddd;
            border-radius: 6px;
            transition: border-color 0.3s;
        }
        input[type="file"]:focus, input[type="text"]:focus, select:focus {
            border-color: #667eea;
            outline: none;
        }
        button { 
            padding: 0.8em; 
            font-size: 1em; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            border: none; 
            border-radius: 6px; 
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
        }
        ul { list-style-type: none; padding: 0; }
        li { 
            margin: 0.5em 0; 
            word-break: break-word;
            padding: 0.8em;
            background: #f8f9fa;
            border-radius: 6px;
            border-left: 4px solid #667eea;
            display: flex;
            align-items: center;
            flex-wrap: wrap;
        }
        .file-info {
            flex: 1;
            min-width: 200px;
        }
        .file-actions {
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
        }
        a { text-decoration: none; color: #667eea; font-weight: 500; }
        a:hover { text-decoration: underline; }
        .delete-btn, .rename-btn, .extract-btn, .gallery-btn { 
            color: white; 
            border: none; 
            padding: 0.5em 1em; 
            border-radius: 4px; 
            cursor: pointer;
            font-size: 0.9em;
            text-decoration: none;
            display: inline-block;
        }
        .delete-btn { background-color: #dc3545; }
        .rename-btn { background-color: #ffc107; color: black; }
        .extract-btn { background-color: #28a745; }
        .gallery-btn { background-color: #17a2b8; }
        .compress-toggle { 
            margin-top: 1em;
            background: #28a745;
        }
        .select-all {
            margin-bottom: 10px;
            background: #6c757d;
        }
        
        .file-list {
            max-height: 400px;
            overflow-y: auto;
            border: 1px solid #ddd;
            border-radius: 6px;
            padding: 1em;
        }
    </style>
    <script>
        function toggleCompress() {
            const section = document.getElementById("compress-section");
            section.style.display = section.style.display === "none" ? "block" : "none";
        }
        
        function toggleRename(id) {
            const input = document.getElementById("rename-" + id);
            const btn = document.getElementById("rename-" + id + "-btn");
            input.style.display = input.style.display === "none" ? "inline" : "none";
            btn.style.display = btn.style.display === "none" ? "inline" : "none";
        }
        
        function selectAllFiles(selectAll) {
            const checkboxes = document.querySelectorAll('input[name="selected"]');
            checkboxes.forEach(checkbox => {
                checkbox.checked = selectAll;
            });
        }
        
        // Función para enviar formularios de forma segura
        function submitForm(form, event) {
            event.preventDefault();
            if (confirm('¿Estás seguro de que quieres realizar esta acción?')) {
                form.submit();
            }
        }
    </script>
</head>
<body>
    <div class="header">
        <div class="header-title">
            Servidor Flask de Neko Bot creado por <a href="https://t.me/nakigeplayer" target="_blank">Naki</a>
        </div>
        <div class="nav-buttons">
            <a href="/" class="nav-btn">🏠 Inicio</a>
            <a href="/utils" class="nav-btn">🛠️ Utilidades</a>
            <a href="/downloads" class="nav-btn">📥 Descargas</a>
            {% if has_images %}
            <a href="/gallery?path={{ current_path }}" class="nav-btn">🖼️ Galería</a>
            {% endif %}
        </div>
    </div>
    
    <div class="content">
        <div class="section">
            <h2>📤 Subir archivo</h2>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <button type="submit">Subir archivo</button>
            </form>
        </div>

        <div class="section">
            <h2>🗜️ Comprimir archivos</h2>
            <button class="compress-toggle" onclick="toggleCompress()">Mostrar opciones de compresión</button>
            <div id="compress-section" style="display:none; margin-top: 1em;">
                <button type="button" class="select-all" onclick="selectAllFiles(true)">Seleccionar todo</button>
                <button type="button" class="select-all" onclick="selectAllFiles(false)">Deseleccionar todo</button>
                <form action="/compress" method="post">
                    <input type="text" name="archive_name" placeholder="Nombre del archivo .7z" required>
                    <div class="file-list">
                        {% for item in items %}
                            <div>
                                <input type="checkbox" name="selected" value="{{ item['full_path'] }}" id="file-{{ loop.index }}">
                                <label for="file-{{ loop.index }}">
                                    {% if item['is_dir'] %}
                                        📂 {{ item['name'] }}/
                                    {% else %}
                                        📄 {{ item['name'] }} — {{ item['size_mb'] }} MB
                                    {% endif %}
                                </label>
                            </div>
                        {% endfor %}
                    </div>
                    <button type="submit">Comprimir seleccionados</button>
                </form>
            </div>
        </div>

        <div class="section">
            <h2>📁 Archivos guardados</h2>
            <ul>
            {% for item in items %}
                <li>
                    <div class="file-info">
                        {% if item['is_dir'] %}
                            📂 <a href="/browse?path={{ item['rel_path'] }}">{{ item['name'] }}/</a>
                        {% else %}
                            📄 <a href="/download?path={{ item['rel_path'] }}">{{ item['name'] }}</a> — {{ item['size_mb'] }} MB
                        {% endif %}
                    </div>
                    <div class="file-actions">
                        <form action="/delete" method="post" style="display:inline;">
                            <input type="hidden" name="path" value="{{ item['full_path'] }}">
                            <button type="submit" class="delete-btn" onclick="return confirm('¿Eliminar {{ item['name'] }}?')">Eliminar</button>
                        </form>
                        <button class="rename-btn" onclick="toggleRename('{{ loop.index }}')">✏️ Renombrar</button>
                        {% if item['name'].lower().endswith('.7z') or item['name'].lower().endswith('.cbz') or item['name'].lower().endswith('.zip') %}
                        <form action="/extract" method="post" style="display:inline;">
                            <input type="hidden" name="path" value="{{ item['full_path'] }}">
                            <button type="submit" class="extract-btn" onclick="return confirm('¿Descomprimir {{ item['name'] }}?')">📦 Descomprimir</button>
                        </form>
                        {% endif %}
                        {% if item['name'].lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')) %}
                        <a href="/{{ item['rel_path'] }}" class="gallery-btn" target="_blank">🖼️ Ver</a>
                        {% endif %}
                        <form action="/rename" method="post" style="display:inline;">
                            <input type="hidden" name="old_path" value="{{ item['full_path'] }}">
                            <input type="text" name="new_name" id="rename-{{ loop.index }}" style="display:none; width: 200px;" placeholder="Nuevo nombre">
                            <button type="submit" style="display:none;" id="rename-{{ loop.index }}-btn">✅</button>
                        </form>
                    </div>
                </li>
            {% endfor %}
            </ul>
        </div>
    </div>
</body>
</html>
"""
   
GALLERY_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Galería de Imágenes</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { 
            font-family: Arial; 
            margin: 0; 
            padding: 0; 
            background-color: #f0f0f0;
        }
        .header { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            padding: 1em; 
            text-align: center; 
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header a { 
            color: white; 
            text-decoration: none;
            font-weight: bold;
            margin: 0 10px;
            padding: 5px 10px;
            border-radius: 4px;
            background: rgba(255,255,255,0.2);
        }
        .header a:hover { 
            background: rgba(255,255,255,0.3);
        }
        .gallery-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 15px;
            padding: 20px;
        }
        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s;
            background: white;
        }
        .gallery-item:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .gallery-item img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            display: block;
        }
        .gallery-item .caption {
            padding: 10px;
            text-align: center;
            font-size: 0.9em;
            color: #333;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .back-button {
            display: inline-block;
            margin: 10px 20px;
            padding: 8px 15px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 4px;
        }
        .fullscreen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.9);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            cursor: pointer;
        }
        .fullscreen img {
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
        }
        .nav-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="header">
        <a href="/">🏠 Inicio</a>
        <a href="/utils">🛠️ Utilidades</a>
        <a href="/downloads">📥 Descargas</a>
        <a href="/browse?path={{ current_path }}">📂 Volver al explorador</a>
    </div>

    <div class="nav-buttons">
        <a href="?path={{ current_path }}&view=grid" class="nav-btn">🖼️ Vista Cuadrícula</a>
        <a href="?path={{ current_path }}&view=slideshow" class="nav-btn">🎬 Vista Presentación</a>
    </div>

    <div class="gallery-container">
        {% for image in image_files %}
        <div class="gallery-item" onclick="openFullscreen('{{ image.url_path }}')">
            <img src="{{ image.url_path }}" alt="{{ image.name }}" loading="lazy">
            <div class="caption">{{ image.name }}</div>
        </div>
        {% endfor %}
    </div>

    <div id="fullscreen-view" class="fullscreen" style="display:none;" onclick="closeFullscreen()">
        <img id="fullscreen-img" src="">
    </div>

    <script>
        function openFullscreen(src) {
            document.getElementById('fullscreen-img').src = src;
            document.getElementById('fullscreen-view').style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }
        
        function closeFullscreen() {
            document.getElementById('fullscreen-view').style.display = 'none';
            document.body.style.overflow = 'auto';
        }
        
        // Cerrar con ESC
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') closeFullscreen();
        });
    </script>
</body>
</html>
"""

SEARCH_NH_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Búsqueda nHentai</title>
    <style>
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 15px;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .gallery-item {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .gallery-item img {
            max-width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 4px;
        }
        .gallery-name {
            margin-top: 10px;
            font-weight: bold;
            font-size: 12px;
            word-break: break-word;
            height: 40px;
            overflow: hidden;
        }
        .gallery-code {
            color: #666;
            font-size: 11px;
            margin: 5px 0;
        }
        .search-form {
            padding: 20px;
            background: #f5f5f5;
            margin-bottom: 20px;
            text-align: center;
        }
        .search-form input {
            padding: 8px;
            margin: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .search-form button {
            padding: 8px 16px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .pagination {
            text-align: center;
            padding: 20px;
        }
        .pagination a {
            margin: 0 10px;
            padding: 8px 16px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 4px;
        }
        .pagination span {
            margin: 0 15px;
            font-weight: bold;
        }
        .convert-btn {
            background: #ffc107;
            color: black;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            margin: 2px;
            font-size: 11px;
        }
        .loading {
            opacity: 0.5;
        }
        .convert-all-btn {
            background: #17a2b8;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            margin: 10px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="search-form">
        <form method="GET" action="/api/snh/">
            <input type="text" name="q" value="{{ search_term }}" placeholder="Término de búsqueda" required>
            <input type="number" name="p" value="{{ current_page }}" min="1" placeholder="Página">
            <button type="submit">Buscar</button>
        </form>
        <button class="convert-all-btn" onclick="convertAllImages()">Convertir Todas las Imágenes a Base64</button>
    </div>

    {% if results %}
    <div class="gallery-grid">
        {% for result in results %}
        <div class="gallery-item" id="gallery-{{ result.code }}">
            {% if result.image_links %}
            <img src="{{ result.image_links[0] }}" alt="{{ result.name }}" 
                 id="img-{{ result.code }}"
                 data-original-src="{{ result.image_links[0] }}"
                 onerror="this.src='https://via.placeholder.com/200x300?text=Imagen+no+disponible'">
            {% else %}
            <img src="https://via.placeholder.com/200x300?text=Sin+imagen" alt="Sin imagen" id="img-{{ result.code }}" data-original-src="">
            {% endif %}
            <div class="gallery-code">Código: {{ result.code }}</div>
            <div class="gallery-name">{{ result.name }}</div>
            <div style="margin-top: 10px;">
                <a href="/api/dnh/{{ result.code }}">Descargar CBZ</a>
                <button class="convert-btn" onclick="convertToBase64('{{ result.code }}')">
                    Convertir a Base64
                </button>
            </div>
        </div>
        {% endfor %}
    </div>
    
    <div class="pagination">
        {% if current_page > 1 %}
        <a href="/api/snh/{{ search_term }}?p={{ current_page - 1 }}">Página Anterior</a>
        {% endif %}
        <span>Página {{ current_page }} de {{ total_pages }}</span>
        {% if current_page < total_pages %}
        <a href="/api/snh/{{ search_term }}?p={{ current_page + 1 }}">Página Siguiente</a>
        {% endif %}
    </div>
    {% else %}
    <div style="text-align: center; padding: 40px;">
        <h3>No se encontraron resultados para "{{ search_term }}"</h3>
    </div>
    {% endif %}

    <script>
        async function convertToBase64(code) {
            const imgElement = document.getElementById(`img-${code}`);
            const galleryElement = document.getElementById(`gallery-${code}`);
            const btnElement = event.target;
            const originalSrc = imgElement.dataset.originalSrc;
            
            if (!originalSrc || originalSrc.includes('base64') || originalSrc.includes('via.placeholder.com')) {
                return;
            }
            
            btnElement.disabled = true;
            btnElement.textContent = 'Convirtiendo...';
            galleryElement.classList.add('loading');
            
            try {
                const response = await fetch('/api/proxy-image?url=' + encodeURIComponent(originalSrc));
                const blob = await response.blob();
                
                const reader = new FileReader();
                reader.onload = function() {
                    const base64 = reader.result;
                    imgElement.src = base64;
                    btnElement.textContent = '¡Convertida!';
                    galleryElement.classList.remove('loading');
                    
                    setTimeout(() => {
                        btnElement.disabled = false;
                        btnElement.textContent = 'Convertir a Base64';
                    }, 2000);
                };
                reader.readAsDataURL(blob);
                
            } catch (error) {
                console.error('Error convirtiendo imagen:', error);
                btnElement.textContent = 'Error';
                galleryElement.classList.remove('loading');
                
                setTimeout(() => {
                    btnElement.disabled = false;
                    btnElement.textContent = 'Convertir a Base64';
                }, 2000);
            }
        }

        async function convertAllImages() {
            const convertButtons = document.querySelectorAll('.convert-btn');
            const convertAllBtn = document.querySelector('.convert-all-btn');
            
            convertAllBtn.disabled = true;
            convertAllBtn.textContent = 'Convirtiendo todas...';
            
            for (let i = 0; i < convertButtons.length; i++) {
                const btn = convertButtons[i];
                const galleryElement = btn.closest('.gallery-item');
                const code = galleryElement.id.replace('gallery-', '');
                const imgElement = document.getElementById(`img-${code}`);
                const originalSrc = imgElement.dataset.originalSrc;
                
                if (originalSrc && !originalSrc.includes('base64') && !originalSrc.includes('via.placeholder.com')) {
                    btn.click();
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
            
            convertAllBtn.disabled = false;
            convertAllBtn.textContent = 'Convertir Todas las Imágenes a Base64';
        }

        document.addEventListener('DOMContentLoaded', function() {
            const images = document.querySelectorAll('img[data-original-src]');
            images.forEach(img => {
                img.addEventListener('error', function() {
                    if (this.src && !this.src.includes('via.placeholder.com')) {
                        this.src = 'https://via.placeholder.com/200x300?text=Error+cargando+imagen';
                    }
                });
            });
        });
    </script>
</body>
</html>
'''

SEARCH_3H_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Búsqueda 3Hentai</title>
    <style>
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 15px;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .gallery-item {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .gallery-item img {
            max-width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 4px;
        }
        .gallery-name {
            margin-top: 10px;
            font-weight: bold;
            font-size: 12px;
            word-break: break-word;
            height: 60px;
            overflow: hidden;
        }
        .gallery-code {
            color: #666;
            font-size: 11px;
            margin: 5px 0;
        }
        .search-form {
            padding: 20px;
            background: #f5f5f5;
            margin-bottom: 20px;
            text-align: center;
        }
        .search-form input {
            padding: 8px;
            margin: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .search-form button {
            padding: 8px 16px;
            background: #e846c9;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .pagination {
            text-align: center;
            padding: 20px;
        }
        .pagination a {
            margin: 0 10px;
            padding: 8px 16px;
            background: #e846c9;
            color: white;
            text-decoration: none;
            border-radius: 4px;
        }
        .pagination span {
            margin: 0 15px;
            font-weight: bold;
        }
        .convert-btn {
            background: #ffc107;
            color: black;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            margin: 2px;
            font-size: 11px;
        }
        .loading {
            opacity: 0.5;
        }
        .convert-all-btn {
            background: #17a2b8;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            margin: 10px;
            font-size: 14px;
        }
        .total-results {
            text-align: center;
            color: #666;
            margin-bottom: 10px;
        }
        .download-link {
            background: #28a745;
            color: white;
            padding: 5px 10px;
            border-radius: 4px;
            text-decoration: none;
            font-size: 11px;
            display: inline-block;
            margin: 2px;
        }
        .download-link:hover {
            background: #218838;
        }
    </style>
</head>
<body>
    <div class="search-form">
        <form method="GET" action="/api/s3h/">
            <input type="text" name="q" value="{{ search_term }}" placeholder="Término de búsqueda" required>
            <input type="number" name="p" value="{{ current_page }}" min="1" placeholder="Página">
            <button type="submit">Buscar en 3Hentai</button>
        </form>
        <button class="convert-all-btn" onclick="convertAllImages()">Convertir Todas las Imágenes a Base64</button>
    </div>

    {% if results %}
    <div class="total-results">
        <strong>{{ total_results }}</strong> resultados totales - Página {{ current_page }} de {{ total_pages }}
    </div>
    <div class="gallery-grid">
        {% for result in results %}
        <div class="gallery-item" id="gallery-{{ result.code }}">
            {% if result.image_links and result.image_links[0] %}
            <img src="{{ result.image_links[0] }}" alt="{{ result.name }}" 
                 id="img-{{ result.code }}"
                 data-original-src="{{ result.image_links[0] }}"
                 onerror="this.src='https://via.placeholder.com/200x300?text=Imagen+no+disponible'">
            {% else %}
            <img src="https://via.placeholder.com/200x300?text=Sin+imagen" alt="Sin imagen" id="img-{{ result.code }}" data-original-src="">
            {% endif %}
            <div class="gallery-code">ID: {{ result.code }}</div>
            <div class="gallery-name">{{ result.name }}</div>
            <div style="margin-top: 10px;">
                <a href="/api/v3h/{{ result.code }}" class="download-link" target="_blank">
                    Ver Detalles
                </a>
                <button class="convert-btn" onclick="convertToBase64('{{ result.code }}')">
                    Convertir a Base64
                </button>
            </div>
        </div>
        {% endfor %}
    </div>
    
    <div class="pagination">
        {% if current_page > 1 %}
        <a href="/api/s3h/{{ search_term }}?p={{ current_page - 1 }}">Página Anterior</a>
        {% endif %}
        <span>Página {{ current_page }} de {{ total_pages }}</span>
        {% if current_page < total_pages %}
        <a href="/api/s3h/{{ search_term }}?p={{ current_page + 1 }}">Página Siguiente</a>
        {% endif %}
    </div>
    {% else %}
    <div style="text-align: center; padding: 40px;">
        <h3>No se encontraron resultados para "{{ search_term }}"</h3>
    </div>
    {% endif %}

    <script>
        async function convertToBase64(code) {
            const imgElement = document.getElementById(`img-${code}`);
            const galleryElement = document.getElementById(`gallery-${code}`);
            const btnElement = event.target;
            const originalSrc = imgElement.dataset.originalSrc;
            
            if (!originalSrc || originalSrc.includes('base64') || originalSrc.includes('via.placeholder.com')) {
                return;
            }
            
            btnElement.disabled = true;
            btnElement.textContent = 'Convirtiendo...';
            galleryElement.classList.add('loading');
            
            try {
                const response = await fetch('/api/proxy-image?url=' + encodeURIComponent(originalSrc));
                const blob = await response.blob();
                
                const reader = new FileReader();
                reader.onload = function() {
                    const base64 = reader.result;
                    imgElement.src = base64;
                    btnElement.textContent = '¡Convertida!';
                    galleryElement.classList.remove('loading');
                    
                    setTimeout(() => {
                        btnElement.disabled = false;
                        btnElement.textContent = 'Convertir a Base64';
                    }, 2000);
                };
                reader.readAsDataURL(blob);
                
            } catch (error) {
                console.error('Error convirtiendo imagen:', error);
                btnElement.textContent = 'Error';
                galleryElement.classList.remove('loading');
                
                setTimeout(() => {
                    btnElement.disabled = false;
                    btnElement.textContent = 'Convertir a Base64';
                }, 2000);
            }
        }

        async function convertAllImages() {
            const convertButtons = document.querySelectorAll('.convert-btn');
            const convertAllBtn = document.querySelector('.convert-all-btn');
            
            convertAllBtn.disabled = true;
            convertAllBtn.textContent = 'Convirtiendo todas...';
            
            for (let i = 0; i < convertButtons.length; i++) {
                const btn = convertButtons[i];
                const galleryElement = btn.closest('.gallery-item');
                const code = galleryElement.id.replace('gallery-', '');
                const imgElement = document.getElementById(`img-${code}`);
                const originalSrc = imgElement.dataset.originalSrc;
                
                if (originalSrc && !originalSrc.includes('base64') && !originalSrc.includes('via.placeholder.com')) {
                    btn.click();
                    await new Promise(resolve => setTimeout(resolve, 1000));
                }
            }
            
            convertAllBtn.disabled = false;
            convertAllBtn.textContent = 'Convertir Todas las Imágenes a Base64';
        }

        document.addEventListener('DOMContentLoaded', function() {
            const images = document.querySelectorAll('img[data-original-src]');
            images.forEach(img => {
                img.addEventListener('error', function() {
                    if (this.src && !this.src.includes('via.placeholder.com')) {
                        this.src = 'https://via.placeholder.com/200x300?text=Error+cargando+imagen';
                    }
                });
            });
        });
    </script>
</body>
</html>
'''

VIEW_NH_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }} - nHentai</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .search-header {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .search-form {
            display: flex;
            gap: 10px;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .search-form input {
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            min-width: 300px;
        }
        
        .search-form button {
            padding: 12px 24px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        
        .gallery-header {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        @media (min-width: 768px) {
            .gallery-header {
                flex-direction: row;
                align-items: flex-start;
            }
        }
        
        .cover-container {
            flex-shrink: 0;
            width: 100%;
            max-width: 300px;
            margin: 0 auto;
        }
        
        @media (min-width: 768px) {
            .cover-container {
                width: 300px;
                margin: 0;
            }
        }
        
        .cover-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
            border-radius: 8px;
            cursor: pointer;
        }
        
        .info-container {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .gallery-title {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            line-height: 1.3;
        }
        
        .gallery-code {
            color: #666;
            font-size: 16px;
            margin-bottom: 10px;
        }
        
        .tags-section {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .tag-category {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: flex-start;
        }
        
        .tag-category strong {
            min-width: 80px;
            color: #333;
            font-size: 14px;
        }
        
        .tag-list {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            flex: 1;
        }
        
        .tag {
            background: #e9ecef;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            color: #495057;
        }
        
        .download-section {
            margin-top: 10px;
        }
        
        .download-btn {
            background: #28a745;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .download-btn:hover {
            background: #218838;
        }
        
        .download-btn:disabled {
            background: #6c757d;
            cursor: not-allowed;
        }
        
        .progress-info {
            margin-top: 10px;
            font-size: 14px;
            color: #666;
        }
        
        .gallery-section {
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .gallery-title-section {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #333;
        }
        
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }
        
        @media (min-width: 768px) {
            .gallery-grid {
                grid-template-columns: repeat(5, 1fr);
                gap: 15px;
            }
        }
        
        .gallery-item {
            border-radius: 8px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .gallery-item:hover {
            transform: scale(1.05);
        }
        
        .gallery-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.95);
            z-index: 1000;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        .modal-content {
            position: relative;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .modal-image {
            max-width: 95%;
            max-height: 95%;
            object-fit: contain;
            transition: transform 0.3s ease;
        }
        
        .image-counter {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            color: white;
            background: rgba(0,0,0,0.7);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 14px;
            z-index: 1001;
        }
        
        .modal-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            cursor: pointer;
        }
        
        .loading {
            opacity: 0.7;
        }
        
        .scrollable-gallery {
            width: 100%;
            height: 100vh;
            overflow-y: auto;
            scroll-snap-type: y mandatory;
        }
        
        .scrollable-gallery img {
            width: 100%;
            height: 100vh;
            object-fit: contain;
            scroll-snap-align: start;
        }
    </style>
</head>
<body>
    <div class="search-header">
        <form class="search-form" method="GET" action="/api/snh/">
            <input type="text" name="q" placeholder="Buscar en nHentai..." required>
            <button type="submit">🔍 Buscar</button>
        </form>
    </div>
    
    <div class="gallery-header">
        <div class="cover-container">
            <img src="{{ cover_image }}" 
                 alt="{{ title }}" 
                 class="cover-image"
                 onclick="openModal(0)"
                 onerror="this.src='https://via.placeholder.com/300x400?text=Cover+no+disponible'">
        </div>
        
        <div class="info-container">
            <div>
                <div class="gallery-code">Código: {{ code }}</div>
                <h1 class="gallery-title">{{ title }}</h1>
            </div>
            
            <div class="tags-section">
                {% for category, tags in tags.items() %}
                <div class="tag-category">
                    <strong>{{ category }}:</strong>
                    <div class="tag-list">
                        {% for tag in tags %}
                        <span class="tag">{{ tag }}</span>
                        {% endfor %}
                    </div>
                </div>
                {% endfor %}
            </div>
            
            <div class="download-section">
                <button class="download-btn" onclick="downloadCBZ()">
                    📥 Descargar CBZ
                </button>
                <div class="progress-info" id="progressInfo"></div>
            </div>
        </div>
    </div>
    
    <div class="gallery-section">
        <h2 class="gallery-title-section">Galería de Imágenes ({{ image_links|length }})</h2>
        <div class="gallery-grid">
            {% for image_url in image_links %}
            <div class="gallery-item" onclick="openModal({{ loop.index0 }})">
                <img src="{{ image_url }}" 
                     alt="Imagen {{ loop.index }}" 
                     class="gallery-image"
                     onerror="this.src='https://via.placeholder.com/200x300?text=Error+cargando'"
                     loading="lazy">
            </div>
            {% endfor %}
        </div>
    </div>
    
    <div class="modal" id="imageModal">
        <div class="image-counter" id="imageCounter"></div>
        <div class="modal-content">
            <div class="modal-overlay" onclick="closeModal()"></div>
            <img class="modal-image" id="modalImage" src="" onclick="closeModal()">
        </div>
    </div>

    <script>
        let currentImageIndex = 0;
        const totalImages = {{ image_links|length }};
        const imageLinks = {{ image_links|tojson }};
        const cleanTitle = "{{ clean_title }}";
        const code = "{{ code }}";
        let touchStartY = 0;
        let touchEndY = 0;
        
        function openModal(index) {
            currentImageIndex = index;
            const modal = document.getElementById('imageModal');
            const modalImage = document.getElementById('modalImage');
            const imageCounter = document.getElementById('imageCounter');
            
            modalImage.src = imageLinks[index];
            imageCounter.textContent = `${index + 1} / ${totalImages}`;
            modal.style.display = 'flex';
            document.body.style.overflow = 'hidden';
            
            // Configurar eventos táctiles
            modalImage.addEventListener('touchstart', handleTouchStart, false);
            modalImage.addEventListener('touchend', handleTouchEnd, false);
        }
        
        function closeModal() {
            const modal = document.getElementById('imageModal');
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
        
        function handleTouchStart(event) {
            touchStartY = event.changedTouches[0].screenY;
        }
        
        function handleTouchEnd(event) {
            touchEndY = event.changedTouches[0].screenY;
            handleSwipe();
        }
        
        function handleSwipe() {
            const swipeDistance = touchStartY - touchEndY;
            const swipeThreshold = 50;
            
            if (Math.abs(swipeDistance) > swipeThreshold) {
                if (swipeDistance > 0) {
                    // Swipe hacia arriba - siguiente imagen
                    navigateImage(1);
                } else {
                    // Swipe hacia abajo - imagen anterior
                    navigateImage(-1);
                }
            }
        }
        
        function navigateImage(direction) {
            let newIndex = currentImageIndex + direction;
            
            if (newIndex < 0) {
                newIndex = totalImages - 1;
            } else if (newIndex >= totalImages) {
                newIndex = 0;
            }
            
            openModal(newIndex);
        }
        
        document.addEventListener('keydown', function(e) {
            const modal = document.getElementById('imageModal');
            if (modal.style.display === 'flex') {
                if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
                    navigateImage(-1);
                } else if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
                    navigateImage(1);
                } else if (e.key === 'Escape') {
                    closeModal();
                }
            }
        });
        
        // Navegación con rueda del mouse
        document.getElementById('imageModal').addEventListener('wheel', function(e) {
            e.preventDefault();
            if (e.deltaY < 0) {
                // Rueda hacia arriba - imagen anterior
                navigateImage(-1);
            } else {
                // Rueda hacia abajo - siguiente imagen
                navigateImage(1);
            }
        }, { passive: false });
        
        async function downloadCBZ() {
            const btn = document.querySelector('.download-btn');
            const progressInfo = document.getElementById('progressInfo');
            
            btn.disabled = true;
            btn.textContent = '⏳ Preparando...';
            
            try {
                const formData = new FormData();
                formData.append('title', cleanTitle);
                formData.append('code', code);
                
                let downloadedCount = 0;
                
                for (let i = 0; i < imageLinks.length; i++) {
                    progressInfo.textContent = `Descargando ${i + 1}/${imageLinks.length}`;
                    
                    try {
                        const response = await fetch('/api/proxy-image?url=' + encodeURIComponent(imageLinks[i]));
                        if (!response.ok) throw new Error('HTTP error ' + response.status);
                        
                        const blob = await response.blob();
                        const contentType = response.headers.get('content-type');
                        let ext = '.jpg';
                        
                        if (contentType) {
                            if (contentType.includes('jpeg') || contentType.includes('jpg')) {
                                ext = '.jpg';
                            } else if (contentType.includes('png')) {
                                ext = '.png';
                            } else if (contentType.includes('webp')) {
                                ext = '.webp';
                            } else if (contentType.includes('gif')) {
                                ext = '.gif';
                            }
                        }
                        
                        const filename = `image_${i + 1}${ext}`;
                        formData.append(`file_${i}`, blob, filename);
                        downloadedCount++;
                        
                    } catch (error) {
                        console.error(`Error descargando imagen ${i + 1}:`, error);
                        progressInfo.textContent = `Error en imagen ${i + 1}, continuando...`;
                        await new Promise(resolve => setTimeout(resolve, 500));
                    }
                }
                
                progressInfo.textContent = 'Creando CBZ...';
                
                const response = await fetch('/api/create-cbz', {
                    method: 'POST',
                    body: formData
                });
                
                if (!response.ok) {
                    throw new Error('Error al crear CBZ');
                }
                
                const blob = await response.blob();
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `${cleanTitle}_${code}.cbz`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                
                progressInfo.textContent = '✅ Descarga completada!';
                btn.textContent = '📥 Descargar CBZ';
                
            } catch (error) {
                console.error('Error en la descarga:', error);
                progressInfo.textContent = '❌ Error en la descarga: ' + error.message;
                btn.textContent = '📥 Reintentar Descarga';
            } finally {
                btn.disabled = false;
                
                setTimeout(() => {
                    progressInfo.textContent = '';
                }, 5000);
            }
        }
        
        function preloadImages() {
            imageLinks.forEach((url, index) => {
                if (index < 10) {
                    const img = new Image();
                    img.src = url;
                }
            });
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            preloadImages();
        });
    </script>
</body>
</html>
'''

VIEW_3H_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }} - 3Hentai</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .gallery-header {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        @media (min-width: 768px) {
            .gallery-header {
                flex-direction: row;
                align-items: flex-start;
            }
        }
        .cover-container {
            flex-shrink: 0;
            width: 100%;
            max-width: 300px;
            margin: 0 auto;
        }
        @media (min-width: 768px) {
            .cover-container {
                width: 300px;
                margin: 0;
            }
        }
        .cover-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
            border-radius: 8px;
            cursor: pointer;
        }
        .info-container {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .gallery-title {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            line-height: 1.3;
        }
        .gallery-code {
            color: #666;
            font-size: 16px;
            margin-bottom: 10px;
        }
        .tags-section {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .tag-category {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: flex-start;
        }
        .tag-category strong {
            min-width: 80px;
            color: #333;
            font-size: 14px;
        }
        .tag-list {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            flex: 1;
        }
        .tag {
            background: #e9ecef;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            color: #495057;
        }
        .download-section {
            margin-top: 10px;
        }
        .download-btn {
            background: #28a745;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s;
        }
        .download-btn:hover {
            background: #218838;
        }
        .download-btn:disabled {
            background: #6c757d;
            cursor: not-allowed;
        }
        .progress-info {
            margin-top: 10px;
            font-size: 14px;
            color: #666;
        }
        .gallery-section {
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .gallery-title-section {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #333;
        }
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }
        @media (min-width: 768px) {
            .gallery-grid {
                grid-template-columns: repeat(5, 1fr);
                gap: 15px;
            }
        }
        .gallery-item {
            border-radius: 8px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .gallery-item:hover {
            transform: scale(1.05);
        }
        .gallery-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.95);
            z-index: 1000;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            position: relative;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .modal-image {
            max-width: 95%;
            max-height: 95%;
            object-fit: contain;
            transition: transform 0.3s ease;
        }
        .image-counter {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            color: white;
            background: rgba(0,0,0,0.7);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 14px;
            z-index: 1001;
        }
        .modal-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            cursor: pointer;
        }
        .loading {
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class="gallery-header">
        <div class="cover-container">
            <img src="{{ cover_image }}" 
                 alt="{{ title }}" 
                 class="cover-image"
                 onclick="openModal(0)"
                 onerror="this.src='https://via.placeholder.com/300x400?text=Cover+no+disponible'">
        </div>
        <div class="info-container">
            <div>
                <div class="gallery-code">Código: {{ code }}</div>
                <h1 class="gallery-title">{{ title }}</h1>
                <div class="gallery-code">Total de páginas: {{ total_pages }}</div>
            </div>
            <div class="tags-section">
                {% for category, tags in tags.items() %}
                <div class="tag-category">
                    <strong>{{ category }}:</strong>
                    <div class="tag-list">
                        {% for tag in tags %}
                        <span class="tag">{{ tag }}</span>
                        {% endfor %}
                    </div>
                </div>
                {% endfor %}
            </div>
            <div class="download-section">
                <button class="download-btn" onclick="downloadCBZ()">
                    Descargar CBZ
                </button>
                <div class="progress-info" id="progressInfo"></div>
            </div>
        </div>
    </div>
    <div class="gallery-section">
        <h2 class="gallery-title-section">Galería de Imágenes ({{ image_links|length }})</h2>
        <div class="gallery-grid">
            {% for image_url in image_links %}
            <div class="gallery-item" onclick="openModal({{ loop.index0 }})">
                <img src="{{ image_url }}" 
                     alt="Imagen {{ loop.index }}" 
                     class="gallery-image"
                     onerror="this.src='https://via.placeholder.com/200x300?text=Error+cargando'"
                     loading="lazy">
            </div>
            {% endfor %}
        </div>
    </div>
    <div class="modal" id="imageModal">
        <div class="image-counter" id="imageCounter"></div>
        <div class="modal-content">
            <div class="modal-overlay" onclick="closeModal()"></div>
            <img class="modal-image" id="modalImage" src="" onclick="closeModal()">
        </div>
    </div>
    <script>
        let currentImageIndex = 0;
        const totalImages = {{ image_links|length }};
        const imageLinks = {{ image_links|tojson }};
        const cleanTitle = "{{ clean_title }}";
        const code = "{{ code }}";
        let touchStartY = 0;
        let touchEndY = 0;
        
        function openModal(index) {
            currentImageIndex = index;
            const modal = document.getElementById('imageModal');
            const modalImage = document.getElementById('modalImage');
            const imageCounter = document.getElementById('imageCounter');
            
            modalImage.src = imageLinks[index];
            imageCounter.textContent = `${index + 1} / ${totalImages}`;
            modal.style.display = 'flex';
            document.body.style.overflow = 'hidden';
            
            // Configurar eventos táctiles
            modalImage.addEventListener('touchstart', handleTouchStart, false);
            modalImage.addEventListener('touchend', handleTouchEnd, false);
        }
        
        function closeModal() {
            const modal = document.getElementById('imageModal');
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
        
        function handleTouchStart(event) {
            touchStartY = event.changedTouches[0].screenY;
        }
        
        function handleTouchEnd(event) {
            touchEndY = event.changedTouches[0].screenY;
            handleSwipe();
        }
        
        function handleSwipe() {
            const swipeDistance = touchStartY - touchEndY;
            const swipeThreshold = 50;
            
            if (Math.abs(swipeDistance) > swipeThreshold) {
                if (swipeDistance > 0) {
                    // Swipe hacia arriba - siguiente imagen
                    navigateImage(1);
                } else {
                    // Swipe hacia abajo - imagen anterior
                    navigateImage(-1);
                }
            }
        }
        
        function navigateImage(direction) {
            let newIndex = currentImageIndex + direction;
            if (newIndex < 0) {
                newIndex = totalImages - 1;
            } else if (newIndex >= totalImages) {
                newIndex = 0;
            }
            openModal(newIndex);
        }
        
        document.addEventListener('keydown', function(e) {
            const modal = document.getElementById('imageModal');
            if (modal.style.display === 'flex') {
                if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
                    navigateImage(-1);
                } else if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
                    navigateImage(1);
                } else if (e.key === 'Escape') {
                    closeModal();
                }
            }
        });
        
        // Navegación con rueda del mouse
        document.getElementById('imageModal').addEventListener('wheel', function(e) {
            e.preventDefault();
            if (e.deltaY < 0) {
                // Rueda hacia arriba - imagen anterior
                navigateImage(-1);
            } else {
                // Rueda hacia abajo - siguiente imagen
                navigateImage(1);
            }
        }, { passive: false });
        
        async function downloadCBZ() {
            const btn = document.querySelector('.download-btn');
            const progressInfo = document.getElementById('progressInfo');
            
            btn.disabled = true;
            btn.textContent = 'Preparando...';
            
            try {
                const formData = new FormData();
                formData.append('title', cleanTitle);
                formData.append('code', code);
                
                let downloadedCount = 0;
                
                for (let i = 0; i < imageLinks.length; i++) {
                    progressInfo.textContent = `Descargando ${i + 1}/${imageLinks.length}`;
                    
                    try {
                        const response = await fetch('/api/proxy-image?url=' + encodeURIComponent(imageLinks[i]));
                        if (!response.ok) throw new Error('HTTP error ' + response.status);
                        
                        const blob = await response.blob();
                        const contentType = response.headers.get('content-type');
                        let ext = '.jpg';
                        
                        if (contentType) {
                            if (contentType.includes('jpeg') || contentType.includes('jpg')) {
                                ext = '.jpg';
                            } else if (contentType.includes('png')) {
                                ext = '.png';
                            } else if (contentType.includes('webp')) {
                                ext = '.webp';
                            } else if (contentType.includes('gif')) {
                                ext = '.gif';
                            }
                        }
                        
                        const filename = `image_${i + 1}${ext}`;
                        formData.append(`file_${i}`, blob, filename);
                        downloadedCount++;
                        
                    } catch (error) {
                        console.error(`Error descargando imagen ${i + 1}:`, error);
                        progressInfo.textContent = `Error en imagen ${i + 1}, continuando...`;
                        await new Promise(resolve => setTimeout(resolve, 500));
                    }
                }
                
                progressInfo.textContent = 'Creando CBZ...';
                
                const response = await fetch('/api/create-cbz', {
                    method: 'POST',
                    body: formData
                });
                
                if (!response.ok) {
                    throw new Error('Error al crear CBZ');
                }
                
                const blob = await response.blob();
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `${cleanTitle}_${code}.cbz`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                
                progressInfo.textContent = 'Descarga completada!';
                btn.textContent = 'Descargar CBZ';
                
            } catch (error) {
                console.error('Error en la descarga:', error);
                progressInfo.textContent = 'Error en la descarga: ' + error.message;
                btn.textContent = 'Reintentar Descarga';
            } finally {
                btn.disabled = false;
                setTimeout(() => {
                    progressInfo.textContent = '';
                }, 5000);
            }
        }
        
        function preloadImages() {
            imageLinks.forEach((url, index) => {
                if (index < 10) {
                    const img = new Image();
                    img.src = url;
                }
            });
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            preloadImages();
        });
    </script>
</body>
</html>
'''
