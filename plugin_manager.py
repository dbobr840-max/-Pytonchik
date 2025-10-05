import os
import sys
import requests
import json
import zipfile
import tempfile
import shutil
from urllib.parse import urljoin
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import importlib

class PluginManager:
    def __init__(self):
        self.plugins_dir = "C:\\Pytonchik\\plugins"
        self.plugins_config = "C:\\Pytonchik\\plugins_config.json"
        self.available_plugins = self.load_plugins_config()
        
        # Создаем директории если нет
        os.makedirs(self.plugins_dir, exist_ok=True)
        
    def load_plugins_config(self):
        """Загрузка конфигурации плагинов"""
        default_plugins = {
            "youtube-plus": {
                "name": "YouTube+",
                "description": "🎬 Управление YouTube через Pytonchik",
                "version": "1.0.0",
                "author": "Pytonchik Team",
                "dependencies": ["requests", "tkinter"],
                "files": [
                    "youtube_plugin.py",
                    "youtube_pt.py", 
                    "youtube_plugin.bat"
                ],
                "github_url": "https://raw.githubusercontent.com/pytonchik/plugins/main/youtube-plus/",
                "install_command": "youtube_install.bat"
            },
            "info-mods": {
                "name": "Info+Mods", 
                "description": "🚀 200+ модификаций для Pytonchik",
                "version": "1.0.0",
                "author": "Pytonchik Team",
                "dependencies": ["psutil", "GPUtil", "pyautogui", "pygame", "speechrecognition", "qrcode", "speedtest-cli"],
                "files": [
                    "info_mods_plugin.py",
                    "info_mods_integration.py",
                    "info_mods.bat"
                ],
                "github_url": "https://raw.githubusercontent.com/pytonchik/plugins/main/info-mods/",
                "install_command": "info_mods_install.bat"
            },
            "gui-builder": {
                "name": "GUI Builder",
                "description": "🎨 Визуальный конструктор интерфейсов",
                "version": "1.0.0", 
                "author": "Pytonchik Team",
                "dependencies": ["tkinter", "PIL"],
                "files": ["gui_builder.py"],
                "github_url": "https://raw.githubusercontent.com/pytonchik/plugins/main/gui-builder/",
                "install_command": "gui_builder_install.bat"
            },
            "game-engine": {
                "name": "Game Engine",
                "description": "🎮 Движок для создания 2D игр",
                "version": "1.0.0",
                "author": "Pytonchik Team", 
                "dependencies": ["pygame", "numpy"],
                "files": ["game_engine.py"],
                "github_url": "https://raw.githubusercontent.com/pytonchik/plugins/main/game-engine/",
                "install_command": "game_engine_install.bat"
            },
            "ai-assistant": {
                "name": "AI Assistant",
                "description": "🤖 ИИ помощник с голосовым управлением",
                "version": "1.0.0",
                "author": "Pytonchik Team",
                "dependencies": ["speechrecognition", "pyttsx3", "requests"],
                "files": ["ai_assistant.py"],
                "github_url": "https://raw.githubusercontent.com/pytonchik/plugins/main/ai-assistant/",
                "install_command": "ai_assistant_install.bat"
            }
        }
        
        # Сохраняем конфиг если его нет
        if not os.path.exists(self.plugins_config):
            with open(self.plugins_config, 'w', encoding='utf-8') as f:
                json.dump(default_plugins, f, ensure_ascii=False, indent=2)
            return default_plugins
        else:
            with open(self.plugins_config, 'r', encoding='utf-8') as f:
                return json.load(f)
    
    def list_available_plugins(self):
        """Список доступных плагинов"""
        result = "📦 ДОСТУПНЫЕ ПЛАГИНЫ:\n\n"
        for plugin_id, plugin_info in self.available_plugins.items():
            result += f"🔹 {plugin_info['name']} ({plugin_id})\n"
            result += f"   📝 {plugin_info['description']}\n"
            result += f"   🏷️ Версия: {plugin_info['version']}\n"
            result += f"   👤 Автор: {plugin_info['author']}\n"
            result += f"   📥 Установка: install-sets {plugin_id}\n\n"
        return result
    
    def list_installed_plugins(self):
        """Список установленных плагинов"""
        installed = []
        for plugin_id in self.available_plugins:
            if self.is_plugin_installed(plugin_id):
                installed.append(plugin_id)
        
        if not installed:
            return "❌ Нет установленных плагинов"
        
        result = "📁 УСТАНОВЛЕННЫЕ ПЛАГИНЫ:\n\n"
        for plugin_id in installed:
            plugin_info = self.available_plugins[plugin_id]
            result += f"✅ {plugin_info['name']} ({plugin_id})\n"
            result += f"   📝 {plugin_info['description']}\n"
            result += f"   🏷️ Версия: {plugin_info['version']}\n\n"
        
        return result
    
    def is_plugin_installed(self, plugin_id):
        """Проверка установлен ли плагин"""
        if plugin_id not in self.available_plugins:
            return False
        
        plugin_info = self.available_plugins[plugin_id]
        for file in plugin_info['files']:
            file_path = os.path.join(self.plugins_dir, file)
            if not os.path.exists(file_path):
                return False
        return True
    
    def install_plugin(self, plugin_id):
        """Установка плагина"""
        if plugin_id not in self.available_plugins:
            return f"❌ Плагин '{plugin_id}' не найден"
        
        if self.is_plugin_installed(plugin_id):
            return f"✅ Плагин '{plugin_id}' уже установлен"
        
        plugin_info = self.available_plugins[plugin_id]
        results = []
        
        # Устанавливаем зависимости
        results.append(self.install_dependencies(plugin_info['dependencies']))
        
        # Скачиваем файлы плагина
        for file in plugin_info['files']:
            result = self.download_plugin_file(plugin_id, file)
            results.append(result)
        
        # Запускаем команду установки если есть
        if 'install_command' in plugin_info:
            result = self.run_install_command(plugin_id, plugin_info['install_command'])
            results.append(result)
        
        # Создаем примеры использования
        self.create_examples(plugin_id)
        
        return "\n".join(results) + f"\n\n✅ Плагин '{plugin_info['name']}' успешно установлен!"
    
    def install_dependencies(self, dependencies):
        """Установка зависимостей"""
        if not dependencies:
            return "📦 Зависимости: нет"
        
        results = ["📦 УСТАНОВКА ЗАВИСИМОСТЕЙ:"]
        for dep in dependencies:
            try:
                # Пробуем импортировать чтобы проверить установлен ли
                importlib.import_module(dep)
                results.append(f"   ✅ {dep} - уже установлен")
            except ImportError:
                try:
                    # Устанавливаем через pip
                    subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
                    results.append(f"   ✅ {dep} - установлен")
                except subprocess.CalledProcessError:
                    results.append(f"   ❌ {dep} - ошибка установки")
        
        return "\n".join(results)
    
    def download_plugin_file(self, plugin_id, filename):
        """Скачивание файла плагина"""
        plugin_info = self.available_plugins[plugin_id]
        github_url = plugin_info['github_url']
        
        # В реальной системе здесь было бы скачивание с GitHub
        # Для демо создаем файлы локально
        file_path = os.path.join(self.plugins_dir, filename)
        
        try:
            # Создаем демо-файлы плагинов
            if plugin_id == "youtube-plus":
                self.create_youtube_plugin_files()
            elif plugin_id == "info-mods":
                self.create_info_mods_files()
            elif plugin_id == "gui-builder":
                self.create_gui_builder_files()
            elif plugin_id == "game-engine":
                self.create_game_engine_files()
            elif plugin_id == "ai-assistant":
                self.create_ai_assistant_files()
            
            return f"   📥 {filename} - скачан"
        except Exception as e:
            return f"   ❌ {filename} - ошибка: {e}"
    
    def run_install_command(self, plugin_id, command):
        """Запуск команды установки"""
        try:
            if command.endswith('.bat'):
                bat_path = os.path.join(self.plugins_dir, command)
                if os.path.exists(bat_path):
                    subprocess.run(bat_path, check=True, cwd=self.plugins_dir)
                    return f"   ⚙️ {command} - выполнен"
            return f"   ⚙️ {command} - пропущен (файл не найден)"
        except Exception as e:
            return f"   ❌ {command} - ошибка: {e}"
    
    def create_examples(self, plugin_id):
        """Создание примеров использования"""
        examples_dir = os.path.join(self.plugins_dir, "examples")
        os.makedirs(examples_dir, exist_ok=True)
        
        if plugin_id == "youtube-plus":
            example_code = '''# youtube_demo.pt - демо YouTube плагина
окно("YouTube+ 🎬")
метка("=== YOUTUBE УПРАВЛЕНИЕ ===")
метка("Статистика каналов")
метка("Поиск видео") 
метка("Просмотр в программе")

кнопка("📊 Статистика канала")
кнопка("🔍 Поиск видео")
кнопка("🎬 Просмотр")
кнопка("🚀 Запуск YouTube+")
кнопка("❌ Выход")

показать()
'''
            with open(os.path.join(examples_dir, "youtube_demo.pt"), "w", encoding="utf-8") as f:
                f.write(example_code)
        
        elif plugin_id == "info-mods":
            example_code = '''# info_mods_demo.pt - демо Info+Mods
окно("Info+Mods 🚀")
метка("=== 200+ МОДИФИКАЦИЙ ===")
метка("Системный монитор")
метка("Инструменты разработчика")
метка("Развлекательные функции")

кнопка("🖥️ Системная информация")
кнопка("💻 Инструменты Dev")
кнопка("🎮 Развлечения")
кнопка("🚀 Запуск Info+Mods")
кнопка("❌ Выход")

показать()
'''
            with open(os.path.join(examples_dir, "info_mods_demo.pt"), "w", encoding="utf-8") as f:
                f.write(example_code)
    
    def uninstall_plugin(self, plugin_id):
        """Удаление плагина"""
        if plugin_id not in self.available_plugins:
            return f"❌ Плагин '{plugin_id}' не найден"
        
        if not self.is_plugin_installed(plugin_id):
            return f"❌ Плагин '{plugin_id}' не установлен"
        
        plugin_info = self.available_plugins[plugin_id]
        results = []
        
        # Удаляем файлы плагина
        for file in plugin_info['files']:
            file_path = os.path.join(self.plugins_dir, file)
            if os.path.exists(file_path):
                os.remove(file_path)
                results.append(f"   🗑️ {file} - удален")
        
        return "\n".join(results) + f"\n\n✅ Плагин '{plugin_info['name']}' удален!"
    
    def create_youtube_plugin_files(self):
        """Создание файлов YouTube плагина (демо)"""
        # Создаем основные файлы YouTube плагина
        youtube_plugin_code = """
# YouTube+ Plugin (демо версия)
print("YouTube+ плагин установлен!")
# Полный код будет скачан с GitHub
"""
        
        with open(os.path.join(self.plugins_dir, "youtube_plugin.py"), "w", encoding="utf-8") as f:
            f.write(youtube_plugin_code)
        
        # Бат-файл для установки
        bat_content = '''@echo off
echo Installing YouTube+ dependencies...
pip install requests
echo YouTube+ plugin ready!
pause
'''
        with open(os.path.join(self.plugins_dir, "youtube_plugin.bat"), "w") as f:
            f.write(bat_content)
    
    def create_info_mods_files(self):
        """Создание файлов Info+Mods плагина (демо)"""
        info_mods_code = """
# Info+Mods Plugin (демо версия) 
print("Info+Mods плагин установлен!")
# Полный код будет скачан с GitHub
"""
        
        with open(os.path.join(self.plugins_dir, "info_mods_plugin.py"), "w", encoding="utf-8") as f:
            f.write(info_mods_code)
        
        bat_content = '''@echo off
echo Installing Info+Mods dependencies...
pip install psutil GPUtil pyautogui
echo Info+Mods plugin ready!
pause
'''
        with open(os.path.join(self.plugins_dir, "info_mods.bat"), "w") as f:
            f.write(bat_content)
    
    def create_gui_builder_files(self):
        """Создание файлов GUI Builder"""
        with open(os.path.join(self.plugins_dir, "gui_builder.py"), "w", encoding="utf-8") as f:
            f.write("# GUI Builder Plugin - установлен")
    
    def create_game_engine_files(self):
        """Создание файлов Game Engine"""
        with open(os.path.join(self.plugins_dir, "game_engine.py"), "w", encoding="utf-8") as f:
            f.write("# Game Engine Plugin - установлен")
    
    def create_ai_assistant_files(self):
        """Создание файлов AI Assistant"""
        with open(os.path.join(self.plugins_dir, "ai_assistant.py"), "w", encoding="utf-8") as f:
            f.write("# AI Assistant Plugin - установлен")

