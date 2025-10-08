LOGIN_TEMPLATE = """
<!doctype html>
<html><head><title>Login</title><meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="styles.css">
</head>
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
    <link rel="stylesheet" href="styles.css">
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
    <link rel="stylesheet" href="styles.css">
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
                }, 5000);
            } else {
                clearInterval(autoRefreshInterval);
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
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
    <link rel="stylesheet" href="styles.css">
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
        
        function submitForm(form, event) {
            event.preventDefault();
            if (confirm('¿Estás seguro de que quieres realizar esta acción?')) {
                form.submit();
            }
        }
    </script>
</body>
</html>
"""

GALLERY_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Galería de Imágenes</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
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
    <link rel="stylesheet" href="styles.css">
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

VIEW_NH_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }} - nHentai</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="search-section">
        <form method="GET" action="/api/snh/" class="search-form">
            <input type="text" name="q" value="{{ search_term or '' }}" placeholder="Buscar en nHentai..." class="search-input" required>
            <button type="submit" class="search-btn">Buscar</button>
        </form>
    </div>

    <div class="gallery-header">
        <div class="cover-container">
            <img src="{{ cover_image }}" 
                 alt="{{ title }}" 
                 class="cover-image"
                 onclick="openCascadeModal(0)"
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
        <div class="cascade-gallery">
            {% for image_url in image_links %}
            <img src="{{ image_url }}" 
                 alt="Imagen {{ loop.index }}" 
                 class="cascade-image"
                 onclick="openCascadeModal({{ loop.index0 }})"
                 onerror="this.src='https://via.placeholder.com/800x1200?text=Error+cargando'"
                 loading="lazy">
            {% endfor %}
        </div>
    </div>
    
    <div class="cascade-modal" id="cascadeModal">
        <div class="image-counter" id="imageCounter"></div>
        <div class="cascade-modal-content" id="cascadeModalContent">
            {% for image_url in image_links %}
            <img src="{{ image_url }}" 
                 alt="Imagen {{ loop.index }}" 
                 class="cascade-modal-image"
                 onerror="this.src='https://via.placeholder.com/800x1200?text=Error+cargando'">
            {% endfor %}
        </div>
    </div>

    <script>
        let currentImageIndex = 0;
        const totalImages = {{ image_links|length }};
        const imageLinks = {{ image_links|tojson }};
        const cleanTitle = "{{ clean_title }}";
        const code = "{{ code }}";
        
        function openCascadeModal(index) {
            currentImageIndex = index;
            const modal = document.getElementById('cascadeModal');
            const imageCounter = document.getElementById('imageCounter');
            
            imageCounter.textContent = `${index + 1} / ${totalImages}`;
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
            
            const targetImage = document.querySelectorAll('.cascade-modal-image')[index];
            targetImage.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        
        function closeCascadeModal() {
            const modal = document.getElementById('cascadeModal');
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
        
        function navigateImage(direction) {
            let newIndex = currentImageIndex + direction;
            
            if (newIndex < 0) {
                newIndex = totalImages - 1;
            } else if (newIndex >= totalImages) {
                newIndex = 0;
            }
            
            openCascadeModal(newIndex);
        }
        
        document.getElementById('cascadeModal').addEventListener('click', function(e) {
            if (e.target === this || e.target.classList.contains('cascade-modal-image')) {
                closeCascadeModal();
            }
        });
        
        document.addEventListener('keydown', function(e) {
            const modal = document.getElementById('cascadeModal');
            if (modal.style.display === 'block') {
                if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
                    navigateImage(-1);
                } else if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
                    navigateImage(1);
                } else if (e.key === 'Escape') {
                    closeCascadeModal();
                }
            }
        });
        
        document.getElementById('cascadeModalContent').addEventListener('wheel', function(e) {
            e.preventDefault();
            if (e.deltaY > 0) {
                navigateImage(1);
            } else {
                navigateImage(-1);
            }
        });
        
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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="gallery-header">
        <div class="cover-container">
            <img src="{{ cover_image }}" 
                 alt="{{ title }}" 
                 class="cover-image"
                 onclick="openCascadeModal(0)"
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
        <div class="cascade-gallery">
            {% for image_url in image_links %}
            <img src="{{ image_url }}" 
                 alt="Imagen {{ loop.index }}" 
                 class="cascade-image"
                 onclick="openCascadeModal({{ loop.index0 }})"
                 onerror="this.src='https://via.placeholder.com/800x1200?text=Error+cargando'"
                 loading="lazy">
            {% endfor %}
        </div>
    </div>
    <div class="cascade-modal" id="cascadeModal">
        <div class="image-counter" id="imageCounter"></div>
        <div class="cascade-modal-content" id="cascadeModalContent">
            {% for image_url in image_links %}
            <img src="{{ image_url }}" 
                 alt="Imagen {{ loop.index }}" 
                 class="cascade-modal-image"
                 onerror="this.src='https://via.placeholder.com/800x1200?text=Error+cargando'">
            {% endfor %}
        </div>
    </div>
    <script>
        let currentImageIndex = 0;
        const totalImages = {{ image_links|length }};
        const imageLinks = {{ image_links|tojson }};
        const cleanTitle = "{{ clean_title }}";
        const code = "{{ code }}";
        
        function openCascadeModal(index) {
            currentImageIndex = index;
            const modal = document.getElementById('cascadeModal');
            const imageCounter = document.getElementById('imageCounter');
            
            imageCounter.textContent = `${index + 1} / ${totalImages}`;
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
            
            const targetImage = document.querySelectorAll('.cascade-modal-image')[index];
            targetImage.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        
        function closeCascadeModal() {
            const modal = document.getElementById('cascadeModal');
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
        
        function navigateImage(direction) {
            let newIndex = currentImageIndex + direction;
            if (newIndex < 0) {
                newIndex = totalImages - 1;
            } else if (newIndex >= totalImages) {
                newIndex = 0;
            }
            openCascadeModal(newIndex);
        }
        
        document.getElementById('cascadeModal').addEventListener('click', function(e) {
            if (e.target === this || e.target.classList.contains('cascade-modal-image')) {
                closeCascadeModal();
            }
        });
        
        document.addEventListener('keydown', function(e) {
            const modal = document.getElementById('cascadeModal');
            if (modal.style.display === 'block') {
                if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
                    navigateImage(-1);
                } else if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
                    navigateImage(1);
                } else if (e.key === 'Escape') {
                    closeCascadeModal();
                }
            }
        });
        
        document.getElementById('cascadeModalContent').addEventListener('wheel', function(e) {
            e.preventDefault();
            if (e.deltaY > 0) {
                navigateImage(1);
            } else {
                navigateImage(-1);
            }
        });
        
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
