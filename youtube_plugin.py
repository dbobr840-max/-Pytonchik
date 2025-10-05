import requests
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from datetime import datetime

class YouTubePlugin:
    def __init__(self):
        self.api_key = self.load_api_key()
        self.base_url = "https://www.googleapis.com/youtube/v3"
        
    def load_api_key(self):
        """Загрузка API ключа из файла"""
        key_file = "C:\\Pytonchik\\youtube_api_key.txt"
        if os.path.exists(key_file):
            with open(key_file, 'r') as f:
                return f.read().strip()
        else:
            # Создаем файл с инструкцией
            with open(key_file, 'w') as f:
                f.write("ВСТАВЬТЕ_ВАШ_API_КЛЮЧ_ЗДЕСЬ")
            messagebox.showwarning("YouTube API", 
                                 f"Создан файл {key_file}\n"
                                 "Получите API ключ на https://console.cloud.google.com/")
            return None
    
    def make_request(self, endpoint, params):
        """Выполнение запроса к YouTube API"""
        if not self.api_key or self.api_key == "ВСТАВЬТЕ_ВАШ_API_КЛЮЧ_ЗДЕСЬ":
            return {"error": "API ключ не настроен"}
        
        params['key'] = self.api_key
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def get_channel_stats(self, channel_id):
        """Получение статистики канала"""
        params = {
            'part': 'statistics,snippet',
            'id': channel_id
        }
        return self.make_request('channels', params)
    
    def get_channel_videos(self, channel_id, max_results=10):
        """Получение видео канала"""
        # Сначала получаем ID загрузок канала
        params = {
            'part': 'contentDetails',
            'id': channel_id
        }
        channel_data = self.make_request('channels', params)
        
        if 'error' in channel_data:
            return channel_data
        
        if 'items' not in channel_data or not channel_data['items']:
            return {"error": "Канал не найден"}
        
        uploads_playlist_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        
        # Получаем видео из плейлиста загрузок
        params = {
            'part': 'snippet',
            'playlistId': uploads_playlist_id,
            'maxResults': max_results
        }
        return self.make_request('playlistItems', params)
    
    def search_videos(self, query, max_results=10):
        """Поиск видео"""
        params = {
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'maxResults': max_results
        }
        return self.make_request('search', params)
    
    def get_video_details(self, video_id):
        """Получение информации о видео"""
        params = {
            'part': 'snippet,statistics,contentDetails',
            'id': video_id
        }
        return self.make_request('videos', params)
    
    def format_number(self, num):
        """Форматирование чисел (1K, 1M и т.д.)"""
        try:
            num = int(num)
            if num >= 1000000:
                return f"{num/1000000:.1f}M"
            elif num >= 1000:
                return f"{num/1000:.1f}K"
            else:
                return str(num)
        except:
            return num

