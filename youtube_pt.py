import sys
import os
sys.path.append('C:\\Pytonchik')

try:
    from youtube_plugin import YouTubePlugin
    YOUTUBE_AVAILABLE = True
except ImportError:
    YOUTUBE_AVAILABLE = False

class PytonchikYouTube:
    def __init__(self):
        self.youtube = YouTubePlugin() if YOUTUBE_AVAILABLE else None
        self.output = []
    
    def execute_command(self, command, args):
        """Выполнение YouTube команд"""
        if not YOUTUBE_AVAILABLE:
            return "❌ Плагин YouTube не доступен"
        
        if command == 'youtube_статистика':
            return self.get_channel_stats(args[0] if args else None)
        elif command == 'youtube_поиск':
            return self.search_videos(args[0] if args else "Python")
        elif command == 'youtube_видео':
            return self.get_video_info(args[0] if args else None)
        elif command == 'youtube_запустить':
            return self.launch_gui()
        else:
            return f"❌ Неизвестная команда: {command}"
    
    def get_channel_stats(self, channel_id):
        """Получить статистику канала"""
        if not channel_id:
            return "❌ Укажите ID канала"
        
        data = self.youtube.get_channel_stats(channel_id)
        
        if 'error' in data:
            return f"❌ Ошибка: {data['error']}"
        
        if 'items' not in data or not data['items']:
            return "❌ Канал не найден"
        
        channel = data['items'][0]
        snippet = channel['snippet']
        stats = channel['statistics']
        
        result = f"""
📺 Канал: {snippet['title']}
👥 Подписчики: {self.youtube.format_number(stats.get('subscriberCount', 'N/A'))}
📊 Просмотры: {self.youtube.format_number(stats.get('viewCount', 'N/A'))}
🎬 Видео: {self.youtube.format_number(stats.get('videoCount', 'N/A'))}
        """
        
        return result
    
    def search_videos(self, query):
        """Поиск видео"""
        data = self.youtube.search_videos(query, 5)
        
        if 'error' in data:
            return f"❌ Ошибка: {data['error']}"
        
        if 'items' not in data:
            return "❌ Видео не найдены"
        
        result = "🔍 Результаты поиска:\n"
        for i, video in enumerate(data['items'], 1):
            title = video['snippet']['title']
            channel = video['snippet']['channelTitle']
            result += f"{i}. {title}\n   📺 {channel}\n\n"
        
        return result
    
    def get_video_info(self, video_id):
        """Получить информацию о видео"""
        if not video_id:
            return "❌ Укажите ID видео"
        
        data = self.youtube.get_video_details(video_id)
        
        if 'error' in data:
            return f"❌ Ошибка: {data['error']}"
        
        if 'items' not in data or not data['items']:
            return "❌ Видео не найдено"
        
        video = data['items'][0]
        snippet = video['snippet']
        stats = video.get('statistics', {})
        
        result = f"""
🎬 Название: {snippet['title']}
📺 Канал: {snippet['channelTitle']}
👀 Просмотры: {self.youtube.format_number(stats.get('viewCount', 'N/A'))}
👍 Лайков: {self.youtube.format_number(stats.get('likeCount', 'N/A'))}
💬 Комментарии: {self.youtube.format_number(stats.get('commentCount', 'N/A'))}
🕒 Опубликовано: {snippet['publishedAt'][:10]}
        """
        
        return result
    
    def launch_gui(self):
        """Запуск графического интерфейса"""
        try:
            from youtube_plugin import start_youtube_plugin
            start_youtube_plugin()
            return "✅ YouTube+ GUI запущен"
        except Exception as e:
            return f"❌ Ошибка запуска GUI: {e}"

# Глобальный экземпляр для использования в Pytonchik
youtube_manager = PytonchikYouTube()

def youtube_command(command, *args):
    """Функция для вызова из Pytonchik"""
    return youtube_manager.execute_command(command, args)