class PluginManagerGUI:
    def __init__(self, root):
        self.root = root
        self.manager = PluginManager()
        self.setup_gui()
    
    def setup_gui(self):
        """Настройка графического интерфейса"""
        self.root.title("📦 Менеджер плагинов Pytonchik")
        self.root.geometry("800x600")
        
        # Вкладки
        tab_control = ttk.Notebook(self.root)
        
        # Вкладка установки
        install_tab = ttk.Frame(tab_control)
        tab_control.add(install_tab, text='📥 Установка')
        self.setup_install_tab(install_tab)
        
        # Вкладка управления
        manage_tab = ttk.Frame(tab_control)
        tab_control.add(manage_tab, text='⚙️ Управление')
        self.setup_manage_tab(manage_tab)
        
        tab_control.pack(expand=1, fill='both')
    
    def setup_install_tab(self, tab):
        """Настройка вкладки установки"""
        ttk.Label(tab, text="Доступные плагины:", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Список плагинов
        self.plugins_list = tk.Listbox(tab, height=15)
        self.plugins_list.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Заполняем список
        for plugin_id, plugin_info in self.manager.available_plugins.items():
            status = "✅" if self.manager.is_plugin_installed(plugin_id) else "📥"
            self.plugins_list.insert(tk.END, f"{status} {plugin_info['name']} ({plugin_id})")
        
        # Кнопки
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Button(btn_frame, text="Установить выбранный", 
                  command=self.install_selected).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Обновить список", 
                  command=self.refresh_list).pack(side='left', padx=5)
    
    def setup_manage_tab(self, tab):
        """Настройка вкладки управления"""
        ttk.Label(tab, text="Установленные плагины:", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Текстовая область с информацией
        self.info_text = scrolledtext.ScrolledText(tab, height=20)
        self.info_text.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Обновляем информацию
        self.update_installed_info()
    
    def install_selected(self):
        """Установка выбранного плагина"""
        selection = self.plugins_list.curselection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите плагин для установки")
            return
        
        index = selection[0]
        plugin_line = self.plugins_list.get(index)
        plugin_id = plugin_line.split('(')[1].split(')')[0]
        
        result = self.manager.install_plugin(plugin_id)
        messagebox.showinfo("Результат", result)
        self.refresh_list()
        self.update_installed_info()
    
    def refresh_list(self):
        """Обновление списка плагинов"""
        self.plugins_list.delete(0, tk.END)
        for plugin_id, plugin_info in self.manager.available_plugins.items():
            status = "✅" if self.manager.is_plugin_installed(plugin_id) else "📥"
            self.plugins_list.insert(tk.END, f"{status} {plugin_info['name']} ({plugin_id})")
    
    def update_installed_info(self):
        """Обновление информации об установленных плагинах"""
        info = self.manager.list_installed_plugins()
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, info)

