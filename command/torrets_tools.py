import time
import datetime
import requests
from bs4 import BeautifulSoup
import urllib.parse
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from command.torrets_dl import process_magnet_download_telegram, download_from_magnet_or_torrent, get_download_progress, cleanup_old_downloads

nyaa_cache = {}
sukebei_cache = {}
CACHE_DURATION = 600

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")

def search_nyaa(query):
    base_url = "https://nyaa.si/"
    search_query = urllib.parse.quote_plus(query)
    page = 1
    results = []
    previous_results = []
    
    while True:
        url = f"{base_url}?q={search_query}&f=0&c=0_0&p={page}"
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', class_='torrent-list')
            
            if not table:
                break
                
            current_page_results = []
            rows = table.find_all('tr')[1:]
            
            for row in rows:
                try:
                    name_cell = row.find('td', colspan="2")
                    if not name_cell:
                        continue
                    
                    name_links = name_cell.find_all('a', href=lambda x: x and '/view/' in x)
                    if not name_links:
                        continue
                    
                    name = name_links[-1].get_text(strip=True)
                    
                    torrent_link = None
                    magnet_link = None
                    
                    download_links = row.find_all('a')
                    for link in download_links:
                        href = link.get('href', '')
                        if href.startswith('/download/'):
                            torrent_link = f"https://nyaa.si{href}"
                        elif href.startswith('magnet:'):
                            magnet_link = href
                    
                    size_td = row.find('td', class_='text-center', string=lambda x: x and 'MiB' in x or 'GiB' in x)
                    size = size_td.get_text(strip=True) if size_td else "N/A"
                    
                    date_td = row.find('td', class_='text-center', attrs={'data-timestamp': True})
                    date = date_td.get_text(strip=True) if date_td else "N/A"
                    
                    current_page_results.append({
                        'name': name,
                        'torrent': torrent_link,
                        'magnet': magnet_link,
                        'size': size,
                        'date': date
                    })
                    
                except Exception as e:
                    continue
            
            if not current_page_results:
                break
                
            if previous_results and current_page_results == previous_results:
                break
                
            results.extend(current_page_results)
            previous_results = current_page_results
            page += 1
            
        except requests.RequestException:
            break
        except Exception as e:
            break
    
    output = ""
    for i, result in enumerate(results, 1):
        output += f"Resultado {i}\n"
        output += f"{result['name']}\n"
        output += f"Tamaño: {result['size']}\n"
        output += f"Fecha: {result['date']}\n"
        if result['torrent']:
            output += f"Link de Torrent: {result['torrent']}\n"
        if result['magnet']:
            output += f"Link de Magnet: {result['magnet']}\n"
        output += "\n"
    
    return output

async def search_in_nyaa(client, message, search_query):
    current_time = time.time()
    expired_keys = [key for key, data in nyaa_cache.items() if current_time - data['timestamp'] > CACHE_DURATION]
    for key in expired_keys:
        del nyaa_cache[key]
    cache_key = f"{message.chat.id}_{search_query.lower()}"
    
    if cache_key in nyaa_cache:
        results = nyaa_cache[cache_key]['results']
    else:
        results_data = search_nyaa(search_query)
        if not results_data.strip():
            await message.reply("❌ No se encontraron resultados para tu búsqueda.")
            return
        
        results = []
        current_result = {}
        for line in results_data.split('\n'):
            line = line.strip()
            if line.startswith('Resultado'):
                if current_result:
                    results.append(current_result)
                current_result = {'index': int(line.split()[1])}
            elif line and not line.startswith(('Link de Torrent:', 'Link de Magnet:')):
                if 'name' not in current_result:
                    current_result['name'] = line
                elif line.startswith('Tamaño:'):
                    current_result['size'] = line.replace('Tamaño: ', '')
                elif line.startswith('Fecha:'):
                    current_result['date'] = line.replace('Fecha: ', '')
            elif line.startswith('Link de Torrent:'):
                current_result['torrent'] = line.replace('Link de Torrent: ', '')
            elif line.startswith('Link de Magnet:'):
                current_result['magnet'] = line.replace('Link de Magnet: ', '')
        
        if current_result:
            results.append(current_result)
    
        nyaa_cache[cache_key] = {
            'results': results,
            'timestamp': current_time,
            'current_index': 0
        }
        
    await show_nyaa_result(client, message, cache_key, 0)

