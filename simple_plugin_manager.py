import os
import sys
import subprocess
import json

class SimplePluginManager:
    def __init__(self):
        self.plugins_dir = "C:\\Pytonchik\\plugins"
        os.makedirs(self.plugins_dir, exist_ok=True)
        
    def list_plugins(self):
        """Список доступных плагинов"""
        plugins = {
            "youtube-plus": {
                "name": "YouTube+",
                "description": "🎬 Управление YouTube через Pytonchik",
                "version": "1.0"
            },
            "info-mods": {
                "name": "Info+Mods", 
                "description": "🚀 200+ модификаций для Pytonchik",
                "version": "1.0"
            },
            "game-engine": {
                "name": "Game Engine",
                "description": "🎮 Движок для создания 2D игр", 
                "version": "1.0"
            },
            "ai-assistant": {
                "name": "AI Assistant",
                "description": "🤖 Голосовой помощник с ИИ",
                "version": "1.0"
            }
        }
        
        print("📦 ДОСТУПНЫЕ ПЛАГИНЫ:")
        print("=" * 50)
        for plugin_id, info in plugins.items():
            print(f"🔹 {info['name']}")
            print(f"   📝 {info['description']}")
            print(f"   🏷️  Версия: {info['version']}")
            print(f"   🔧 Установка: install-sets {plugin_id}")
            print()
    
    def install_plugin(self, plugin_name):
        """Установка плагина"""
        plugins = {
            "youtube-plus": self.install_youtube_plus,
            "info-mods": self.install_info_mods,
            "game-engine": self.install_game_engine,
            "ai-assistant": self.install_ai_assistant
        }
        
        if plugin_name in plugins:
            print(f"🚀 Устанавливаю {plugin_name}...")
            print("-" * 40)
            plugins[plugin_name]()
            print("-" * 40)
            print(f"✅ {plugin_name} успешно установлен!")
        else:
            print(f"❌ Плагин '{plugin_name}' не найден")
            print("📋 Доступные плагины: youtube-plus, info-mods, game-engine, ai-assistant")
    
    def install_youtube_plus(self):
        """Установка YouTube+ плагина"""
        youtube_code = '''import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

def youtube_gui():
    root = tk.Tk()
    root.title("YouTube+ 🎬")
    root.geometry("500x400")
    
    # Стили
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 10))
    style.configure('TLabel', font=('Arial', 11))
    
    # Заголовок
    title_label = ttk.Label(root, text="YouTube+ Plugin", font=('Arial', 16, 'bold'))
    title_label.pack(pady=20)
    
    # Статус
    status_label = ttk.Label(root, text="✅ Плагин успешно установлен!", foreground="green")
    status_label.pack(pady=10)
    
    # Фрейм с кнопками
    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=20)
    
    # Кнопки функций
    ttk.Button(btn_frame, text="📊 Статистика канала", 
              command=lambda: messagebox.showinfo("YouTube+", "Функция статистики канала")).pack(pady=5, fill='x')
    
    ttk.Button(btn_frame, text="🔍 Поиск видео", 
              command=lambda: messagebox.showinfo("YouTube+", "Функция поиска видео")).pack(pady=5, fill='x')
    
    ttk.Button(btn_frame, text="🎬 Просмотр видео", 
              command=lambda: webbrowser.open("https://www.youtube.com")).pack(pady=5, fill='x')
    
    ttk.Button(btn_frame, text="📈 Тренды", 
              command=lambda: messagebox.showinfo("YouTube+", "Популярные видео")).pack(pady=5, fill='x')
    
    # Кнопка выхода
    ttk.Button(root, text="❌ Выход", 
              command=root.quit).pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    youtube_gui()
'''
        
        # Сохраняем плагин
        plugin_file = os.path.join(self.plugins_dir, "youtube_plus.py")
        with open(plugin_file, "w", encoding="utf-8") as f:
            f.write(youtube_code)
        
        # Создаем бат-файл для запуска
        bat_content = '''@echo off
chcp 65001
echo 🎬 Запуск YouTube+ плагина...
python "C:\\Pytonchik\\plugins\\youtube_plus.py"
'''
        bat_file = os.path.join(self.plugins_dir, "youtube_plus.bat")
        with open(bat_file, "w", encoding="utf-8") as f:
            f.write(bat_content)
        
        print("📁 Создан файл: youtube_plus.py")
        print("📁 Создан файл: youtube_plus.bat")
        print("🚀 Запуск: youtube-plus")
    
    def install_info_mods(self):
        """Установка Info+Mods плагина"""
        info_mods_code = '''import tkinter as tk
from tkinter import ttk, messagebox
import random
import psutil
import platform

def info_mods_gui():
    root = tk.Tk()
    root.title("Info+Mods 🚀")
    root.geometry("600x500")
    
    # Стили
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 10))
    style.configure('TLabel', font=('Arial', 11))
    
    # Заголовок
    title_label = ttk.Label(root, text="Info+Mods - 200+ функций", font=('Arial', 16, 'bold'))
    title_label.pack(pady=20)
    
    # Статус
    status_label = ttk.Label(root, text="✅ Плагин успешно установлен!", foreground="green")
    status_label.pack(pady=10)
    
    # Фрейм с вкладками
    tab_control = ttk.Notebook(root)
    
    # Вкладка системы
    system_tab = ttk.Frame(tab_control)
    tab_control.add(system_tab, text='🖥️ Система')
    
    # Вкладка развлечений
    fun_tab = ttk.Frame(tab_control)
    tab_control.add(fun_tab, text='🎮 Развлечения')
    
    tab_control.pack(expand=1, fill='both', padx=10, pady=10)
    
    # Системные кнопки
    ttk.Button(system_tab, text="📊 Информация о системе", 
              command=lambda: messagebox.showinfo("Система", f"OS: {platform.system()}\\nCPU: {psutil.cpu_percent()}%")).pack(pady=5)
    
    ttk.Button(system_tab, text="💾 Информация о памяти", 
              command=lambda: messagebox.showinfo("Память", f"RAM: {psutil.virtual_memory().percent}%")).pack(pady=5)
    
    # Развлекательные кнопки
    ttk.Button(fun_tab, text="😂 Случайная шутка", 
              command=lambda: messagebox.showinfo("Шутка", random.choice([
                  "Почему программисты путают Хэллоуин и Рождество? Oct 31 == Dec 25!",
                  "Сколько программистов нужно для вкручивания лампочки? Ни одного!"
              ]))).pack(pady=5)
    
    ttk.Button(fun_tab, text="🎲 Случайное число", 
              command=lambda: messagebox.showinfo("Число", f"Ваше число: {random.randint(1, 100)}")).pack(pady=5)
    
    # Кнопка выхода
    ttk.Button(root, text="❌ Выход", 
              command=root.quit).pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    info_mods_gui()
'''
        
        # Сохраняем плагин
        plugin_file = os.path.join(self.plugins_dir, "info_mods.py")
        with open(plugin_file, "w", encoding="utf-8") as f:
            f.write(info_mods_code)
        
        # Создаем бат-файл для запуска
        bat_content = '''@echo off
chcp 65001
echo 🚀 Запуск Info+Mods плагина...
python "C:\\Pytonchik\\plugins\\info_mods.py"
'''
        bat_file = os.path.join(self.plugins_dir, "info_mods.bat")
        with open(bat_file, "w", encoding="utf-8") as f:
            f.write(bat_content)
        
        print("📁 Создан файл: info_mods.py")
        print("📁 Создан файл: info_mods.bat")
        print("🚀 Запуск: info-mods")
        
        # Пробуем установить psutil
        try:
            import psutil
            print("✅ psutil уже установлен")
        except:
            print("📦 Устанавливаю psutil...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    
    def install_game_engine(self):
        """Установка Game Engine плагина"""
        game_code = '''import tkinter as tk
from tkinter import ttk, messagebox

def game_engine_gui():
    root = tk.Tk()
    root.title("Game Engine 🎮")
    root.geometry("500x400")
    
    # Заголовок
    title_label = ttk.Label(root, text="Game Engine Plugin", font=('Arial', 16, 'bold'))
    title_label.pack(pady=20)
    
    status_label = ttk.Label(root, text="✅ Плагин успешно установлен!", foreground="green")
    status_label.pack(pady=10)
    
    # Игры
    games_frame = ttk.Frame(root)
    games_frame.pack(pady=20)
    
    ttk.Button(games_frame, text="🐍 Змейка", 
              command=lambda: messagebox.showinfo("Змейка", "Запуск игры Змейка...")).pack(pady=5, fill='x')
    
    ttk.Button(games_frame, text="🧩 Тетрис", 
              command=lambda: messagebox.showinfo("Тетрис", "Запуск игры Тетрис...")).pack(pady=5, fill='x')
    
    ttk.Button(games_frame, text="🎯 Арканоид", 
              command=lambda: messagebox.showinfo("Арканоид", "Запуск игры Арканоид...")).pack(pady=5, fill='x')
    
    ttk.Button(root, text="❌ Выход", 
              command=root.quit).pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    game_engine_gui()
'''
        
        plugin_file = os.path.join(self.plugins_dir, "game_engine.py")
        with open(plugin_file, "w", encoding="utf-8") as f:
            f.write(game_code)
        
        print("📁 Создан файл: game_engine.py")
        print("🚀 Запуск: game-engine")
    
    def install_ai_assistant(self):
        """Установка AI Assistant плагина"""
        ai_code = '''import tkinter as tk
from tkinter import ttk, messagebox

def ai_assistant_gui():
    root = tk.Tk()
    root.title("AI Assistant 🤖")
    root.geometry("500x400")
    
    # Заголовок
    title_label = ttk.Label(root, text="AI Assistant Plugin", font=('Arial', 16, 'bold'))
    title_label.pack(pady=20)
    
    status_label = ttk.Label(root, text="✅ Плагин успешно установлен!", foreground="green")
    status_label.pack(pady=10)
    
    # Функции ИИ
    ai_frame = ttk.Frame(root)
    ai_frame.pack(pady=20)
    
    ttk.Button(ai_frame, text="🎤 Голосовые команды", 
              command=lambda: messagebox.showinfo("ИИ", "Голосовые команды активированы")).pack(pady=5, fill='x')
    
    ttk.Button(ai_frame, text="💬 Чат-бот", 
              command=lambda: messagebox.showinfo("ИИ", "Чат-бот запущен")).pack(pady=5, fill='x')
    
    ttk.Button(ai_frame, text="📝 Автописание", 
              command=lambda: messagebox.showinfo("ИИ", "Автоматическое описание")).pack(pady=5, fill='x')
    
    ttk.Button(root, text="❌ Выход", 
              command=root.quit).pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    ai_assistant_gui()
'''
        
        plugin_file = os.path.join(self.plugins_dir, "ai_assistant.py")
        with open(plugin_file, "w", encoding="utf-8") as f:
            f.write(ai_code)
        
        print("📁 Создан файл: ai_assistant.py")
        print("🚀 Запуск: ai-assistant")
    
    def list_installed(self):
        """Список установленных плагинов"""
        installed = []
        for file in os.listdir(self.plugins_dir):
            if file.endswith('.py'):
                installed.append(file[:-3])  # убираем .py
        
        if not installed:
            print("❌ Нет установленных плагинов")
            return
        
        print("📁 УСТАНОВЛЕННЫЕ ПЛАГИНЫ:")
        print("=" * 40)
        for plugin in installed:
            print(f"✅ {plugin}")
            bat_file = os.path.join(self.plugins_dir, f"{plugin}.bat")
            if os.path.exists(bat_file):
                print(f"   🚀 Запуск: {plugin.replace('_', '-')}")
            else:
                print(f"   🚀 Запуск: python C:\\Pytonchik\\plugins\\{plugin}.py")
            print()

def main():
    if len(sys.argv) < 2:
        print("📦 Pytonchik Plugin Manager")
        print("=" * 50)
        print("Использование:")
        print("  install-sets list                    - список плагинов")
        print("  install-sets install <plugin>        - установить плагин")
        print("  install-sets installed               - установленные плагины")
        print()
        print("Примеры:")
        print("  install-sets install youtube-plus")
        print("  install-sets install info-mods")
        print("  install-sets list")
        return
    
    manager = SimplePluginManager()
    command = sys.argv[1]
    
    if command == "list":
        manager.list_plugins()
    elif command == "install" and len(sys.argv) > 2:
        plugin_name = sys.argv[2]
        manager.install_plugin(plugin_name)
    elif command == "installed":
        manager.list_installed()
    else:
        print("❌ Неизвестная команда")
        print("📋 Используйте: install-sets list")

if __name__ == "__main__":
    main()