def start_plugin_manager_gui():
    """Запуск графического менеджера плагинов"""
    root = tk.Tk()
    app = PluginManagerGUI(root)
    root.mainloop()

def main():
    """Основная функция для командной строки"""
    if len(sys.argv) < 2:
        print("""
📦 Менеджер плагинов Pytonchik

Использование:
  install-sets list              - список доступных плагинов
  install-sets installed         - список установленных плагинов
  install-sets install <plugin>  - установить плагин
  install-sets uninstall <plugin>- удалить плагин
  install-sets gui               - графический интерфейс

Примеры:
  install-sets install youtube-plus
  install-sets install info-mods
  install-sets list
        """)
        return
    
    command = sys.argv[1]
    manager = PluginManager()
    
    if command == "list":
        print(manager.list_available_plugins())
    elif command == "installed":
        print(manager.list_installed_plugins())
    elif command == "install" and len(sys.argv) > 2:
        plugin_id = sys.argv[2]
        print(f"📦 Установка плагина: {plugin_id}")
        print(manager.install_plugin(plugin_id))
    elif command == "uninstall" and len(sys.argv) > 2:
        plugin_id = sys.argv[2]
        print(f"🗑️ Удаление плагина: {plugin_id}")
        print(manager.uninstall_plugin(plugin_id))
    elif command == "gui":
        start_plugin_manager_gui()
    else:
        print("❌ Неизвестная команда")

if __name__ == "__main__":
    main()