def search_sukebei(query):
    base_url = "https://sukebei.nyaa.si/"
    search_query = urllib.parse.quote_plus(query)
    page = 1
    results = []
    
    while True:
        url = f"{base_url}?q={search_query}&f=0&c=0_0&p={page}"
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', class_='torrent-list')
            
            if not table:
                break
                
            current_page_results = []
            rows = table.find_all('tr')[1:]
            
            if not rows:
                break
                
            for row in rows:
                try:
                    name_cell = row.find('td', colspan="2")
                    if not name_cell:
                        continue
                    
                    name_links = name_cell.find_all('a', href=lambda x: x and '/view/' in x)
                    if not name_links:
                        continue
                    
                    name = name_links[-1].get_text(strip=True)
                    
                    torrent_link = None
                    magnet_link = None
                    
                    download_links = row.find_all('a')
                    for link in download_links:
                        href = link.get('href', '')
                        if href.startswith('/download/'):
                            torrent_link = f"https://sukebei.nyaa.si{href}"
                        elif href.startswith('magnet:'):
                            magnet_link = href
                    
                    size_td = row.find('td', class_='text-center', string=lambda x: x and 'MiB' in x or 'GiB' in x)
                    size = size_td.get_text(strip=True) if size_td else "N/A"
                    
                    date_td = row.find('td', class_='text-center', attrs={'data-timestamp': True})
                    date = date_td.get_text(strip=True) if date_td else "N/A"
                    
                    current_page_results.append({
                        'name': name,
                        'torrent': torrent_link,
                        'magnet': magnet_link,
                        'size': size,
                        'date': date
                    })
                    
                except Exception as e:
                    continue
            
            if not current_page_results:
                break
                
            results.extend(current_page_results)
            page += 1
            
        except requests.RequestException:
            break
        except Exception as e:
            break
    
    output = ""
    for i, result in enumerate(results, 1):
        output += f"Resultado {i}\n"
        output += f"{result['name']}\n"
        output += f"Tamaño: {result['size']}\n"
        output += f"Fecha: {result['date']}\n"
        if result['torrent']:
            output += f"Link de Torrent: {result['torrent']}\n"
        if result['magnet']:
            output += f"Link de Magnet: {result['magnet']}\n"
        output += "\n"
    
    return output

async def search_in_sukebei(client, message, search_query):
    current_time = time.time()
    expired_keys = [key for key, data in sukebei_cache.items() if current_time - data['timestamp'] > CACHE_DURATION]
    for key in expired_keys:
        del sukebei_cache[key]
    cache_key = f"sukebei_{message.chat.id}_{search_query.lower()}"
    
    if cache_key in sukebei_cache:
        results = sukebei_cache[cache_key]['results']
    else:
        results_data = search_sukebei(search_query)
        if not results_data.strip():
            await message.reply("❌ No se encontraron resultados para tu búsqueda.")
            return
        
        results = []
        current_result = {}
        for line in results_data.split('\n'):
            line = line.strip()
            if line.startswith('Resultado'):
                if current_result:
                    results.append(current_result)
                current_result = {'index': int(line.split()[1])}
            elif line and not line.startswith(('Link de Torrent:', 'Link de Magnet:')):
                if 'name' not in current_result:
                    current_result['name'] = line
                elif line.startswith('Tamaño:'):
                    current_result['size'] = line.replace('Tamaño: ', '')
                elif line.startswith('Fecha:'):
                    current_result['date'] = line.replace('Fecha: ', '')
            elif line.startswith('Link de Torrent:'):
                current_result['torrent'] = line.replace('Link de Torrent: ', '')
            elif line.startswith('Link de Magnet:'):
                current_result['magnet'] = line.replace('Link de Magnet: ', '')
        
        if current_result:
            results.append(current_result)
    
        sukebei_cache[cache_key] = {
            'results': results,
            'timestamp': current_time,
            'current_index': 0
        }
        
    await show_sukebei_result(client, message, cache_key, 0)