class YouTubeGUI:
    def __init__(self, root):
        self.root = root
        self.youtube = YouTubePlugin()
        self.setup_gui()
        
    def setup_gui(self):
        """Настройка графического интерфейса"""
        self.root.title("YouTube+ 🎬 - Pytonchik Plugin")
        self.root.geometry("800x600")
        
        # Создаем вкладки
        tab_control = ttk.Notebook(self.root)
        
        # Вкладка статистики канала
        self.stats_tab = ttk.Frame(tab_control)
        tab_control.add(self.stats_tab, text='📊 Статистика канала')
        self.setup_stats_tab()
        
        # Вкладка поиска видео
        self.search_tab = ttk.Frame(tab_control)
        tab_control.add(self.search_tab, text='🔍 Поиск видео')
        self.setup_search_tab()
        
        # Вкладка просмотра видео
        self.watch_tab = ttk.Frame(tab_control)
        tab_control.add(self.watch_tab, text='🎥 Просмотр')
        self.setup_watch_tab()
        
        tab_control.pack(expand=1, fill='both')
        
    def setup_stats_tab(self):
        """Настройка вкладки статистики"""
        # Поле ввода ID канала
        ttk.Label(self.stats_tab, text="ID канала или username:").pack(pady=5)
        self.channel_entry = ttk.Entry(self.stats_tab, width=50)
        self.channel_entry.pack(pady=5)
        self.channel_entry.insert(0, "UC_x5XG1OV2P6uZZ5FSM9Ttw")  # YouTube API канал
        
        ttk.Button(self.stats_tab, text="Получить статистику", 
                  command=self.show_channel_stats).pack(pady=10)
        
        # Область для отображения статистики
        self.stats_frame = ttk.Frame(self.stats_tab)
        self.stats_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
    def setup_search_tab(self):
        """Настройка вкладки поиска"""
        ttk.Label(self.search_tab, text="Поиск видео:").pack(pady=5)
        self.search_entry = ttk.Entry(self.search_tab, width=50)
        self.search_entry.pack(pady=5)
        self.search_entry.insert(0, "Python programming")
        
        ttk.Button(self.search_tab, text="Искать видео", 
                  command=self.search_videos).pack(pady=10)
        
        # Список результатов поиска
        self.search_results = tk.Listbox(self.search_tab, height=15)
        self.search_results.pack(fill='both', expand=True, padx=10, pady=5)
        self.search_results.bind('<<ListboxSelect>>', self.on_video_select)
        
    def setup_watch_tab(self):
        """Настройка вкладки просмотра"""
        ttk.Label(self.watch_tab, text="ID видео для просмотра:").pack(pady=5)
        self.video_entry = ttk.Entry(self.watch_tab, width=50)
        self.video_entry.pack(pady=5)
        
        ttk.Button(self.watch_tab, text="Смотреть видео", 
                  command=self.watch_video).pack(pady=10)
        
        # Информация о видео
        self.video_info = tk.Text(self.watch_tab, height=10, wrap='word')
        self.video_info.pack(fill='both', expand=True, padx=10, pady=5)
        
    def show_channel_stats(self):
        """Показать статистику канала"""
        channel_id = self.channel_entry.get().strip()
        if not channel_id:
            messagebox.showerror("Ошибка", "Введите ID канала")
            return
        
        # Очищаем предыдущие результаты
        for widget in self.stats_frame.winfo_children():
            widget.destroy()
        
        data = self.youtube.get_channel_stats(channel_id)
        
        if 'error' in data:
            ttk.Label(self.stats_frame, text=f"Ошибка: {data['error']}").pack()
            return
        
        if 'items' not in data or not data['items']:
            ttk.Label(self.stats_frame, text="Канал не найден").pack()
            return
        
        channel = data['items'][0]
        snippet = channel['snippet']
        stats = channel['statistics']
        
        # Отображаем информацию
        info_text = f"""
📺 Канал: {snippet['title']}
📝 Описание: {snippet['description'][:100]}...
👥 Подписчики: {self.youtube.format_number(stats.get('subscriberCount', 'N/A'))}
📊 Просмотры: {self.youtube.format_number(stats.get('viewCount', 'N/A'))}
🎬 Видео: {self.youtube.format_number(stats.get('videoCount', 'N/A'))}
🕒 Создан: {snippet['publishedAt'][:10]}
        """
        
        ttk.Label(self.stats_frame, text=info_text, justify='left').pack(anchor='w')
        
        # Показываем последние видео
        ttk.Label(self.stats_frame, text="\n🎥 Последние видео:", 
                 font=('Arial', 10, 'bold')).pack(anchor='w', pady=(10,5))
        
        videos_data = self.youtube.get_channel_videos(channel_id, 5)
        if 'items' in videos_data:
            for video in videos_data['items']:
                title = video['snippet']['title']
                btn = ttk.Button(self.stats_frame, text=title[:50] + "...", 
                               command=lambda v=video: self.open_video(v['snippet']['resourceId']['videoId']))
                btn.pack(anchor='w', pady=2)
        
    def search_videos(self):
        """Поиск видео"""
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showerror("Ошибка", "Введите поисковый запрос")
            return
        
        self.search_results.delete(0, tk.END)
        
        data = self.youtube.search_videos(query, 15)
        
        if 'error' in data:
            self.search_results.insert(tk.END, f"Ошибка: {data['error']}")
            return
        
        if 'items' not in data:
            self.search_results.insert(tk.END, "Видео не найдены")
            return
        
        for video in data['items']:
            title = video['snippet']['title']
            channel = video['snippet']['channelTitle']
            self.search_results.insert(tk.END, f"{title} | {channel}")
            self.search_results.video_data = data['items']  # Сохраняем данные
    
    def on_video_select(self, event):
        """Обработка выбора видео из списка"""
        selection = self.search_results.curselection()
        if selection:
            index = selection[0]
            video_data = self.search_results.video_data[index]
            video_id = video_data['id']['videoId']
            
            # Получаем детальную информацию о видео
            details = self.youtube.get_video_details(video_id)
            if 'items' in details:
                video = details['items'][0]
                self.show_video_details(video)
    
    def show_video_details(self, video):
        """Показать информацию о видео"""
        snippet = video['snippet']
        stats = video.get('statistics', {})
        
        info_text = f"""
🎬 Название: {snippet['title']}
📺 Канал: {snippet['channelTitle']}
📝 Описание: {snippet['description'][:200]}...
👀 Просмотры: {self.youtube.format_number(stats.get('viewCount', 'N/A'))}
👍 Лайков: {self.youtube.format_number(stats.get('likeCount', 'N/A'))}
💬 Комментарии: {self.youtube.format_number(stats.get('commentCount', 'N/A'))}
🕒 Опубликовано: {snippet['publishedAt'][:10]}
📏 Длительность: {video.get('contentDetails', {}).get('duration', 'N/A')}
        """
        
        self.video_info.delete(1.0, tk.END)
        self.video_info.insert(1.0, info_text)
        
        # Сохраняем ID видео для кнопки просмотра
        self.video_entry.delete(0, tk.END)
        self.video_entry.insert(0, video['id'])
    
    def watch_video(self):
        """Открыть видео в браузере"""
        video_id = self.video_entry.get().strip()
        if video_id:
            webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")
    
    def open_video(self, video_id):
        """Открыть видео по ID"""
        webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")

def start_youtube_plugin():
    """Запуск плагина YouTube"""
    root = tk.Tk()
    app = YouTubeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    start_youtube_plugin()