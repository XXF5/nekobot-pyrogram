NEW_MAIN_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Explorador de Archivos</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body { font-family: Arial; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; margin-bottom: 20px; }
        
        .folder { margin: 10px 0; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }
        .folder-header { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            padding: 15px; 
            cursor: pointer; 
            display: flex; 
            justify-content: space-between; 
            align-items: center;
            transition: background 0.3s;
        }
        .folder-header:hover { background: linear-gradient(135deg, #5a6fd8 0%, #6a3f8f 100%); }
        .folder-content { padding: 15px; display: none; }
        
        .file-item { 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            padding: 12px 15px; 
            border-bottom: 1px solid #eee; 
            transition: background 0.2s;
        }
        .file-item:hover { background: #f8f9fa; }
        .file-item:last-child { border-bottom: none; }
        
        .file-info { 
            display: flex; 
            align-items: center; 
            gap: 10px; 
            flex: 1; 
            min-width: 0;
        }
        .file-index { 
            background: #667eea; 
            color: white; 
            padding: 2px 8px; 
            border-radius: 12px; 
            font-size: 12px; 
            flex-shrink: 0;
        }
        .file-name { 
            flex: 1; 
            min-width: 0; 
            overflow: hidden; 
            text-overflow: ellipsis; 
            white-space: nowrap;
            font-weight: 500;
        }
        .file-name a {
            color: #333;
            text-decoration: none;
        }
        .file-name a:hover {
            color: #667eea;
            text-decoration: underline;
        }
        .file-size { 
            color: #666; 
            font-size: 12px; 
            flex-shrink: 0;
            margin-left: 10px;
        }
        .file-type { 
            color: #888; 
            font-size: 11px; 
            background: #e9ecef;
            padding: 2px 6px;
            border-radius: 3px;
            margin-left: 5px;
        }
        
        .file-actions { 
            display: flex; 
            gap: 8px; 
            flex-shrink: 0;
        }
        
        .action-btn {
            padding: 6px 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 4px;
            min-width: 28px;
            justify-content: center;
        }
        .btn-download { background: #28a745; color: white; }
        .btn-download:hover { background: #218838; }
        .btn-gallery { background: #17a2b8; color: white; }
        .btn-gallery:hover { background: #138496; }
        .btn-create-cbz { background: #9c27b0; color: white; }
        .btn-create-cbz:hover { background: #7b1fa2; }
        .btn-rename { background: #ffc107; color: black; }
        .btn-rename:hover { background: #e0a800; }
        .btn-delete { background: #dc3545; color: white; }
        .btn-delete:hover { background: #c82333; }
        .btn-compress { background: #6f42c1; color: white; }
        .btn-compress:hover { background: #5a369c; }
        .btn-move { background: #20c997; color: white; }
        .btn-move:hover { background: #1ba87e; }
        
        .nav { 
            margin-bottom: 20px; 
            display: flex; 
            gap: 10px; 
            flex-wrap: wrap;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
        }
        .nav a { 
            color: white;
            text-decoration: none; 
            padding: 8px 16px; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 4px; 
            transition: transform 0.2s;
        }
        .nav a:hover {
            transform: translateY(-2px);
            text-decoration: none;
        }
        
        .total-files { 
            background: #e9ecef; 
            padding: 12px; 
            border-radius: 4px; 
            margin: 10px 0; 
            text-align: center;
            font-weight: 500;
            color: #495057;
        }
        
        .bulk-actions {
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
            justify-content: center;
        }
        
        .bulk-btn {
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            transition: transform 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .btn-select-all { background: #6c757d; color: white; }
        .btn-select-all:hover { background: #5a6268; transform: translateY(-2px); }
        .btn-delete-empty { background: #fd7e14; color: white; }
        .btn-delete-empty:hover { background: #e06c10; transform: translateY(-2px); }
        .btn-compress-selected { background: #6f42c1; color: white; }
        .btn-compress-selected:hover { background: #5a369c; transform: translateY(-2px); }
        .btn-merge-cbz { background: #9c27b0; color: white; }
        .btn-merge-cbz:hover { background: #7b1fa2; transform: translateY(-2px); }
        .btn-move-selected { background: #20c997; color: white; }
        .btn-move-selected:hover { background: #1ba87e; transform: translateY(-2px); }
        .btn-delete-selected { background: #dc3545; color: white; }
        .btn-delete-selected:hover { background: #c82333; transform: translateY(-2px); }
        
        .checkbox-item {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-right: 15px;
        }
        .checkbox-item input[type="checkbox"] {
            width: 16px;
            height: 16px;
            cursor: pointer;
        }
        
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background: white;
            padding: 30px;
            border-radius: 10px;
            max-width: 500px;
            width: 90%;
            max-height: 80vh;
            overflow-y: auto;
        }
        .modal-title {
            margin-top: 0;
            color: #333;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .modal-actions {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
            margin-top: 20px;
        }
        .modal-btn {
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }
        .btn-confirm { background: #28a745; color: white; }
        .btn-cancel { background: #6c757d; color: white; }
        
        select, input[type="text"] {
            width: 100%;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            margin-bottom: 15px;
        }
        select:focus, input[type="text"]:focus {
            border-color: #667eea;
            outline: none;
        }
        
        .folder-selector {
            max-height: 200px;
            overflow-y: auto;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            margin-bottom: 15px;
        }
        .folder-option {
            padding: 8px;
            cursor: pointer;
            border-radius: 4px;
            margin-bottom: 5px;
            transition: background 0.2s;
        }
        .folder-option:hover {
            background: #f8f9fa;
        }
        .folder-option.selected {
            background: #e3f2fd;
            border-left: 4px solid #667eea;
        }
        
        .cbz-selector {
            max-height: 300px;
            overflow-y: auto;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            margin-bottom: 15px;
        }
        .cbz-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 8px;
            border-bottom: 1px solid #eee;
        }
        .cbz-item:last-child {
            border-bottom: none;
        }
        .cbz-item-handle {
            cursor: move;
            color: #666;
        }
        .cbz-item-name {
            flex: 1;
            font-size: 14px;
        }
        .cbz-item-checkbox input[type="checkbox"] {
            width: 16px;
            height: 16px;
        }
        
        .sortable-ghost {
            opacity: 0.4;
        }
        .sortable-drag {
            background: #f8f9fa;
        }
        
        @media (max-width: 768px) {
            .container { padding: 10px; }
            .file-actions { flex-wrap: wrap; justify-content: flex-end; }
            .action-btn { padding: 5px 8px; font-size: 11px; }
            .nav { flex-direction: column; }
            .nav a { text-align: center; }
            .bulk-actions { flex-direction: column; }
        }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/sortablejs@1.14.0/Sortable.min.js"></script>
    <script>
        let selectedItems = new Set();
        
        function toggleFolder(folderName) {
            const content = document.getElementById('content-' + folderName);
            const icon = document.getElementById('icon-' + folderName);
            if (content.style.display === 'block') {
                content.style.display = 'none';
                icon.textContent = '▶';
            } else {
                content.style.display = 'block';
                icon.textContent = '▼';
            }
        }
        
        function selectItem(itemPath, checkbox) {
            if (checkbox.checked) {
                selectedItems.add(itemPath);
            } else {
                selectedItems.delete(itemPath);
            }
            updateBulkActions();
        }
        
        function selectAllItems() {
            const checkboxes = document.querySelectorAll('input[type="checkbox"]');
            checkboxes.forEach(checkbox => {
                checkbox.checked = true;
                if (checkbox.dataset.path) {
                    selectedItems.add(checkbox.dataset.path);
                }
            });
            updateBulkActions();
        }
        
        function updateBulkActions() {
            const count = selectedItems.size;
            document.querySelectorAll('.bulk-btn').forEach(btn => {
                if (btn.classList.contains('btn-select-all')) return;
                btn.disabled = count === 0;
            });
            
            if (count > 0) {
                document.getElementById('selectedCount').textContent = ` (${count} seleccionados)`;
            } else {
                document.getElementById('selectedCount').textContent = '';
            }
        }
        
        function showRenameInput(filePath, currentName) {
            const newName = prompt("Nuevo nombre:", currentName);
            if (newName && newName !== currentName) {
                const form = document.getElementById('rename-form');
                document.getElementById('old_path').value = filePath;
                document.getElementById('new_name').value = newName;
                form.submit();
            }
        }
        
        function showMoveDialog() {
            if (selectedItems.size === 0) return;
            
            fetch('/api/folders')
                .then(response => response.json())
                .then(folders => {
                    const modal = document.getElementById('moveModal');
                    const list = document.getElementById('folderList');
                    list.innerHTML = '';
                    
                    folders.forEach(folder => {
                        const div = document.createElement('div');
                        div.className = 'folder-option';
                        div.textContent = folder;
                        div.onclick = function() {
                            document.querySelectorAll('.folder-option').forEach(el => el.classList.remove('selected'));
                            this.classList.add('selected');
                            document.getElementById('selectedFolder').value = folder;
                        };
                        list.appendChild(div);
                    });
                    
                    modal.style.display = 'flex';
                    document.getElementById('newFolderInput').style.display = 'none';
                });
        }
        
        function showCompressDialog() {
            if (selectedItems.size === 0) return;
            
            const modal = document.getElementById('compressModal');
            modal.style.display = 'flex';
            document.getElementById('archiveName').value = `archivo_${Date.now()}`;
        }

        function showMergeCbzDialog() {
            const currentFolder = window.location.pathname;
            let actualPath = "";
            
            if (currentFolder === "/" || currentFolder === "/browse") {
                actualPath = "";
            } else if (currentFolder.startsWith("/browse")) {
                const match = currentFolder.match(/\/browse\?path=(.*)/);
                if (match && match[1]) {
                    actualPath = decodeURIComponent(match[1]);
                } else {
                    actualPath = "";
                }
            } else {
                actualPath = currentFolder.replace(/^\//, "");
            }
            
            fetch(`/api/list_cbz?path=${encodeURIComponent(actualPath)}`)
                .then(response => response.json())
                .then(cbzFiles => {
                    if (cbzFiles.length === 0) {
                        alert('No hay archivos CBZ en este directorio');
                        return;
                    }
                    
                    const modal = document.getElementById('mergeCbzModal');
                    const list = document.getElementById('cbzList');
                    list.innerHTML = '';
                    
                    cbzFiles.forEach(cbzFile => {
                        const div = document.createElement('div');
                        div.className = 'cbz-item';
                        div.dataset.path = cbzFile.path;
                        
                        div.innerHTML = `
                            <div class="cbz-item-handle">☰</div>
                            <div class="cbz-item-name">${cbzFile.name}</div>
                            <div class="cbz-item-checkbox">
                                <input type="checkbox" onchange="toggleCbzSelection(this)">
                            </div>
                        `;
                        
                        list.appendChild(div);
                    });
                    
                    modal.style.display = 'flex';
                    document.getElementById('mergedCbzName').value = `combinado_${Date.now()}.cbz`;
                    
                    Sortable.create(list, {
                        handle: '.cbz-item-handle',
                        ghostClass: 'sortable-ghost',
                        dragClass: 'sortable-drag',
                        animation: 150
                    });
                })
                .catch(error => {
                    console.error('Error al cargar CBZs:', error);
                    alert('Error al cargar los archivos CBZ');
                });
        }
        
        function toggleCbzSelection(checkbox) {
            const cbzItem = checkbox.closest('.cbz-item');
            if (checkbox.checked) {
                cbzItem.classList.add('selected');
            } else {
                cbzItem.classList.remove('selected');
            }
        }
        
        function toggleNewFolderInput() {
            const input = document.getElementById('newFolderInput');
            input.style.display = input.style.display === 'none' ? 'block' : 'none';
            if (input.style.display === 'block') {
                document.getElementById('newFolderName').focus();
                document.getElementById('selectedFolder').value = '';
                document.querySelectorAll('.folder-option').forEach(el => el.classList.remove('selected'));
            }
        }
        
        function submitMove() {
            const folder = document.getElementById('selectedFolder').value;
            const newFolder = document.getElementById('newFolderName').value;
            const targetFolder = newFolder || folder;
            
            if (!targetFolder) {
                alert('Selecciona una carpeta o crea una nueva');
                return;
            }
            
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/move_items';
            
            selectedItems.forEach(itemPath => {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = 'items[]';
                input.value = itemPath;
                form.appendChild(input);
            });
            
            const targetInput = document.createElement('input');
            targetInput.type = 'hidden';
            targetInput.name = 'target_folder';
            targetInput.value = targetFolder;
            form.appendChild(targetInput);
            
            document.body.appendChild(form);
            form.submit();
        }
        
        function submitCompress() {
            const archiveName = document.getElementById('archiveName').value;
            if (!archiveName) {
                alert('Ingresa un nombre para el archivo');
                return;
            }
            
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/compress_multiple';
            
            selectedItems.forEach(itemPath => {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = 'selected[]';
                input.value = itemPath;
                form.appendChild(input);
            });
            
            const nameInput = document.createElement('input');
            nameInput.type = 'hidden';
            nameInput.name = 'archive_name';
            nameInput.value = archiveName;
            form.appendChild(nameInput);
            
            document.body.appendChild(form);
            form.submit();
        }
        
        function submitMergeCbz() {
            const cbzName = document.getElementById('mergedCbzName').value;
            if (!cbzName || !cbzName.endsWith('.cbz')) {
                alert('Ingresa un nombre válido para el CBZ (debe terminar en .cbz)');
                return;
            }
            
            const selectedCbzItems = Array.from(document.querySelectorAll('#cbzList .cbz-item.selected'));
            if (selectedCbzItems.length < 2) {
                alert('Selecciona al menos 2 CBZs para combinar');
                return;
            }
            
            const cbzPaths = selectedCbzItems.map(item => item.dataset.path);
            
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/merge_cbz';
            
            cbzPaths.forEach(cbzPath => {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = 'cbz_files[]';
                input.value = cbzPath;
                form.appendChild(input);
            });
            
            const nameInput = document.createElement('input');
            nameInput.type = 'hidden';
            nameInput.name = 'output_name';
            nameInput.value = cbzName;
            form.appendChild(nameInput);
            
            document.body.appendChild(form);
            form.submit();
        }
        
        function createCbzFromFolder(folderPath, folderName) {
            if (!confirm(`¿Crear CBZ "${folderName}.cbz" en el directorio superior?`)) {
                return;
            }
            
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/create_cbz_from_folder';
            
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'folder_path';
            input.value = folderPath;
            form.appendChild(input);
            
            document.body.appendChild(form);
            form.submit();
        }
        
        function deleteSelected() {
            if (selectedItems.size === 0) return;
            
            if (!confirm(`¿Eliminar ${selectedItems.size} elemento(s) seleccionado(s)?`)) {
                return;
            }
            
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/delete_multiple';
            
            selectedItems.forEach(itemPath => {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = 'items[]';
                input.value = itemPath;
                form.appendChild(input);
            });
            
            document.body.appendChild(form);
            form.submit();
        }
        
        function deleteEmptyFolders() {
            if (!confirm('¿Eliminar todas las carpetas vacías?')) {
                return;
            }
            
            fetch('/delete_empty_folders', { method: 'POST' })
                .then(response => response.text())
                .then(result => {
                    alert(result);
                    location.reload();
                });
        }
        
        function closeModal(modalId) {
            document.getElementById(modalId).style.display = 'none';
        }
        
        function checkFolderContent(folderPath) {
            return fetch(`/api/check_folder?path=${encodeURIComponent(folderPath)}`)
                .then(response => response.json())
                .then(data => data.has_content);
        }
        
        function deleteFolder(folderPath, folderName) {
            checkFolderContent(folderPath).then(hasContent => {
                if (hasContent) {
                    if (!confirm(`La carpeta "${folderName}" no está vacía. Si continúa, perderá el contenido. ¿Continuar?`)) {
                        return;
                    }
                }
                
                const form = document.createElement('form');
                form.method = 'POST';
                form.action = '/delete_folder';
                
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = 'path';
                input.value = folderPath;
                form.appendChild(input);
                
                document.body.appendChild(form);
                form.submit();
            });
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            updateBulkActions();
        });
    </script>
</head>
<body>
    <div class="container">
        <div class="nav">
            <a href="/">🏠 Inicio</a>
            <a href="/manga">📖 Manga</a>
            <a href="/utils">🛠️ Utilidades</a>
            <a href="/downloads">📥 Descargas</a>
            {% if user_level >= 3 %}
            <a href="/webusers">👥 Usuarios Web</a>
            {% endif %}
        </div>
        
        <h1>📁 Explorador de Archivos</h1>
        
        <div class="total-files">
            <strong>Total de archivos: {{ total_files }}</strong>
            <span id="selectedCount"></span>
        </div>
        
        <form id="rename-form" action="/rename" method="POST" style="display: none;">
            <input type="hidden" id="old_path" name="old_path">
            <input type="hidden" id="new_name" name="new_name">
        </form>
        
        {% for folder_name, folder_data in folders.items() %}
        <div class="folder">
            <div class="folder-header" onclick="toggleFolder('{{ folder_name }}')">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span>📁 {{ folder_name }} ({{ folder_data["items"]|length }} archivos)</span>
                    {% if user_level >= 4 %}
                    <div class="checkbox-item">
                        <input type="checkbox" 
                               data-path="{{ folder_data['full_path'] }}"
                               onchange="selectItem('{{ folder_data['full_path'] }}', this)">
                    </div>
                    {% endif %}
                </div>
                <div style="display: flex; align-items: center; gap: 10px;">
                    {% if folder_data["has_images"] %}
                    <a href="/gallery?path={{ folder_name }}" class="action-btn btn-gallery" title="Abrir galería">🖼️</a>
                    <a href="/gallery_slideshow?path={{ folder_name }}" class="action-btn btn-gallery" title="Vista deslizante">🎬</a>
                    <button class="action-btn btn-create-cbz" 
                            onclick="createCbzFromFolder('{{ folder_data['full_path'] }}', '{{ folder_name }}'); event.stopPropagation();" 
                            title="Crear CBZ">📚</button>
                    {% endif %}
                    {% if user_level >= 4 %}
                    <button class="action-btn btn-move" 
                            onclick="showMoveDialog(); event.stopPropagation();" 
                            title="Mover">➡️</button>
                    <button class="action-btn btn-compress" 
                            onclick="showCompressDialog(); event.stopPropagation();" 
                            title="Comprimir">📦</button>
                    <button class="action-btn btn-delete" 
                            onclick="deleteFolder('{{ folder_data['full_path'] }}', '{{ folder_name }}'); event.stopPropagation();" 
                            title="Borrar">🗑️</button>
                    {% endif %}
                    <span id="icon-{{ folder_name }}">▶</span>
                </div>
            </div>
            <div class="folder-content" id="content-{{ folder_name }}">
                {% for file in folder_data["items"] %}
                <div class="file-item">
                    <div class="file-info">
                        {% if user_level >= 4 %}
                        <div class="checkbox-item">
                            <input type="checkbox" 
                                   data-path="{{ file.full_path }}"
                                   onchange="selectItem('{{ file.full_path }}', this)">
                        </div>
                        {% endif %}
                        <span class="file-index">{{ file.index }}</span>
                        <span class="file-name">
                            <a href="/{{ file.rel_path }}">{{ file.name }}</a>
                        </span>
                        <span class="file-type">{{ file.ext.upper() }}</span>
                        <span class="file-size">({{ file.size_mb }} MB)</span>
                    </div>
                    <div class="file-actions">
                        <a href="/download?path={{ file.rel_path }}" class="action-btn btn-download" title="Descargar">📥</a>
                        {% if user_level >= 4 %}
                        <button class="action-btn btn-rename" 
                                onclick="showRenameInput('{{ file.full_path }}', '{{ file.name }}')" 
                                title="Renombrar">✏️</button>
                        <button class="action-btn btn-move" 
                                onclick="selectItem('{{ file.full_path }}', this.parentElement.parentElement.querySelector('input[type=\"checkbox\"]')); showMoveDialog();" 
                                title="Mover">➡️</button>
                        <button class="action-btn btn-compress" 
                                onclick="selectItem('{{ file.full_path }}', this.parentElement.parentElement.querySelector('input[type=\"checkbox\"]')); showCompressDialog();" 
                                title="Comprimir">📦</button>
                        <form action="/delete" method="POST" style="display: inline;">
                            <input type="hidden" name="path" value="{{ file.full_path }}">
                            <button type="submit" class="action-btn btn-delete" 
                                    onclick="return confirm('¿Eliminar {{ file.name }}?')" 
                                    title="Borrar">🗑️</button>
                        </form>
                        {% endif %}
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endfor %}
        
        {% if user_level >= 4 %}
        <div class="bulk-actions">
            <button class="bulk-btn btn-select-all" onclick="selectAllItems()">
                ☑️ Seleccionar Todos
            </button>
            <button class="bulk-btn btn-delete-empty" onclick="deleteEmptyFolders()">
                🗑️ Borrar Carpetas Vacías
            </button>
            <button class="bulk-btn btn-compress-selected" onclick="showCompressDialog()" disabled>
                📦 Comprimir Seleccionados
            </button>
            <button class="bulk-btn btn-merge-cbz" onclick="showMergeCbzDialog()">
                🔗 Combinar CBZ
            </button>
            <button class="bulk-btn btn-move-selected" onclick="showMoveDialog()" disabled>
                ➡️ Mover Seleccionados
            </button>
            <button class="bulk-btn btn-delete-selected" onclick="deleteSelected()" disabled>
                🗑️ Borrar Seleccionados
            </button>
        </div>
        {% endif %}
    </div>
    
    <div class="modal" id="moveModal">
        <div class="modal-content">
            <h3 class="modal-title">📂 Mover elementos</h3>
            <p>Selecciona la carpeta destino:</p>
            
            <div class="folder-selector" id="folderList">
            </div>
            
            <button onclick="toggleNewFolderInput()" style="margin-bottom: 15px;">
                📁 Nueva Carpeta
            </button>
            
            <div id="newFolderInput" style="display: none; margin-bottom: 15px;">
                <input type="text" id="newFolderName" placeholder="Nombre de la nueva carpeta">
            </div>
            
            <input type="hidden" id="selectedFolder">
            
            <div class="modal-actions">
                <button class="modal-btn btn-cancel" onclick="closeModal('moveModal')">
                    Cancelar
                </button>
                <button class="modal-btn btn-confirm" onclick="submitMove()">
                    Aceptar
                </button>
            </div>
        </div>
    </div>
    
    <div class="modal" id="compressModal">
        <div class="modal-content">
            <h3 class="modal-title">📦 Comprimir elementos</h3>
            <p>Nombre del archivo comprimido:</p>
            <input type="text" id="archiveName" placeholder="nombre_archivo" required>
            
            <div class="modal-actions">
                <button class="modal-btn btn-cancel" onclick="closeModal('compressModal')">
                    Cancelar
                </button>
                <button class="modal-btn btn-confirm" onclick="submitCompress()">
                    Confirmar
                </button>
            </div>
        </div>
    </div>
    
    <div class="modal" id="mergeCbzModal">
        <div class="modal-content">
            <h3 class="modal-title">🔗 Combinar CBZs</h3>
            <p>Selecciona y ordena los CBZs a combinar:</p>
            
            <div class="cbz-selector" id="cbzList">
            </div>
            
            <p>Nombre del CBZ combinado:</p>
            <input type="text" id="mergedCbzName" placeholder="manga_combinado.cbz" required>
            
            <div class="modal-actions">
                <button class="modal-btn btn-cancel" onclick="closeModal('mergeCbzModal')">
                    Cancelar
                </button>
                <button class="modal-btn btn-confirm" onclick="submitMergeCbz()">
                    Combinar
                </button>
            </div>
        </div>
    </div>
</body>
</html>
"""

MANGA_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Descargar Manga de MangaDex</title>
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
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }
        
        .header h1 {
            margin-bottom: 15px;
            font-size: 1.8em;
        }
        
        .nav {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }
        
        .nav a {
            background: rgba(255,255,255,0.2);
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 20px;
            transition: background 0.3s;
        }
        
        .nav a:hover {
            background: rgba(255,255,255,0.3);
        }
        
        .form-section {
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border: 2px dashed #dee2e6;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #333;
        }
        
        .url-input {
            width: 100%;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        .url-input:focus {
            border-color: #667eea;
            outline: none;
        }
        
        .url-input::placeholder {
            color: #aaa;
            font-style: italic;
        }
        
        .select-group {
            display: flex;
            gap: 30px;
            flex-wrap: wrap;
        }
        
        .select-box {
            flex: 1;
            min-width: 250px;
        }
        
        select {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            background: white;
            cursor: pointer;
            transition: border-color 0.3s;
        }
        
        select:focus {
            border-color: #667eea;
            outline: none;
        }
        
        .range-inputs {
            display: none;
            margin-top: 15px;
            padding: 15px;
            background: white;
            border-radius: 8px;
            border: 1px solid #dee2e6;
            flex-wrap: wrap;
            gap: 15px;
            align-items: center;
        }
        
        .range-inputs.active {
            display: flex;
        }
        
        .range-input {
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 14px;
            width: 120px;
        }
        
        .range-input:focus {
            border-color: #667eea;
            outline: none;
        }
        
        .download-btn {
            display: block;
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-top: 20px;
        }
        
        .download-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(40, 167, 69, 0.3);
        }
        
        .download-btn:disabled {
            background: #6c757d;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        
        .info-box {
            background: #e3f2fd;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #2196f3;
            margin-top: 20px;
            font-size: 14px;
            line-height: 1.5;
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .result-message {
            display: none;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
            text-align: center;
        }
        
        .success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        
        .error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        
        @media (max-width: 768px) {
            .select-group {
                flex-direction: column;
                gap: 20px;
            }
            
            .select-box {
                min-width: 100%;
            }
            
            .container {
                padding: 15px;
            }
            
            .header {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📖 Descargar Manga de MangaDex</h1>
            <div class="nav">
                <a href="/">🏠 Inicio</a>
                <a href="/manga">📖 Manga</a>
                <a href="/utils">🛠️ Utilidades</a>
                <a href="/downloads">📥 Descargas</a>
            </div>
        </div>
        
        <div class="form-section">
            <div class="form-group">
                <label for="mangaUrl">🔗 URL de MangaDex:</label>
                <input type="text" 
                       id="mangaUrl" 
                       class="url-input" 
                       placeholder="https://mangadex.org/title/... o https://mangadex.org/chapter/..."
                       value="">
            </div>
            
            <div class="select-group">
                <div class="select-box">
                    <label for="downloadRange">📊 Rango de Descarga:</label>
                    <select id="downloadRange" onchange="toggleRangeInputs()">
                        <option value="all">Todo el manga</option>
                        <option value="from-chapter">A partir de X Capítulo</option>
                        <option value="from-volume">A partir de X Volumen</option>
                        <option value="chapters-range">De X Capítulo a X Capítulo</option>
                        <option value="chapter-to-volume">De X Capítulo a X Volumen</option>
                        <option value="volumes-range">De X Volumen a X Volumen</option>
                        <option value="volume-to-chapter">De X Volumen a X Capítulo</option>
                        <option value="specific-chapter">Capítulo específico</option>
                        <option value="specific-volume">Volumen específico</option>
                    </select>
                    
                    <div id="rangeInputs" class="range-inputs">
                        <input type="number" id="startValue" class="range-input" placeholder="Inicio" min="1">
                        <span id="rangeText">a</span>
                        <input type="number" id="endValue" class="range-input" placeholder="Fin" min="1">
                    </div>
                </div>
                
                <div class="select-box">
                    <label for="saveFormat">💾 Formato de Guardado:</label>
                    <select id="saveFormat">
                        <option value="cbz-volume">Un Volumen como CBZ</option>
                        <option value="cbz">Cada capítulo como CBZ</option>
                        <option value="cbz-single">Todo en un CBZ</option>
                        <option value="pdf">Cada capítulo como PDF</option>
                        <option value="pdf-volume">Un volumen como PDF</option>
                        <option value="pdf-single">Todo en un PDF</option>
                        <option value="raw">Imágenes sueltas</option>
                        <option value="raw-volume">Imágenes por volumen</option>
                        <option value="raw-single">Todas las imágenes en una carpeta</option>
                        <option value="cb7">Cada capítulo como CB7</option>
                        <option value="cb7-volume">Un volumen como CB7</option>
                        <option value="cb7-single">Todo en un CB7</option>
                        <option value="epub">Cada capítulo como EPUB</option>
                        <option value="epub-volume">Un volumen como EPUB</option>
                        <option value="epub-single">Todo en un EPUB</option>
                    </select>
                </div>
            </div>
            
            <button id="downloadButton" class="download-btn" onclick="startDownload()">
                🚀 Iniciar Descarga
            </button>
            
            <div class="loading" id="loadingIndicator">
                <div class="spinner"></div>
                <p>Procesando descarga...</p>
                <p id="progressText">Esto puede tomar varios minutos</p>
            </div>
            
            <div class="result-message" id="resultMessage"></div>
        </div>
        
        <div class="info-box">
            <strong>💡 Información:</strong>
            <ul style="margin-top: 10px; padding-left: 20px;">
                <li>Las descargas se guardan en la carpeta <code>vault_files/Mangas/</code></li>
                <li>Para descargar todo el manga, selecciona "Todo el manga"</li>
                <li>Para un capítulo específico, usa la opción "Capítulo específico"</li>
                <li>Puedes ver el progreso en la página de <a href="/downloads">Descargas</a></li>
                <li>CBZ es un formato comprimido similar a ZIP, ideal para manga</li>
            </ul>
        </div>
    </div>

    <script>
        function toggleRangeInputs() {
            const rangeSelect = document.getElementById('downloadRange');
            const rangeInputs = document.getElementById('rangeInputs');
            const startValue = document.getElementById('startValue');
            const endValue = document.getElementById('endValue');
            const rangeText = document.getElementById('rangeText');
            
            rangeInputs.classList.remove('active');
            endValue.style.display = 'block';
            rangeText.style.display = 'inline';
            
            switch(rangeSelect.value) {
                case 'all':
                    break;
                    
                case 'from-chapter':
                    rangeInputs.classList.add('active');
                    rangeText.textContent = 'en adelante';
                    endValue.style.display = 'none';
                    rangeText.style.display = 'inline';
                    startValue.placeholder = 'Número de capítulo';
                    break;
                    
                case 'from-volume':
                    rangeInputs.classList.add('active');
                    rangeText.textContent = 'en adelante';
                    endValue.style.display = 'none';
                    rangeText.style.display = 'inline';
                    startValue.placeholder = 'Número de volumen';
                    break;
                    
                case 'chapters-range':
                    rangeInputs.classList.add('active');
                    rangeText.textContent = 'a';
                    startValue.placeholder = 'Capítulo inicio';
                    endValue.placeholder = 'Capítulo fin';
                    break;
                    
                case 'chapter-to-volume':
                    rangeInputs.classList.add('active');
                    rangeText.textContent = 'al volumen';
                    startValue.placeholder = 'Capítulo inicio';
                    endValue.placeholder = 'Volumen fin';
                    break;
                    
                case 'volumes-range':
                    rangeInputs.classList.add('active');
                    rangeText.textContent = 'a';
                    startValue.placeholder = 'Volumen inicio';
                    endValue.placeholder = 'Volumen fin';
                    break;
                    
                case 'volume-to-chapter':
                    rangeInputs.classList.add('active');
                    rangeText.textContent = 'al capítulo';
                    startValue.placeholder = 'Volumen inicio';
                    endValue.placeholder = 'Capítulo fin';
                    break;
                    
                case 'specific-chapter':
                    rangeInputs.classList.add('active');
                    rangeText.textContent = '(único)';
                    endValue.style.display = 'none';
                    startValue.placeholder = 'Número de capítulo';
                    break;
                    
                case 'specific-volume':
                    rangeInputs.classList.add('active');
                    rangeText.textContent = '(único)';
                    endValue.style.display = 'none';
                    startValue.placeholder = 'Número de volumen';
                    break;
            }
        }
        
        async function startDownload() {
            const url = document.getElementById('mangaUrl').value.trim();
            const rangeSelect = document.getElementById('downloadRange').value;
            const formatSelect = document.getElementById('saveFormat').value;
            const startValue = document.getElementById('startValue').value;
            const endValue = document.getElementById('endValue').value;
            
            if (!url) {
                showResult('Por favor, ingresa una URL de MangaDex', 'error');
                return;
            }
            
            if (!url.includes('mangadex.org')) {
                showResult('La URL debe ser de MangaDex (mangadex.org)', 'error');
                return;
            }
            
            const downloadBtn = document.getElementById('downloadButton');
            const loadingIndicator = document.getElementById('loadingIndicator');
            const progressText = document.getElementById('progressText');
            
            downloadBtn.disabled = true;
            downloadBtn.textContent = 'Procesando...';
            loadingIndicator.style.display = 'block';
            
            const formData = new FormData();
            formData.append('url', url);
            formData.append('range', rangeSelect);
            formData.append('format', formatSelect);
            formData.append('start', startValue);
            formData.append('end', endValue);
            
            try {
                const response = await fetch('/manga/download', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                if (result.success) {
                    showResult(`✅ ${result.message}<br><br>ID de descarga: ${result.download_id}<br><a href="/downloads">Ver progreso aquí</a>`, 'success');
                } else {
                    showResult(`❌ ${result.message}`, 'error');
                }
            } catch (error) {
                showResult(`❌ Error de conexión: ${error.message}`, 'error');
            } finally {
                downloadBtn.disabled = false;
                downloadBtn.textContent = '🚀 Iniciar Descarga';
                loadingIndicator.style.display = 'none';
            }
        }
        
        function showResult(message, type) {
            const resultDiv = document.getElementById('resultMessage');
            resultDiv.className = `result-message ${type}`;
            resultDiv.innerHTML = message;
            resultDiv.style.display = 'block';
            
            setTimeout(() => {
                resultDiv.style.display = 'none';
            }, 10000);
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            toggleRangeInputs();
        });
    </script>
</body>
</html>
"""

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
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body { 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background: #f5f5f5;
            min-height: 100vh;
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
            font-size: 1.5em; 
            margin-bottom: 10px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }
        
        .nav-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
            flex-wrap: wrap;
        }
        
        .nav-btn {
            background: rgba(255,255,255,0.2);
            padding: 10px 20px;
            border-radius: 20px;
            color: white;
            text-decoration: none;
            font-size: 1em;
            transition: background 0.3s, transform 0.2s;
            border: 1px solid rgba(255,255,255,0.3);
        }
        
        .nav-btn:hover {
            background: rgba(255,255,255,0.3);
            transform: translateY(-2px);
            text-decoration: none;
        }
        
        .content { 
            padding: 2em; 
            max-width: 800px;
            margin: 0 auto;
        }
        
        .section {
            background: white;
            padding: 2em;
            border-radius: 15px;
            margin-bottom: 2em;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border: 1px solid #e0e0e0;
        }
        
        h2 {
            color: #333;
            margin-top: 0;
            border-bottom: 3px solid #667eea;
            padding-bottom: 0.7em;
            margin-bottom: 1.2em;
            font-size: 1.8em;
        }
        
        h3 {
            color: #444;
            margin: 1.5em 0 1em 0;
            font-size: 1.4em;
        }
        
        form { 
            margin-bottom: 2em; 
            display: flex; 
            flex-direction: column; 
            gap: 1.2em; 
        }
        
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 0.5em;
        }
        
        label {
            font-weight: bold;
            color: #333;
            font-size: 1.1em;
            margin-bottom: 0.3em;
        }
        
        input[type="text"], 
        input[type="url"],
        select { 
            padding: 1em; 
            font-size: 1.1em; 
            border: 2px solid #ddd;
            border-radius: 8px;
            transition: border-color 0.3s, box-shadow 0.3s;
            width: 100%;
        }
        
        input[type="text"]:focus, 
        input[type="url"]:focus,
        select:focus {
            border-color: #667eea;
            outline: none;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
        }
        
        .checkbox-group {
            display: flex;
            align-items: center;
            gap: 0.8em;
            margin: 1em 0;
        }
        
        input[type="checkbox"] {
            width: 20px;
            height: 20px;
            cursor: pointer;
        }
        
        .checkbox-label {
            font-size: 1em;
            color: #555;
            cursor: pointer;
        }
        
        button { 
            padding: 1em 2em; 
            font-size: 1.1em; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            font-weight: bold;
            margin-top: 1em;
        }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        button:disabled {
            background: #6c757d;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        
        .info-text {
            background: #e3f2fd;
            padding: 1em;
            border-radius: 8px;
            border-left: 4px solid #2196f3;
            margin: 1.5em 0;
            font-size: 1em;
            line-height: 1.6;
        }
        
        .info-text strong {
            color: #0d47a1;
        }
        
        .file-input {
            padding: 1em;
            border: 2px dashed #667eea;
            border-radius: 8px;
            background: #f8f9fa;
            cursor: pointer;
            transition: background 0.3s;
            text-align: center;
            color: #555;
        }
        
        .file-input:hover {
            background: #e9ecef;
        }
        
        .error-message {
            background: #f8d7da;
            color: #721c24;
            padding: 1em;
            border-radius: 8px;
            border: 1px solid #f5c6cb;
            margin: 1em 0;
            display: none;
        }
        
        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 1em;
            border-radius: 8px;
            border: 1px solid #c3e6cb;
            margin: 1em 0;
            display: none;
        }
        
        .hidden {
            display: none;
        }
        
        @media (max-width: 768px) {
            .content {
                padding: 1em;
            }
            
            .section {
                padding: 1.5em;
            }
            
            .nav-buttons {
                flex-direction: column;
                align-items: center;
                gap: 10px;
            }
            
            .nav-btn {
                width: 90%;
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-title">
            🛠️ Utilidades - Servidor Flask de Neko Bot
        </div>
        <div class="nav-buttons">
            <a href="/" class="nav-btn">🏠 Inicio</a>
            <a href="/manga" class="nav-btn">📖 Manga</a>
            <a href="/utils" class="nav-btn">🛠️ Utilidades</a>
            <a href="/downloads" class="nav-btn">📥 Descargas</a>
        </div>
    </div>
    
    <div class="content">
        <div class="section">
            <h2>📤 Subir archivos al servidor</h2>
            
            <div class="error-message" id="uploadError"></div>
            <div class="success-message" id="uploadSuccess"></div>
            
            <form id="uploadForm">
                <div class="form-group">
                    <label for="destinationPath">Ruta de destino:</label>
                    <input type="text" 
                           id="destinationPath" 
                           name="destination_path" 
                           placeholder="Ingrese aquí la ruta destino, si se deja vacío quedará en el directorio base vault_files">
                </div>
                
                <div class="checkbox-group">
                    <input type="checkbox" id="useCustomName" name="use_custom_name">
                    <label for="useCustomName" class="checkbox-label">Nombre personalizado</label>
                </div>
                
                <div class="form-group hidden" id="customNameContainer">
                    <label for="customName">Nombre personalizado:</label>
                    <input type="text" 
                           id="customName" 
                           name="custom_name" 
                           placeholder="Ingrese acá el nombre personalizado del archivo">
                </div>
                
                <div class="form-group">
                    <label for="files">Seleccionar archivos:</label>
                    <input type="file" 
                           id="files" 
                           name="files" 
                           class="file-input" 
                           multiple 
                           required>
                </div>
                
                <button type="submit" id="uploadBtn">📤 Subir Archivos</button>
            </form>
            
            <div class="info-text">
                <strong>💡 Información:</strong>
                <ul style="margin-top: 10px; padding-left: 20px;">
                    <li>Puedes seleccionar múltiples archivos a la vez</li>
                    <li>Si no especificas ruta, los archivos se guardarán en <code>vault_files/</code></li>
                    <li>El nombre personalizado solo aplica cuando subes un solo archivo</li>
                    <li>Formatos soportados: cualquier tipo de archivo</li>
                </ul>
            </div>
        </div>
        
        <div class="section">
            <h2>📥 Descargar archivos al servidor</h2>
            
            <div class="error-message" id="downloadError"></div>
            <div class="success-message" id="downloadSuccess"></div>
            
            <form id="downloadForm">
                <div class="form-group">
                    <label for="downloadUrl">Enlace para descargar:</label>
                    <input type="url" 
                           id="downloadUrl" 
                           name="download_url" 
                           placeholder="https://ejemplo.com/archivo.zip"
                           required>
                </div>
                
                <div class="form-group">
                    <label for="downloadDestinationPath">Ruta de destino (opcional):</label>
                    <input type="text" 
                           id="downloadDestinationPath" 
                           name="destination_path" 
                           placeholder="Ingrese aquí la ruta destino, si se deja vacío quedará en el directorio base vault_files">
                </div>
                
                <div class="form-group">
                    <label for="downloadCustomName">Nombre personalizado (opcional):</label>
                    <input type="text" 
                           id="downloadCustomName" 
                           name="custom_name" 
                           placeholder="Nombre personalizado del archivo">
                </div>
                
                <button type="submit" id="downloadBtn">📥 Descargar Archivo</button>
            </form>
            
            <div class="info-text">
                <strong>💡 Información:</strong>
                <ul style="margin-top: 10px; padding-left: 20px;">
                    <li>Soporta cualquier tipo de archivo accesible por URL</li>
                    <li>Si no especificas nombre, se usará el nombre original del archivo</li>
                    <li>La descarga se realiza directamente al servidor</li>
                    <li>Puedes descargar imágenes, documentos, archivos comprimidos, etc.</li>
                </ul>
            </div>
        </div>

        <div class="section">
            <h2>🔗 Descargar desde Magnet Link</h2>
            <form action="/magnet" method="post">
                <div class="form-group">
                    <input type="text" name="magnet" placeholder="Magnet link o URL .torrent" required>
                </div>
                <button type="submit">🚀 Iniciar descarga Torrent</button>
            </form>
        </div>

        <div class="section">
            <h2>🔞 Descargar Doujin(s)</h2>
            <form action="/crear_cbz" method="post">
                <div class="form-group">
                    <input type="text" name="codigo" placeholder="Código(s) separados por coma (ej: 123,456,789)" required>
                </div>
                <div class="form-group">
                    <select name="tipo" required>
                        <option value="nh">NHentai</option>
                        <option value="h3">3Hentai</option>
                        <option value="hito">Hitomi.la</option>
                    </select>
                </div>
                <button type="submit">📚 Crear CBZ(s)</button>
            </form>
            <div class="info-text">
                💡 Puedes ingresar múltiples códigos separados por comas (ej: 123456,789012,345678).
                La descarga se procesará en segundo plano y podrás ver el progreso en la página de descargas.
            </div>
        </div>

        <div class="section">
            <h2>📥 Descargar desde MEGA</h2>
            <form action="/mega" method="post">
                <div class="form-group">
                    <input type="text" name="mega_link" placeholder="Enlace MEGA (https://mega.nz/...)" required>
                </div>
                <button type="submit">☁️ Iniciar descarga MEGA</button>
            </form>
            <div class="info-text">
                💡 Ingresa un enlace MEGA para descargar archivos. La descarga se procesará en segundo plano.
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const useCustomNameCheckbox = document.getElementById('useCustomName');
            const customNameContainer = document.getElementById('customNameContainer');
            
            useCustomNameCheckbox.addEventListener('change', function() {
                if (this.checked) {
                    customNameContainer.classList.remove('hidden');
                } else {
                    customNameContainer.classList.add('hidden');
                }
            });
            
            const uploadForm = document.getElementById('uploadForm');
            const uploadError = document.getElementById('uploadError');
            const uploadSuccess = document.getElementById('uploadSuccess');
            const uploadBtn = document.getElementById('uploadBtn');
            
            uploadForm.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const filesInput = document.getElementById('files');
                if (!filesInput.files || filesInput.files.length === 0) {
                    showMessage(uploadError, 'Seleccionar un archivo es obligatorio');
                    return;
                }
                
                uploadBtn.disabled = true;
                uploadBtn.textContent = 'Subiendo...';
                
                const formData = new FormData();
                formData.append('destination_path', document.getElementById('destinationPath').value);
                
                if (useCustomNameCheckbox.checked) {
                    formData.append('custom_name', document.getElementById('customName').value);
                }
                
                for (let i = 0; i < filesInput.files.length; i++) {
                    formData.append('files', filesInput.files[i]);
                }
                
                try {
                    const response = await fetch('/upload_file', {
                        method: 'POST',
                        body: formData
                    });
                    
                    const result = await response.json();
                    
                    if (result.success) {
                        showMessage(uploadSuccess, result.message);
                        uploadForm.reset();
                        customNameContainer.classList.add('hidden');
                        useCustomNameCheckbox.checked = false;
                    } else {
                        showMessage(uploadError, result.message);
                    }
                } catch (error) {
                    showMessage(uploadError, 'Error de conexión: ' + error.message);
                } finally {
                    uploadBtn.disabled = false;
                    uploadBtn.textContent = '📤 Subir Archivos';
                }
            });
            
            const downloadForm = document.getElementById('downloadForm');
            const downloadError = document.getElementById('downloadError');
            const downloadSuccess = document.getElementById('downloadSuccess');
            const downloadBtn = document.getElementById('downloadBtn');
            
            downloadForm.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const downloadUrl = document.getElementById('downloadUrl').value.trim();
                if (!downloadUrl) {
                    showMessage(downloadError, 'El enlace está vacío');
                    return;
                }
                
                downloadBtn.disabled = true;
                downloadBtn.textContent = 'Descargando...';
                
                const formData = new FormData();
                formData.append('download_url', downloadUrl);
                formData.append('destination_path', document.getElementById('downloadDestinationPath').value);
                formData.append('custom_name', document.getElementById('downloadCustomName').value);
                
                try {
                    const response = await fetch('/download_file', {
                        method: 'POST',
                        body: formData
                    });
                    
                    const result = await response.json();
                    
                    if (result.success) {
                        showMessage(downloadSuccess, result.message);
                        downloadForm.reset();
                    } else {
                        showMessage(downloadError, result.message);
                    }
                } catch (error) {
                    showMessage(downloadError, 'Error de conexión: ' + error.message);
                } finally {
                    downloadBtn.disabled = false;
                    downloadBtn.textContent = '📥 Descargar Archivo';
                }
            });
            
            function showMessage(element, message) {
                element.textContent = message;
                element.style.display = 'block';
                
                setTimeout(() => {
                    element.style.display = 'none';
                }, 5000);
            }
        });
    </script>
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
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body { 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container { 
            max-width: 1400px; 
            margin: 0 auto; 
            background: white; 
            padding: 25px; 
            border-radius: 15px; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            margin-top: 20px;
            margin-bottom: 20px;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5em;
            text-align: center;
            border-radius: 10px 10px 0 0;
            margin: -25px -25px 25px -25px;
            position: relative;
        }
        
        h1 { 
            color: white; 
            text-align: center; 
            margin: 0;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            font-size: 2.2em;
        }
        
        .nav { 
            margin-bottom: 25px; 
            text-align: center;
            padding: 15px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
        }
        
        .nav a { 
            margin: 0 15px; 
            text-decoration: none; 
            color: white;
            font-weight: bold;
            padding: 12px 25px;
            border-radius: 25px;
            background: rgba(255, 255, 255, 0.2);
            transition: background 0.3s, transform 0.2s;
            display: inline-block;
            font-size: 1.1em;
        }
        
        .nav a:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
            text-decoration: none;
        }
        
        .download-section {
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border: 2px dashed #dee2e6;
        }
        
        .download-section h2 {
            color: #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #667eea;
            font-size: 1.8em;
        }
        
        .download-cards {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .download-card { 
            border: 2px solid #e0e0e0; 
            padding: 25px; 
            border-radius: 12px; 
            background: white;
            transition: transform 0.3s, box-shadow 0.3s;
            position: relative;
        }
        
        .download-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }
        
        .download-card.completed { 
            border-color: #28a745;
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        }
        
        .download-card.error { 
            border-color: #dc3545;
            background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        }
        
        .download-card.processing { 
            border-color: #007bff;
            background: linear-gradient(135deg, #cce7ff 0%, #b3d9ff 100%);
        }
        
        .download-card h3 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.5em;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .delete-btn {
            background: #dc3545;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9em;
            transition: background 0.3s;
        }
        
        .delete-btn:hover {
            background: #c82333;
        }
        
        .progress-bar { 
            background: #e0e0e0; 
            height: 25px; 
            border-radius: 12px; 
            overflow: hidden; 
            margin: 20px 0; 
            position: relative;
        }
        
        .progress-fill { 
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            height: 100%; 
            transition: width 0.5s ease-out; 
            position: relative;
        }
        
        .progress-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-weight: bold;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
            font-size: 0.9em;
        }
        
        .stats { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); 
            gap: 15px; 
            margin: 20px 0;
        }
        
        .stat-item { 
            padding: 12px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
            border-left: 4px solid #667eea;
            text-align: center;
        }
        
        .stat-item strong {
            display: block;
            color: #333;
            margin-bottom: 5px;
            font-size: 0.9em;
        }
        
        .stat-item span {
            color: #666;
            font-size: 1.1em;
            font-weight: 600;
        }
        
        .controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 30px 0;
            padding: 20px;
            background: #e9ecef;
            border-radius: 10px;
            flex-wrap: wrap;
            gap: 15px;
        }
        
        .refresh-btn { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            border: none; 
            padding: 12px 30px; 
            border-radius: 8px; 
            cursor: pointer;
            transition: transform 0.2s;
            font-size: 1.1em;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .refresh-btn:hover {
            transform: translateY(-2px);
        }
        
        .bulk-actions {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .bulk-btn {
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1em;
            transition: transform 0.2s;
        }
        
        .bulk-btn.delete-all {
            background: #dc3545;
            color: white;
        }
        
        .bulk-btn.delete-all:hover {
            background: #c82333;
            transform: translateY(-2px);
        }
        
        .bulk-btn.delete-completed {
            background: #ffc107;
            color: black;
        }
        
        .bulk-btn.delete-completed:hover {
            background: #e0a800;
            transform: translateY(-2px);
        }
        
        .auto-refresh { 
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 12px 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .auto-refresh input[type="checkbox"] {
            width: 20px;
            height: 20px;
            cursor: pointer;
        }
        
        .auto-refresh label {
            color: #333;
            font-weight: 500;
            cursor: pointer;
        }
        
        .message-box {
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
            font-size: 0.95em;
            line-height: 1.5;
        }
        
        .error-box {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        
        .info-box {
            background: #d1ecf1;
            color: #0c5460;
            border: 1px solid #bee5eb;
        }
        
        .current-item {
            font-style: italic;
            color: #6c757d;
            margin: 10px 0;
            padding: 8px 12px;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 6px;
            border-left: 3px solid #17a2b8;
        }
        
        .no-downloads {
            text-align: center;
            padding: 60px 40px;
            color: #6c757d;
            font-size: 1.2em;
        }
        
        .no-downloads h3 {
            margin-bottom: 20px;
            font-size: 1.8em;
            color: #495057;
        }
        
        .no-downloads p {
            max-width: 600px;
            margin: 0 auto 30px auto;
            line-height: 1.6;
        }
        
        .manga-progress {
            font-size: 1.2em;
            font-weight: bold;
            margin: 15px 0;
            color: #495057;
            padding: 10px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 6px;
            text-align: center;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 15px;
                margin: 10px;
            }
            
            .download-cards {
                grid-template-columns: 1fr;
            }
            
            .controls {
                flex-direction: column;
                align-items: stretch;
            }
            
            .bulk-actions {
                justify-content: center;
            }
            
            .nav a {
                margin: 5px;
                display: block;
                width: calc(100% - 10px);
                box-sizing: border-box;
            }
            
            .stats {
                grid-template-columns: 1fr;
            }
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
            <a href="/manga">📖 Manga</a>
            <a href="/utils">🛠️ Utilidades</a>
            <a href="/downloads">📥 Descargas</a>
        </div>

        <div class="controls">
            <button class="refresh-btn" onclick="location.reload()">
                🔄 Actualizar
            </button>
            
            <div class="bulk-actions">
                <button class="bulk-btn delete-completed" onclick="deleteAllCompleted()">
                    🗑️ Eliminar Completadas
                </button>
                <button class="bulk-btn delete-all" onclick="deleteAllDownloads()">
                    🗑️ Eliminar Todas
                </button>
            </div>
            
            <div class="auto-refresh">
                <input type="checkbox" id="autoRefresh" onchange="toggleAutoRefresh()">
                <label for="autoRefresh">Actualizar automáticamente cada 5 segundos</label>
            </div>
        </div>
        
        {% if manga_downloads %}
        <div class="download-section">
            <h2>📖 Descargas de Manga</h2>
            <div class="download-cards">
                {% for id, download in manga_downloads.items() %}
                <div class="download-card {{ download.state }}">
                    <h3>
                        📖 Manga Download
                        {% if download.state in ["completed", "error"] %}
                        <button class="delete-btn" onclick="deleteDownload('{{ id }}', 'manga')">×</button>
                        {% endif %}
                    </h3>
                    
                    <p><strong>URL:</strong> {{ download.url[:50] }}...</p>
                    
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {{ download.progress }}%">
                            <div class="progress-text">{{ download.progress }}%</div>
                        </div>
                    </div>
                    
                    <div class="stats">
                        <div class="stat-item">
                            <strong>Estado:</strong>
                            <span style="color: 
                                {% if download.state == 'completed' %}#28a745
                                {% elif download.state == 'error' %}#dc3545
                                {% else %}#007bff{% endif %};">
                                {{ download.state }}
                            </span>
                        </div>
                        <div class="stat-item">
                            <strong>Formato:</strong>
                            <span>{{ download.format }}</span>
                        </div>
                        <div class="stat-item">
                            <strong>Rango:</strong>
                            <span>{{ download.range }}</span>
                        </div>
                        <div class="stat-item">
                            <strong>Iniciado:</strong>
                            <span>{{ download.start_time[:19] }}</span>
                        </div>
                        {% if download.end_time %}
                        <div class="stat-item">
                            <strong>Finalizado:</strong>
                            <span>{{ download.end_time[:19] }}</span>
                        </div>
                        {% endif %}
                    </div>
                    
                    {% if download.message %}
                    <div class="current-item">{{ download.message }}</div>
                    {% endif %}
                    
                    {% if download.error %}
                    <div class="message-box error-box">
                        <strong>❌ Error:</strong> {{ download.error }}
                    </div>
                    {% endif %}
                    
                    {% if download.output %}
                    <div class="message-box info-box">
                        <strong>📋 Salida:</strong><br>
                        <small>{{ download.output[-200:] if download.output|length > 200 else download.output }}</small>
                    </div>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
        
        {% if mega_downloads %}
        <div class="download-section">
            <h2>📦 Descargas MEGA</h2>
            <div class="download-cards">
                {% for id, download in mega_downloads.items() %}
                <div class="download-card {{ download.state }}">
                    <h3>
                        📥 Descarga MEGA
                        {% if download.state in ["completed", "error"] %}
                        <button class="delete-btn" onclick="deleteDownload('{{ id }}', 'mega')">×</button>
                        {% endif %}
                    </h3>
                    
                    <p><strong>Enlace:</strong> {{ download.link[:50] }}...</p>
                    
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {{ download.progress }}%">
                            <div class="progress-text">{{ download.progress }}%</div>
                        </div>
                    </div>
                    
                    <div class="stats">
                        <div class="stat-item">
                            <strong>Estado:</strong>
                            <span>{{ download.state }}</span>
                        </div>
                        <div class="stat-item">
                            <strong>Progreso:</strong>
                            <span>{{ download.progress }}%</span>
                        </div>
                        <div class="stat-item">
                            <strong>Iniciado:</strong>
                            <span>{{ download.start_time[:19] }}</span>
                        </div>
                        {% if download.end_time %}
                        <div class="stat-item">
                            <strong>Finalizado:</strong>
                            <span>{{ download.end_time[:19] }}</span>
                        </div>
                        {% endif %}
                        {% if download.output_dir %}
                        <div class="stat-item">
                            <strong>Directorio:</strong>
                            <span>{{ download.output_dir|basename }}</span>
                        </div>
                        {% endif %}
                    </div>
                    
                    {% if download.message %}
                    <div class="current-item">{{ download.message }}</div>
                    {% endif %}
                    
                    {% if download.error %}
                    <div class="message-box error-box">
                        <strong>❌ Error:</strong> {{ download.error }}
                    </div>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
        
        {% if doujin_downloads %}
        <div class="download-section">
            <h2>📚 Descargas de Doujins</h2>
            <div class="download-cards">
                {% for id, download in doujin_downloads.items() %}
                <div class="download-card {{ download.state }}">
                    <h3>
                        📖 CBZ{{ 's' if download.total > 1 else '' }} ({{ download.tipo|upper }})
                        {% if download.state in ["completed", "error"] %}
                        <button class="delete-btn" onclick="deleteDownload('{{ id }}', 'doujin')">×</button>
                        {% endif %}
                    </h3>
                    
                    <div class="manga-progress">
                        Progreso: {{ download.progress }} de {{ download.total }} CBZ{{ 's' if download.total > 1 else '' }}
                    </div>
                    
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {{ (download.progress / download.total * 100) | round(1) }}%">
                            <div class="progress-text">{{ (download.progress / download.total * 100) | round(1) }}%</div>
                        </div>
                    </div>
                    
                    <div class="stats">
                        <div class="stat-item">
                            <strong>✅ Completados:</strong>
                            <span>{{ download.completados }}</span>
                        </div>
                        <div class="stat-item">
                            <strong>❌ Errores:</strong>
                            <span>{{ download.errores }}</span>
                        </div>
                        <div class="stat-item">
                            <strong>📊 Total:</strong>
                            <span>{{ download.total }}</span>
                        </div>
                        <div class="stat-item">
                            <strong>Iniciado:</strong>
                            <span>{{ download.start_time[:19] }}</span>
                        </div>
                        {% if download.end_time %}
                        <div class="stat-item">
                            <strong>Finalizado:</strong>
                            <span>{{ download.end_time[:19] }}</span>
                        </div>
                        {% endif %}
                    </div>
                    
                    {% if download.state == 'processing' %}
                    <div class="current-item">{{ download.current_item }}</div>
                    {% endif %}
                    
                    {% if download.state == 'completed' and download.resultados %}
                    <div class="message-box info-box">
                        <strong>📋 Resultados:</strong><br>
                        {% for resultado in download.resultados[:3] %}
                        <small>{{ resultado.codigo }}: 
                            <span style="color: {% if resultado.estado == 'completado' %}#28a745{% else %}#dc3545{% endif %};">
                                {{ resultado.estado }}
                            </span>
                            {% if resultado.error %} - {{ resultado.error }}{% endif %}
                        </small><br>
                        {% endfor %}
                        {% if download.resultados|length > 3 %}
                        <small>... y {{ download.resultados|length - 3 }} más</small>
                        {% endif %}
                    </div>
                    {% endif %}
                    
                    {% if download.error %}
                    <div class="message-box error-box">
                        <strong>❌ Error:</strong> {{ download.error }}
                    </div>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
        
        {% if downloads %}
        <div class="download-section">
            <h2>📦 Descargas Torrent</h2>
            <div class="download-cards">
                {% for id, download in downloads.items() %}
                <div class="download-card {{ download.state }}">
                    <h3>
                        {{ download.filename }}
                        {% if download.state in ["completed", "error"] %}
                        <button class="delete-btn" onclick="deleteDownload('{{ id }}', 'torrent')">×</button>
                        {% endif %}
                    </h3>
                    
                    <p><strong>Enlace:</strong> {{ download.link[:50] }}...</p>
                    
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {{ download.percent }}%">
                            <div class="progress-text">{{ download.percent }}%</div>
                        </div>
                    </div>
                    
                    <div class="stats">
                        <div class="stat-item">
                            <strong>Estado:</strong>
                            <span>{{ download.state }}</span>
                        </div>
                        <div class="stat-item">
                            <strong>Descargado:</strong>
                            <span>{{ (download.downloaded / (1024*1024)) | round(2) }} MB</span>
                        </div>
                        <div class="stat-item">
                            <strong>Total:</strong>
                            <span>{{ (download.total_size / (1024*1024)) | round(2) if download.total_size > 0 else 'Calculando...' }} MB</span>
                        </div>
                        <div class="stat-item">
                            <strong>Velocidad:</strong>
                            <span>{{ (download.speed / (1024*1024)) | round(2) }} MB/s</span>
                        </div>
                        <div class="stat-item">
                            <strong>Iniciado:</strong>
                            <span>{{ download.start_time[:19] }}</span>
                        </div>
                        {% if download.end_time %}
                        <div class="stat-item">
                            <strong>Completado:</strong>
                            <span>{{ download.end_time[:19] }}</span>
                        </div>
                        {% endif %}
                    </div>
                    
                    {% if download.error %}
                    <div class="message-box error-box">
                        <strong>❌ Error:</strong> {{ download.error }}
                    </div>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if not downloads and not doujin_downloads and not mega_downloads and not manga_downloads %}
        <div class="no-downloads">
            <h3>📭 No hay descargas activas</h3>
            <p>Inicia una nueva descarga desde la página de Utilidades</p>
            <p>Las descargas de manga, torrents, MEGA y doujins aparecerán aquí</p>
            <a href="/utils" class="refresh-btn" style="display: inline-block; margin-top: 20px;">
                🛠️ Ir a Utilidades
            </a>
        </div>
        {% endif %}
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
        
        async function deleteDownload(downloadId, downloadType) {
            if (!confirm('¿Eliminar esta descarga?')) {
                return;
            }
            
            try {
                const response = await fetch('/api/downloads/delete', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        download_id: downloadId,
                        type: downloadType
                    })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert(result.message);
                    location.reload();
                } else {
                    alert('Error: ' + result.message);
                }
            } catch (error) {
                alert('Error de conexión: ' + error.message);
            }
        }
        
        async function deleteAllCompleted() {
            if (!confirm('¿Eliminar todas las descargas completadas?')) {
                return;
            }
            
            try {
                const response = await fetch('/api/downloads/delete-all', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        type: 'all'
                    })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert(result.message);
                    location.reload();
                } else {
                    alert('Error: ' + result.message);
                }
            } catch (error) {
                alert('Error de conexión: ' + error.message);
            }
        }
        
        async function deleteAllDownloads() {
            if (!confirm('¿Eliminar TODAS las descargas (incluyendo las activas)?')) {
                return;
            }
            
            try {
                const response = await fetch('/api/downloads/delete-all', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        type: 'all'
                    })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert(result.message);
                    location.reload();
                } else {
                    alert('Error: ' + result.message);
                }
            } catch (error) {
                alert('Error de conexión: ' + error.message);
            }
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            const cards = document.querySelectorAll('.download-card');
            cards.forEach(card => {
                const progressBar = card.querySelector('.progress-bar');
                if (progressBar) {
                    const progressFill = progressBar.querySelector('.progress-fill');
                    const progressText = progressBar.querySelector('.progress-text');
                    if (progressFill && progressText) {
                        const width = progressFill.style.width;
                        progressText.textContent = width;
                    }
                }
            });
        });
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
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body { 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background-color: #1a1a1a;
            color: white;
        }
        
        .header { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            padding: 1em; 
            text-align: center; 
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        
        .header a { 
            color: white; 
            text-decoration: none;
            font-weight: bold;
            margin: 0 10px;
            padding: 8px 15px;
            border-radius: 20px;
            background: rgba(255,255,255,0.2);
            transition: all 0.3s ease;
            display: inline-block;
        }
        
        .header a:hover { 
            background: rgba(255,255,255,0.3);
            transform: translateY(-2px);
            text-decoration: none;
        }
        
        .view-selector {
            text-align: center;
            padding: 15px;
            background: rgba(0,0,0,0.2);
            margin-bottom: 10px;
        }
        
        .view-btn {
            padding: 10px 20px;
            margin: 0 5px;
            background: rgba(255,255,255,0.1);
            color: white;
            border: 2px solid rgba(255,255,255,0.3);
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
        }
        
        .view-btn:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }
        
        .view-btn.active {
            background: #667eea;
            border-color: #667eea;
        }
        
        .gallery-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 15px;
            padding: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            background: #2a2a2a;
            aspect-ratio: 2/3;
        }
        
        .gallery-item:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }
        
        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.5s ease;
        }
        
        .gallery-item:hover img {
            transform: scale(1.1);
        }
        
        .gallery-caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(transparent, rgba(0,0,0,0.8));
            padding: 15px 10px 10px;
            font-size: 14px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            text-align: center;
        }
        
        .image-counter {
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: bold;
        }
        
        .slideshow-container {
            display: none;
            position: relative;
            max-width: 100vw;
            min-height: 100vh;
            background: #000;
        }
        
        .slideshow-image {
            width: 100%;
            height: 100vh;
            object-fit: contain;
            display: block;
        }
        
        .slideshow-info {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 14px;
            z-index: 101;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .progress-bar {
            width: 200px;
            height: 4px;
            background: rgba(255,255,255,0.2);
            border-radius: 2px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: #667eea;
            transition: width 0.3s ease;
        }
        
        .nav-buttons {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 20px;
            z-index: 101;
        }
        
        .nav-btn {
            background: rgba(0,0,0,0.7);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .nav-btn:hover {
            background: rgba(102, 126, 234, 0.8);
            transform: translateY(-2px);
        }
        
        .close-btn {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0,0,0,0.7);
            color: white;
            border: none;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 20px;
            z-index: 101;
            transition: all 0.3s ease;
        }
        
        .close-btn:hover {
            background: rgba(220, 53, 69, 0.8);
            transform: rotate(90deg);
        }
        
        .fullscreen-view {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.95);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }
        
        .fullscreen-img {
            max-width: 95%;
            max-height: 95%;
            object-fit: contain;
        }
        
        .image-nav {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(0,0,0,0.5);
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 20px;
            transition: all 0.3s ease;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .image-nav:hover {
            background: rgba(102, 126, 234, 0.8);
        }
        
        .image-nav.prev {
            left: 20px;
        }
        
        .image-nav.next {
            right: 20px;
        }
        
        @media (max-width: 768px) {
            .gallery-container {
                grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
                gap: 10px;
                padding: 10px;
            }
            
            .header a {
                margin: 5px;
                padding: 6px 12px;
                font-size: 14px;
            }
            
            .nav-buttons {
                bottom: 20px;
                gap: 10px;
            }
            
            .nav-btn {
                padding: 10px 20px;
                font-size: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <a href="/">🏠 Inicio</a>
        <a href="/manga">📖 Manga</a>
        <a href="/utils">🛠️ Utilidades</a>
        <a href="/downloads">📥 Descargas</a>
        <a href="/browse?path={{ current_path }}">📂 Volver al explorador</a>
    </div>

    <div class="view-selector">
        <button class="view-btn active" onclick="showGridView()">🖼️ Vista Cuadrícula</button>
        <button class="view-btn" onclick="showSlideshowView()">🎬 Vista Deslizante</button>
    </div>

    <div class="gallery-container" id="gridView">
        {% for image in image_files %}
        <div class="gallery-item" onclick="openFullscreen('{{ image.url_path }}', {{ loop.index0 }})">
            <div class="image-counter">{{ loop.index }}/{{ image_files|length }}</div>
            <img src="{{ image.url_path }}" 
                 alt="{{ image.name }}" 
                 loading="lazy"
                 onerror="this.src='https://via.placeholder.com/250x375/333/666?text=Error'">
            <div class="gallery-caption">{{ image.name }}</div>
        </div>
        {% endfor %}
    </div>

    <div class="slideshow-container" id="slideshowView">
        <div class="slideshow-info">
            <span id="currentSlide">1</span>/<span id="totalSlides">{{ image_files|length }}</span>
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill" style="width: 0%"></div>
            </div>
        </div>
        
        <button class="close-btn" onclick="hideSlideshow()">✕</button>
        
        <div class="nav-buttons">
            <button class="nav-btn" onclick="prevSlide()">
                ◀ Anterior
            </button>
            <button class="nav-btn" onclick="toggleAutoSlide()" id="autoSlideBtn">
                ⏸️ Pausar
            </button>
            <button class="nav-btn" onclick="nextSlide()">
                Siguiente ▶
            </button>
        </div>
        
        {% for image in image_files %}
        <img src="{{ image.url_path }}" 
             alt="{{ image.name }}"
             class="slideshow-image"
             style="display: none;"
             data-index="{{ loop.index0 }}"
             onerror="this.src='https://via.placeholder.com/1920x1080/333/666?text=Error'">
        {% endfor %}
    </div>

    <div class="fullscreen-view" id="fullscreenView" onclick="closeFullscreen()">
        <button class="close-btn" onclick="closeFullscreen()">✕</button>
        <button class="image-nav prev" onclick="navigateFullscreen(-1); event.stopPropagation()">◀</button>
        <img class="fullscreen-img" id="fullscreenImg" src="" onclick="event.stopPropagation()">
        <button class="image-nav next" onclick="navigateFullscreen(1); event.stopPropagation()">▶</button>
        <div class="slideshow-info" style="top: auto; bottom: 20px;">
            <span id="fullscreenCurrent">1</span>/<span id="fullscreenTotal">{{ image_files|length }}</span>
        </div>
    </div>

    <script>
        const imageFiles = {{ image_files|tojson }};
        let currentSlideIndex = 0;
        let autoSlideInterval;
        let isAutoSliding = true;
        let fullscreenIndex = 0;
        
        function showGridView() {
            document.getElementById('gridView').style.display = 'grid';
            document.getElementById('slideshowView').style.display = 'none';
            document.querySelectorAll('.view-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.view-btn')[0].classList.add('active');
            stopAutoSlide();
        }
        
        function showSlideshowView() {
            document.getElementById('gridView').style.display = 'none';
            document.getElementById('slideshowView').style.display = 'block';
            document.querySelectorAll('.view-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.view-btn')[1].classList.add('active');
            showSlide(0);
            startAutoSlide();
        }
        
        function hideSlideshow() {
            showGridView();
        }
        
        function showSlide(index) {
            if (index < 0) index = imageFiles.length - 1;
            if (index >= imageFiles.length) index = 0;
            
            currentSlideIndex = index;
            
            document.querySelectorAll('.slideshow-image').forEach(img => img.style.display = 'none');
            document.querySelectorAll(`.slideshow-image[data-index="${index}"]`).forEach(img => {
                img.style.display = 'block';
            });
            
            document.getElementById('currentSlide').textContent = index + 1;
            document.getElementById('totalSlides').textContent = imageFiles.length;
            
            const progress = ((index + 1) / imageFiles.length) * 100;
            document.getElementById('progressFill').style.width = progress + '%';
        }
        
        function prevSlide() {
            showSlide(currentSlideIndex - 1);
            resetAutoSlide();
        }
        
        function nextSlide() {
            showSlide(currentSlideIndex + 1);
            resetAutoSlide();
        }
        
        function startAutoSlide() {
            if (autoSlideInterval) clearInterval(autoSlideInterval);
            isAutoSliding = true;
            document.getElementById('autoSlideBtn').innerHTML = '⏸️ Pausar';
            autoSlideInterval = setInterval(nextSlide, 3000);
        }
        
        function stopAutoSlide() {
            if (autoSlideInterval) clearInterval(autoSlideInterval);
            isAutoSliding = false;
            document.getElementById('autoSlideBtn').innerHTML = '▶️ Reanudar';
        }
        
        function toggleAutoSlide() {
            if (isAutoSliding) {
                stopAutoSlide();
            } else {
                startAutoSlide();
            }
        }
        
        function resetAutoSlide() {
            if (isAutoSliding) {
                clearInterval(autoSlideInterval);
                autoSlideInterval = setInterval(nextSlide, 3000);
            }
        }
        
        function openFullscreen(src, index) {
            fullscreenIndex = index;
            const fullscreenView = document.getElementById('fullscreenView');
            const fullscreenImg = document.getElementById('fullscreenImg');
            
            fullscreenImg.src = src;
            document.getElementById('fullscreenCurrent').textContent = index + 1;
            document.getElementById('fullscreenTotal').textContent = imageFiles.length;
            
            fullscreenView.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }
        
        function closeFullscreen() {
            document.getElementById('fullscreenView').style.display = 'none';
            document.body.style.overflow = 'auto';
        }
        
        function navigateFullscreen(direction) {
            fullscreenIndex += direction;
            if (fullscreenIndex < 0) fullscreenIndex = imageFiles.length - 1;
            if (fullscreenIndex >= imageFiles.length) fullscreenIndex = 0;
            
            openFullscreen(imageFiles[fullscreenIndex].url_path, fullscreenIndex);
        }
        
        document.addEventListener('keydown', function(e) {
            if (document.getElementById('fullscreenView').style.display === 'flex') {
                if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
                    navigateFullscreen(-1);
                } else if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
                    navigateFullscreen(1);
                } else if (e.key === 'Escape') {
                    closeFullscreen();
                }
            }
            
            if (document.getElementById('slideshowView').style.display === 'block') {
                if (e.key === 'ArrowLeft') {
                    prevSlide();
                } else if (e.key === 'ArrowRight' || e.key === ' ') {
                    nextSlide();
                } else if (e.key === 'Escape') {
                    hideSlideshow();
                }
            }
        });
        
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('slideshowView').addEventListener('wheel', function(e) {
                e.preventDefault();
                if (e.deltaY < 0) {
                    prevSlide();
                } else {
                    nextSlide();
                }
            }, { passive: false });
            
            document.getElementById('slideshowView').addEventListener('click', function(e) {
                if (e.clientX < window.innerWidth / 2) {
                    prevSlide();
                } else {
                    nextSlide();
                }
            });
            
            document.getElementById('fullscreenView').addEventListener('wheel', function(e) {
                e.preventDefault();
                if (e.deltaY < 0) {
                    navigateFullscreen(-1);
                } else {
                    navigateFullscreen(1);
                }
            }, { passive: false });
        });
        
        function preloadImages() {
            imageFiles.forEach((image, index) => {
                if (index < 5) {
                    const img = new Image();
                    img.src = image.url_path;
                }
            });
        }
        
        document.addEventListener('DOMContentLoaded', preloadImages);
    </script>
</body>
</html>
"""

SEARCH_NH_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Búsqueda nHentai</title>
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
        }
        
        .search-form {
            background: white;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .search-form input {
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            margin: 5px;
            min-width: 200px;
        }
        
        .search-form button {
            padding: 12px 24px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            margin: 5px;
        }
        
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            padding: 20px 0;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        @media (min-width: 768px) {
            .gallery-grid {
                grid-template-columns: repeat(5, 1fr);
                gap: 20px;
            }
        }
        
        .gallery-item {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        
        .gallery-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        
        .image-container {
            position: relative;
            width: 100%;
            padding-bottom: 140%;
            overflow: hidden;
        }
        
        .gallery-item img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .gallery-item:hover img {
            transform: scale(1.05);
        }
        
        .gallery-info {
            padding: 15px;
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        .gallery-name {
            font-weight: 600;
            color: #333;
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            flex: 1;
            min-height: 60px;
        }
        
        .gallery-code {
            color: #666;
            font-size: 14px;
            font-weight: 500;
        }
        
        .gallery-actions {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-top: 10px;
        }
        
        .details-link {
            background: #28a745;
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 12px;
            text-align: center;
            transition: background 0.3s;
        }
        
        .details-link:hover {
            background: #218838;
            text-decoration: none;
        }
        
        .convert-btn {
            background: #ffc107;
            color: black;
            border: none;
            padding: 8px 12px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 12px;
            transition: background 0.3s;
        }
        
        .convert-btn:hover {
            background: #e0a800;
        }
        
        .convert-btn:disabled {
            background: #6c757d;
            cursor: not-allowed;
        }
        
        .pagination {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            padding: 30px 0;
            flex-wrap: wrap;
        }
        
        .pagination a {
            padding: 10px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: transform 0.2s;
        }
        
        .pagination a:hover {
            transform: translateY(-2px);
            text-decoration: none;
        }
        
        .pagination span {
            font-weight: 600;
            color: #333;
            font-size: 16px;
        }
        
        .convert-all-btn {
            background: #17a2b8;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            margin: 10px;
            transition: background 0.3s;
        }
        
        .convert-all-btn:hover {
            background: #138496;
        }
        
        .convert-all-btn:disabled {
            background: #6c757d;
            cursor: not-allowed;
        }
        
        .loading {
            opacity: 0.6;
            pointer-events: none;
        }
        
        .total-results {
            text-align: center;
            color: #666;
            margin-bottom: 20px;
            font-size: 14px;
        }
        
        .no-results {
            text-align: center;
            padding: 60px 20px;
            color: #666;
        }
        
        .no-results h3 {
            margin-bottom: 10px;
            font-size: 20px;
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
    <div class="total-results">
        <strong>{{ total_results }}</strong> resultados encontrados - Página {{ current_page }} de {{ total_pages }}
    </div>
    
    <div class="gallery-grid">
        {% for result in results %}
        <div class="gallery-item" id="gallery-{{ result.code }}">
            <div class="image-container">
                {% if result.image_links %}
                <img src="{{ result.image_links[0] }}" 
                     alt="{{ result.name }}" 
                     id="img-{{ result.code }}"
                     data-original-src="{{ result.image_links[0] }}"
                     onerror="this.src='https://via.placeholder.com/300x420/667eea/ffffff?text=Imagen+no+disponible'">
                {% else %}
                <img src="https://via.placeholder.com/300x420/cccccc/ffffff?text=Sin+imagen" 
                     alt="Sin imagen" 
                     id="img-{{ result.code }}" 
                     data-original-src="">
                {% endif %}
            </div>
            
            <div class="gallery-info">
                <div class="gallery-code">Código: {{ result.code }}</div>
                <div class="gallery-name">{{ result.name }}</div>
                
                <div class="gallery-actions">
                    <a href="/api/vnh/{{ result.code }}" class="details-link" target="_blank">
                        Ver Detalles
                    </a>
                    <button class="convert-btn" onclick="convertToBase64('{{ result.code }}')">
                        Convertir a Base64
                    </button>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    
    <div class="pagination">
        {% if current_page > 1 %}
        <a href="/api/snh/{{ search_term }}?p={{ current_page - 1 }}">‹ Página Anterior</a>
        {% endif %}
        
        <span>Página {{ current_page }} de {{ total_pages }}</span>
        
        {% if current_page < total_pages %}
        <a href="/api/snh/{{ search_term }}?p={{ current_page + 1 }}">Página Siguiente ›</a>
        {% endif %}
    </div>
    
    {% else %}
    <div class="no-results">
        <h3>No se encontraron resultados para "{{ search_term }}"</h3>
        <p>Intenta con otros términos de búsqueda</p>
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
                if (!response.ok) throw new Error('Error en la respuesta');
                
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
            const convertButtons = document.querySelectorAll('.convert-btn:not(:disabled)');
            const convertAllBtn = document.querySelector('.convert-all-btn');
            
            if (convertButtons.length === 0) return;
            
            convertAllBtn.disabled = true;
            convertAllBtn.textContent = 'Convirtiendo todas...';
            
            for (let i = 0; i < convertButtons.length; i++) {
                const btn = convertButtons[i];
                const galleryElement = btn.closest('.gallery-item');
                const code = galleryElement.id.replace('gallery-', '');
                const imgElement = document.getElementById(`img-${code}`);
                const originalSrc = imgElement.dataset.originalSrc;
                
                if (originalSrc && !originalSrc.includes('base64') && !originalSrc.includes('via.placeholder.com')) {
                    const event = new MouseEvent('click', {
                        view: window,
                        bubbles: true,
                        cancelable: true
                    });
                    btn.dispatchEvent(event);
                    
                    await new Promise(resolve => setTimeout(resolve, 1500));
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
                        this.src = 'https://via.placeholder.com/300x420/dc3545/ffffff?text=Error+cargando';
                    }
                });
            });
        });

        function preloadVisibleImages() {
            const images = document.querySelectorAll('img[data-original-src]');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.loaded !== 'true') {
                            img.src = img.dataset.originalSrc;
                            img.dataset.loaded = 'true';
                        }
                        observer.unobserve(img);
                    }
                });
            }, { rootMargin: '50px' });

            images.forEach(img => observer.observe(img));
        }

        document.addEventListener('DOMContentLoaded', preloadVisibleImages);
    </script>
</body>
</html>
'''

SEARCH_3H_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Búsqueda 3Hentai</title>
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
        }
        
        .search-form {
            background: white;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .search-form input {
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            margin: 5px;
            min-width: 200px;
        }
        
        .search-form button {
            padding: 12px 24px;
            background: linear-gradient(135deg, #e846c9 0%, #8e44ad 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            margin: 5px;
        }
        
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            padding: 20px 0;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        @media (min-width: 768px) {
            .gallery-grid {
                grid-template-columns: repeat(5, 1fr);
                gap: 20px;
            }
        }
        
        .gallery-item {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        
        .gallery-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        
        .image-container {
            position: relative;
            width: 100%;
            padding-bottom: 140%;
            overflow: hidden;
        }
        
        .gallery-item img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .gallery-item:hover img {
            transform: scale(1.05);
        }
        
        .gallery-info {
            padding: 15px;
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        .gallery-name {
            font-weight: 600;
            color: #333;
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            flex: 1;
            min-height: 60px;
        }
        
        .gallery-code {
            color: #666;
            font-size: 14px;
            font-weight: 500;
        }
        
        .gallery-actions {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-top: 10px;
        }
        
        .details-link {
            background: #28a745;
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 12px;
            text-align: center;
            transition: background 0.3s;
        }
        
        .details-link:hover {
            background: #218838;
            text-decoration: none;
        }
        
        .convert-btn {
            background: #ffc107;
            color: black;
            border: none;
            padding: 8px 12px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 12px;
            transition: background 0.3s;
        }
        
        .convert-btn:hover {
            background: #e0a800;
        }
        
        .convert-btn:disabled {
            background: #6c757d;
            cursor: not-allowed;
        }
        
        .pagination {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            padding: 30px 0;
            flex-wrap: wrap;
        }
        
        .pagination a {
            padding: 10px 20px;
            background: linear-gradient(135deg, #e846c9 0%, #8e44ad 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: transform 0.2s;
        }
        
        .pagination a:hover {
            transform: translateY(-2px);
            text-decoration: none;
        }
        
        .pagination span {
            font-weight: 600;
            color: #333;
            font-size: 16px;
        }
        
        .convert-all-btn {
            background: #17a2b8;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            margin: 10px;
            transition: background 0.3s;
        }
        
        .convert-all-btn:hover {
            background: #138496;
        }
        
        .convert-all-btn:disabled {
            background: #6c757d;
            cursor: not-allowed;
        }
        
        .loading {
            opacity: 0.6;
            pointer-events: none;
        }
        
        .total-results {
            text-align: center;
            color: #666;
            margin-bottom: 20px;
            font-size: 14px;
        }
        
        .no-results {
            text-align: center;
            padding: 60px 20px;
            color: #666;
        }
        
        .no-results h3 {
            margin-bottom: 10px;
            font-size: 20px;
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
            <div class="image-container">
                {% if result.image_links and result.image_links[0] %}
                <img src="{{ result.image_links[0] }}" 
                     alt="{{ result.name }}" 
                     id="img-{{ result.code }}"
                     data-original-src="{{ result.image_links[0] }}"
                     onerror="this.src='https://via.placeholder.com/300x420/e846c9/ffffff?text=Imagen+no+disponible'">
                {% else %}
                <img src="https://via.placeholder.com/300x420/cccccc/ffffff?text=Sin+imagen" 
                     alt="Sin imagen" 
                     id="img-{{ result.code }}" 
                     data-original-src="">
                {% endif %}
            </div>
            
            <div class="gallery-info">
                <div class="gallery-code">ID: {{ result.code }}</div>
                <div class="gallery-name">{{ result.name }}</div>
                
                <div class="gallery-actions">
                    <a href="/api/v3h/{{ result.code }}" class="details-link" target="_blank">
                        Ver Detalles
                    </a>
                    <button class="convert-btn" onclick="convertToBase64('{{ result.code }}')">
                        Convertir a Base64
                    </button>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    
    <div class="pagination">
        {% if current_page > 1 %}
        <a href="/api/s3h/{{ search_term }}?p={{ current_page - 1 }}">‹ Página Anterior</a>
        {% endif %}
        
        <span>Página {{ current_page }} de {{ total_pages }}</span>
        
        {% if current_page < total_pages %}
        <a href="/api/s3h/{{ search_term }}?p={{ current_page + 1 }}">Página Siguiente ›</a>
        {% endif %}
    </div>
    
    {% else %}
    <div class="no-results">
        <h3>No se encontraron resultados para "{{ search_term }}"</h3>
        <p>Intenta con otros términos de búsqueda</p>
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
                if (!response.ok) throw new Error('Error en la respuesta');
                
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
            const convertButtons = document.querySelectorAll('.convert-btn:not(:disabled)');
            const convertAllBtn = document.querySelector('.convert-all-btn');
            
            if (convertButtons.length === 0) return;
            
            convertAllBtn.disabled = true;
            convertAllBtn.textContent = 'Convirtiendo todas...';
            
            for (let i = 0; i < convertButtons.length; i++) {
                const btn = convertButtons[i];
                const galleryElement = btn.closest('.gallery-item');
                const code = galleryElement.id.replace('gallery-', '');
                const imgElement = document.getElementById(`img-${code}`);
                const originalSrc = imgElement.dataset.originalSrc;
                
                if (originalSrc && !originalSrc.includes('base64') && !originalSrc.includes('via.placeholder.com')) {
                    const event = new MouseEvent('click', {
                        view: window,
                        bubbles: true,
                        cancelable: true
                    });
                    btn.dispatchEvent(event);
                    
                    await new Promise(resolve => setTimeout(resolve, 1500));
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
                        this.src = 'https://via.placeholder.com/300x420/dc3545/ffffff?text=Error+cargando';
                    }
                });
            });
        });

        function preloadVisibleImages() {
            const images = document.querySelectorAll('img[data-original-src]');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.loaded !== 'true') {
                            img.src = img.dataset.originalSrc;
                            img.dataset.loaded = 'true';
                        }
                        observer.unobserve(img);
                    }
                });
            }, { rootMargin: '50px' });

            images.forEach(img => observer.observe(img));
        }

        document.addEventListener('DOMContentLoaded', preloadVisibleImages);
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
                    navigateImage(1);
                } else {
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
        
        document.getElementById('imageModal').addEventListener('wheel', function(e) {
            e.preventDefault();
            if (e.deltaY < 0) {
                navigateImage(-1);
            } else {
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
                    navigateImage(1);
                } else {
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
        
        document.getElementById('imageModal').addEventListener('wheel', function(e) {
            e.preventDefault();
            if (e.deltaY < 0) {
                navigateImage(-1);
            } else {
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


WEBUSERS_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Gestión de Usuarios Web</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 1000px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px; }
        .section { margin: 20px 0; padding: 20px; border: 1px solid #ddd; border-radius: 8px; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #667eea; color: white; }
        tr:hover { background: #f9f9f9; }
        .level-6 { background: #ffe6e6; }
        .level-5 { background: #fff0e6; }
        .level-4 { background: #ffffe6; }
        .level-3 { background: #e6ffe6; }
        .level-2 { background: #e6f7ff; }
        .level-1 { background: #f0e6ff; }
        .level-0 { background: #f5f5f5; }
        .btn { padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; margin: 5px; }
        .btn-create { background: #28a745; color: white; }
        .btn-delete { background: #dc3545; color: white; }
        .btn-update { background: #ffc107; color: black; }
        .form-group { margin: 10px 0; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type="text"], input[type="password"] { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        .nav { margin-bottom: 20px; }
        .nav a { margin-right: 10px; color: #667eea; text-decoration: none; }
        .permission-warning { background: #fff3cd; border: 1px solid #ffeaa7; padding: 10px; border-radius: 4px; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="container">
        <div class="nav">
            <a href="/">🏠 Inicio</a>
            <a href="/manga">📖 Manga</a>
            <a href="/utils">🛠️ Utilidades</a>
            <a href="/downloads">📥 Descargas</a>
            <a href="/webusers">👥 Usuarios Web</a>
        </div>
        
        <h1>👥 Gestión de Usuarios Web</h1>
        
        {% if current_user_level >= 4 %}
        <div class="section">
            <h2>➕ Crear Nuevo Usuario</h2>
            <form method="POST">
                <input type="hidden" name="action" value="create">
                <div class="form-group">
                    <label>ID de Usuario (numérico):</label>
                    <input type="text" name="new_id" required pattern="[0-9]+" title="Solo números">
                </div>
                <div class="form-group">
                    <label>Nombre de Usuario:</label>
                    <input type="text" name="new_user" required>
                </div>
                <div class="form-group">
                    <label>Contraseña:</label>
                    <input type="password" name="new_pass" required>
                </div>
                <button type="submit" class="btn btn-create">Crear Usuario</button>
            </form>
        </div>
        {% endif %}
        
        <div class="section">
            <h2>📋 Usuarios Existentes</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Usuario</th>
                        {% if current_user_level >= 3 %}
                        <th>Contraseña</th>
                        {% endif %}
                        <th>Nivel</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {% for uid, user_data in users.items() %}
                    <tr class="level-{{ user_data.level }}">
                        <td>{{ uid }}</td>
                        <td>{{ user_data.user }}</td>
                        {% if current_user_level >= 3 %}
                        <td>{{ user_data.pass if uid == current_user_id else '****' }}</td>
                        {% endif %}
                        <td>
                            {% if user_data.level == 6 %}Owner
                            {% elif user_data.level == 5 %}Admin
                            {% elif user_data.level == 4 %}Mod
                            {% elif user_data.level == 3 %}VIP
                            {% elif user_data.level == 2 %}User
                            {% elif user_data.level == 1 %}Guest
                            {% else %}No Access{% endif %}
                        </td>
                        <td>
                            {% if current_user_level >= 4 and current_user_level > user_data.level %}
                            <form method="POST" style="display: inline;">
                                <input type="hidden" name="action" value="update">
                                <input type="hidden" name="user_id_to_update" value="{{ uid }}">
                                <input type="text" name="new_username" placeholder="Nuevo usuario" style="width: 100px;">
                                <input type="password" name="new_password" placeholder="Nueva contraseña" style="width: 100px;">
                                <button type="submit" class="btn btn-update">Actualizar</button>
                            </form>
                            {% if current_user_level >= 5 and current_user_level > user_data.level %}
                            <form method="POST" style="display: inline;">
                                <input type="hidden" name="action" value="delete">
                                <input type="hidden" name="user_id_to_delete" value="{{ uid }}">
                                <button type="submit" class="btn btn-delete" onclick="return confirm('¿Borrar usuario {{ uid }}?')">Borrar</button>
                            </form>
                            {% endif %}
                            {% endif %}
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""