async def show_nyaa_result(client, message, cache_key, index):
    if cache_key not in nyaa_cache:
        await message.reply("❌ Los resultados de búsqueda han expirado.")
        return
    
    cache_data = nyaa_cache[cache_key]
    results = cache_data['results']
    
    if index < 0 or index >= len(results):
        await message.reply("❌ Índice de resultado inválido.")
        return
    
    result = results[index]
    cache_data['current_index'] = index
    
    keyboard = []
    
    row1_buttons = []
    if 'torrent' in result:
        row1_buttons.append(InlineKeyboardButton("📥 Torrent", callback_data=f"nyaa_torrent:{cache_key}:{index}"))
    if 'magnet' in result:
        row1_buttons.append(InlineKeyboardButton("🧲 Magnet", callback_data=f"nyaa_magnet:{cache_key}:{index}"))
    
    if row1_buttons:
        keyboard.append(row1_buttons)
    
    row2_buttons = []
    if 'magnet' in result:
        row2_buttons.append(InlineKeyboardButton("🔽DL", callback_data=f"nyaa_dl:{cache_key}:{index}"))
        row2_buttons.append(InlineKeyboardButton("🔽ZIP DL", callback_data=f"nyaa_zip:{cache_key}:{index}"))
    
    if row2_buttons:
        keyboard.append(row2_buttons)
    
    row3_buttons = []
    if any('magnet' in r for r in results):
        if index == 0:
            row3_buttons.append(InlineKeyboardButton("🔽DL All", callback_data=f"nyaa_dl_all:{cache_key}"))
        elif index == len(results) - 1:
            row3_buttons.append(InlineKeyboardButton("🔽DL All Reverse", callback_data=f"nyaa_dl_all_reverse:{cache_key}"))
    
    if row3_buttons:
        keyboard.append(row3_buttons)
    
    nav_buttons = []
    if index > 0:
        nav_buttons.append(InlineKeyboardButton("◀️", callback_data=f"nyaa_prev:{cache_key}"))
        nav_buttons.append(InlineKeyboardButton("⏪", callback_data=f"nyaa_first:{cache_key}"))
    if index < len(results) - 1:
        nav_buttons.append(InlineKeyboardButton("⏩", callback_data=f"nyaa_last:{cache_key}"))
        nav_buttons.append(InlineKeyboardButton("▶️", callback_data=f"nyaa_next:{cache_key}"))
    
    if nav_buttons:
        keyboard.append(nav_buttons)
    
    reply_markup = InlineKeyboardMarkup(keyboard) if keyboard else None
    
    message_text = f"**Resultado {index + 1}/{len(results)}**\n"
    message_text += f"**Nombre:** {result['name']}\n"
    message_text += f"**Fecha:** {result.get('date', 'N/A')}\n"
    message_text += f"**Tamaño:** {result.get('size', 'N/A')}"
    
    if cache_data.get('message_id'):
        try:
            await client.edit_message_text(
                chat_id=message.chat.id,
                message_id=cache_data['message_id'],
                text=message_text,
                reply_markup=reply_markup
            )
            return
        except:
            pass
    
    sent_message = await message.reply(message_text, reply_markup=reply_markup)
    cache_data['message_id'] = sent_message.id

async def show_sukebei_result(client, message, cache_key, index):
    if cache_key not in sukebei_cache:
        await message.reply("❌ Los resultados de búsqueda han expirado.")
        return
    
    cache_data = sukebei_cache[cache_key]
    results = cache_data['results']
    
    if index < 0 or index >= len(results):
        await message.reply("❌ Índice de resultado inválido.")
        return
    
    result = results[index]
    cache_data['current_index'] = index
    
    keyboard = []
    
    row1_buttons = []
    if 'torrent' in result:
        row1_buttons.append(InlineKeyboardButton("📥 Torrent", callback_data=f"sukebei_torrent:{cache_key}:{index}"))
    if 'magnet' in result:
        row1_buttons.append(InlineKeyboardButton("🧲 Magnet", callback_data=f"sukebei_magnet:{cache_key}:{index}"))
    
    if row1_buttons:
        keyboard.append(row1_buttons)
    
    row2_buttons = []
    if 'magnet' in result:
        row2_buttons.append(InlineKeyboardButton("🔽DL", callback_data=f"sukebei_dl:{cache_key}:{index}"))
        row2_buttons.append(InlineKeyboardButton("🔽ZIP DL", callback_data=f"sukebei_zip:{cache_key}:{index}"))
    
    if row2_buttons:
        keyboard.append(row2_buttons)
    
    row3_buttons = []
    if any('magnet' in r for r in results):
        if index == 0:
            row3_buttons.append(InlineKeyboardButton("🔽DL All", callback_data=f"sukebei_dl_all:{cache_key}"))
        elif index == len(results) - 1:
            row3_buttons.append(InlineKeyboardButton("🔽DL All Reverse", callback_data=f"sukebei_dl_all_reverse:{cache_key}"))
    
    if row3_buttons:
        keyboard.append(row3_buttons)
    
    nav_buttons = []
    if index > 0:
        nav_buttons.append(InlineKeyboardButton("◀️", callback_data=f"sukebei_prev:{cache_key}"))
        nav_buttons.append(InlineKeyboardButton("⏪", callback_data=f"sukebei_first:{cache_key}"))
    if index < len(results) - 1:
        nav_buttons.append(InlineKeyboardButton("⏩", callback_data=f"sukebei_last:{cache_key}"))
        nav_buttons.append(InlineKeyboardButton("▶️", callback_data=f"sukebei_next:{cache_key}"))
    
    if nav_buttons:
        keyboard.append(nav_buttons)
    
    reply_markup = InlineKeyboardMarkup(keyboard) if keyboard else None
    
    message_text = f"**Resultado {index + 1}/{len(results)}**\n"
    message_text += f"**Nombre:** {result['name']}\n"
    message_text += f"**Fecha:** {result.get('date', 'N/A')}\n"
    message_text += f"**Tamaño:** {result.get('size', 'N/A')}"
    
    if cache_data.get('message_id'):
        try:
            await client.edit_message_text(
                chat_id=message.chat.id,
                message_id=cache_data['message_id'],
                text=message_text,
                reply_markup=reply_markup
            )
            return
        except:
            pass
    
    sent_message = await message.reply(message_text, reply_markup=reply_markup)
    cache_data['message_id'] = sent_message.id

async def handle_nyaa_callback(client, callback_query):
    data = callback_query.data
    parts = data.split(':')
    
    if len(parts) < 2:
        await callback_query.answer("❌ Error en los datos")
        return
    
    action = parts[0]
    cache_key = parts[1]
    
    if cache_key not in nyaa_cache:
        await callback_query.answer("❌ Los resultados han expirado")
        await callback_query.message.delete()
        return
    
    cache_data = nyaa_cache[cache_key]
    results = cache_data['results']
    current_index = cache_data['current_index']
    
    if action == "nyaa_torrent":
        index = int(parts[2])
        result = results[index]
        
        await callback_query.answer("📥 Enviando link de torrent...")
        await client.send_message(
            chat_id=callback_query.message.chat.id,
            text=result['torrent']
        )
        
    elif action == "nyaa_magnet":
        index = int(parts[2])
        result = results[index]
        await callback_query.answer("🧲 Enviando magnet...")
        await client.send_message(
            chat_id=callback_query.message.chat.id,
            text=result['magnet']
        )
        
    elif action == "nyaa_dl":
        index = int(parts[2])
        result = results[index]
        await callback_query.answer("🔽 Iniciando descarga...")
        await process_magnet_download_telegram(client, callback_query.message, result['magnet'], False)
        
    elif action == "nyaa_zip":
        index = int(parts[2])
        result = results[index]
        await callback_query.answer("🔽 Iniciando descarga comprimida...")
        await process_magnet_download_telegram(client, callback_query.message, result['magnet'], True)
        
    elif action == "nyaa_dl_all":
        await callback_query.answer("🔽 Iniciando descarga de todos los resultados...")
        for result in results:
            if 'magnet' in result:
                await process_magnet_download_telegram(client, callback_query.message, result['magnet'], False)
        
    elif action == "nyaa_dl_all_reverse":
        await callback_query.answer("🔽 Iniciando descarga de todos los resultados en orden inverso...")
        for result in reversed(results):
            if 'magnet' in result:
                await process_magnet_download_telegram(client, callback_query.message, result['magnet'], False)
        
    elif action == "nyaa_prev":
        new_index = max(0, current_index - 1)
        await show_nyaa_result(client, callback_query.message, cache_key, new_index)
        await callback_query.answer()
        
    elif action == "nyaa_next":
        new_index = min(len(results) - 1, current_index + 1)
        await show_nyaa_result(client, callback_query.message, cache_key, new_index)
        await callback_query.answer()
        
    elif action == "nyaa_first":
        await show_nyaa_result(client, callback_query.message, cache_key, 0)
        await callback_query.answer()
        
    elif action == "nyaa_last":
        await show_nyaa_result(client, callback_query.message, cache_key, len(results) - 1)
        await callback_query.answer()

async def handle_sukebei_callback(client, callback_query):
    data = callback_query.data
    parts = data.split(':')
    
    if len(parts) < 2:
        await callback_query.answer("❌ Error en los datos")
        return
    
    action = parts[0]
    cache_key = parts[1]
    
    if cache_key not in sukebei_cache:
        await callback_query.answer("❌ Los resultados han expirado")
        await callback_query.message.delete()
        return
    
    cache_data = sukebei_cache[cache_key]
    results = cache_data['results']
    current_index = cache_data['current_index']
    
    if action == "sukebei_torrent":
        index = int(parts[2])
        result = results[index]
        
        await callback_query.answer("📥 Enviando link de torrent...")
        await client.send_message(
            chat_id=callback_query.message.chat.id,
            text=result['torrent']
        )
        
    elif action == "sukebei_magnet":
        index = int(parts[2])
        result = results[index]
        await callback_query.answer("🧲 Enviando magnet...")
        await client.send_message(
            chat_id=callback_query.message.chat.id,
            text=result['magnet']
        )
        
    elif action == "sukebei_dl":
        index = int(parts[2])
        result = results[index]
        await callback_query.answer("🔽 Iniciando descarga...")
        await process_magnet_download_telegram(client, callback_query.message, result['magnet'], False)
        
    elif action == "sukebei_zip":
        index = int(parts[2])
        result = results[index]
        await callback_query.answer("🔽 Iniciando descarga comprimida...")
        await process_magnet_download_telegram(client, callback_query.message, result['magnet'], True)
        
    elif action == "sukebei_dl_all":
        await callback_query.answer("🔽 Iniciando descarga de todos los resultados...")
        for result in results:
            if 'magnet' in result:
                await process_magnet_download_telegram(client, callback_query.message, result['magnet'], False)
        
    elif action == "sukebei_dl_all_reverse":
        await callback_query.answer("🔽 Iniciando descarga de todos los resultados en orden inverso...")
        for result in reversed(results):
            if 'magnet' in result:
                await process_magnet_download_telegram(client, callback_query.message, result['magnet'], False)
        
    elif action == "sukebei_prev":
        new_index = max(0, current_index - 1)
        await show_sukebei_result(client, callback_query.message, cache_key, new_index)
        await callback_query.answer()
        
    elif action == "sukebei_next":
        new_index = min(len(results) - 1, current_index + 1)
        await show_sukebei_result(client, callback_query.message, cache_key, new_index)
        await callback_query.answer()
        
    elif action == "sukebei_first":
        await show_sukebei_result(client, callback_query.message, cache_key, 0)
        await callback_query.answer()
        
    elif action == "sukebei_last":
        await show_sukebei_result(client, callback_query.message, cache_key, len(results) - 1)
        await callback_query.answer()
