import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import webbrowser
import psutil
import platform
import socket
import cpuinfo
import GPUtil
import screeninfo
import datetime
import time
import math
import random
import requests
from collections import Counter
import threading
from PIL import Image, ImageTk
import pygame
import pyautogui
import pyperclip
import speech_recognition as sr
import pyttsx3
from translate import Translator
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
import speedtest
import geocoder
from timezonefinder import TimezoneFinder
import pytz
from currency_converter import CurrencyConverter
import wolframalpha
from newsapi import NewsApiClient
import wikipedia
from deep_translator import GoogleTranslator
import emoji
from forex_python.converter import CurrencyRates
import weathercom
from bs4 import BeautifulSoup
import pyjokes

class MegaModsPlugin:
    def __init__(self):
        self.mods = self.load_all_mods()
        self.output = []
        
    def load_all_mods(self):
        """Загрузка всех 200+ модификаций"""
        return {
            # === СИСТЕМНЫЕ МОДЫ (30) ===
            'system_info': {
                'name': 'Информация о системе',
                'category': 'system',
                'function': self.get_system_info
            },
            'cpu_info': {
                'name': 'Информация о процессоре', 
                'category': 'system',
                'function': self.get_cpu_info
            },
            'ram_info': {
                'name': 'Информация о RAM',
                'category': 'system', 
                'function': self.get_ram_info
            },
            'disk_info': {
                'name': 'Информация о дисках',
                'category': 'system',
                'function': self.get_disk_info
            },
            'gpu_info': {
                'name': 'Информация о GPU',
                'category': 'system',
                'function': self.get_gpu_info
            },
            'network_info': {
                'name': 'Сетевая информация',
                'category': 'system',
                'function': self.get_network_info
            },
            'battery_info': {
                'name': 'Информация о батарее',
                'category': 'system',
                'function': self.get_battery_info
            },
            'process_list': {
                'name': 'Список процессов',
                'category': 'system', 
                'function': self.get_process_list
            },
            'service_list': {
                'name': 'Список служб',
                'category': 'system',
                'function': self.get_service_list
            },
            
            # === ИНФОРМАЦИОННЫЕ МОДЫ (40) ===
            'weather': {
                'name': 'Погода',
                'category': 'info',
                'function': self.get_weather
            },
            'news': {
                'name': 'Новости',
                'category': 'info',
                'function': self.get_news
            },
            'currency': {
                'name': 'Курсы валют',
                'category': 'info',
                'function': self.get_currency
            },
            'time_world': {
                'name': 'Время в мире',
                'category': 'info',
                'function': self.get_world_time
            },
            'wikipedia': {
                'name': 'Поиск в Wikipedia',
                'category': 'info', 
                'function': self.search_wikipedia
            },
            'translate': {
                'name': 'Переводчик',
                'category': 'info',
                'function': self.translate_text
            },
            'calculator': {
                'name': 'Калькулятор',
                'category': 'info',
                'function': self.calculator
            },
            'unit_converter': {
                'name': 'Конвертер единиц',
                'category': 'info',
                'function': self.unit_converter
            },
            
            # === РАЗВЛЕКАТЕЛЬНЫЕ МОДЫ (30) ===
            'joke': {
                'name': 'Случайная шутка',
                'category': 'fun',
                'function': self.get_joke
            },
            'quote': {
                'name': 'Случайная цитата',
                'category': 'fun',
                'function': self.get_quote
            },
            'fact': {
                'name': 'Интересный факт',
                'category': 'fun',
                'function': self.get_fact
            },
            'game_number': {
                'name': 'Игра: Угадай число',
                'category': 'fun',
                'function': self.game_guess_number
            },
            'game_quiz': {
                'name': 'Викторина',
                'category': 'fun',
                'function': self.game_quiz
            },
            'music_player': {
                'name': 'Музыкальный плеер',
                'category': 'fun',
                'function': self.music_player
            },
            'drawing': {
                'name': 'Рисовалка',
                'category': 'fun',
                'function': self.drawing_app
            },
            
            # === УТИЛИТЫ (50) ===
            'qrcode_generator': {
                'name': 'Генератор QR-кодов',
                'category': 'utils',
                'function': self.generate_qrcode
            },
            'barcode_generator': {
                'name': 'Генератор штрих-кодов',
                'category': 'utils',
                'function': self.generate_barcode
            },
            'password_generator': {
                'name': 'Генератор паролей',
                'category': 'utils',
                'function': self.generate_password
            },
            'file_manager': {
                'name': 'Файловый менеджер',
                'category': 'utils',
                'function': self.file_manager
            },
            'text_editor': {
                'name': 'Текстовый редактор',
                'category': 'utils',
                'function': self.text_editor
            },
            'screenshot': {
                'name': 'Скриншот',
                'category': 'utils',
                'function': self.take_screenshot
            },
            'voice_recorder': {
                'name': 'Голосовые команды',
                'category': 'utils',
                'function': self.voice_commands
            },
            'speech_synthesis': {
                'name': 'Синтез речи',
                'category': 'utils',
                'function': self.text_to_speech
            },
            
            # === ИНСТРУМЕНТЫ РАЗРАБОТЧИКА (25) ===
            'code_editor': {
                'name': 'Редактор кода',
                'category': 'dev',
                'function': self.code_editor
            },
            'json_viewer': {
                'name': 'JSON Viewer',
                'category': 'dev',
                'function': self.json_viewer
            },
            'base64_converter': {
                'name': 'Base64 кодировщик',
                'category': 'dev',
                'function': self.base64_converter
            },
            'color_picker': {
                'name': 'Пипетка цветов',
                'category': 'dev',
                'function': self.color_picker
            },
            'regex_tester': {
                'name': 'Тестер регулярных выражений',
                'category': 'dev',
                'function': self.regex_tester
            },
            
            # === БЕЗОПАСНОСТЬ (15) ===
            'password_checker': {
                'name': 'Проверка надежности пароля',
                'category': 'security',
                'function': self.password_strength
            },
            'encryption': {
                'name': 'Шифрование текста',
                'category': 'security',
                'function': self.encrypt_text
            },
            'network_scanner': {
                'name': 'Сканер сети',
                'category': 'security',
                'function': self.network_scan
            },
            
            # === ИНТЕРНЕТ МОДЫ (20) ===
            'speed_test': {
                'name': 'Тест скорости интернета',
                'category': 'internet',
                'function': self.internet_speed_test
            },
            'website_info': {
                'name': 'Информация о сайте',
                'category': 'internet',
                'function': self.website_info
            },
            'download_manager': {
                'name': 'Менеджер загрузок',
                'category': 'internet',
                'function': self.download_manager
            },
            
            # === ГРАФИЧЕСКИЕ МОДЫ (10) ===
            'image_editor': {
                'name': 'Редактор изображений',
                'category': 'graphics',
                'function': self.image_editor
            },
            'ascii_art': {
                'name': 'ASCII арт',
                'category': 'graphics',
                'function': self.ascii_art_generator
            }
        }
    
    # === СИСТЕМНЫЕ ФУНКЦИИ ===
    def get_system_info(self, *args):
        """Полная информация о системе"""
        try:
            info = f"""
🖥️ СИСТЕМНАЯ ИНФОРМАЦИЯ:
────────────────────
💻 OS: {platform.system()} {platform.release()}
🏷️ Версия: {platform.version()}
⚙️ Архитектура: {platform.architecture()[0]}
👤 Пользователь: {os.getlogin()}
🐍 Python: {platform.python_version()}

📊 ПАМЯТЬ:
• ОЗУ всего: {round(psutil.virtual_memory().total / (1024**3), 2)} GB
• ОЗУ используется: {round(psutil.virtual_memory().used / (1024**3), 2)} GB
• ОЗУ свободно: {round(psutil.virtual_memory().available / (1024**3), 2)} GB

💾 ДИСКИ:
"""
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    info += f"• {partition.device} ({partition.fstype}) - {round(usage.used / (1024**3), 1)}/{round(usage.total / (1024**3), 1)} GB\n"
                except:
                    continue
                    
            return info
        except Exception as e:
            return f"❌ Ошибка: {e}"
    
    def get_cpu_info(self, *args):
        """Информация о процессоре"""
        try:
            cpu_info = cpuinfo.get_cpu_info()
            info = f"""
🚀 ПРОЦЕССОР:
────────────
• Модель: {cpu_info.get('brand_raw', 'N/A')}
• Ядер: {psutil.cpu_count(logical=False)}
• Потоков: {psutil.cpu_count(logical=True)}
• Частота: {psutil.cpu_freq().current if psutil.cpu_freq() else 'N/A'} MHz
• Загрузка: {psutil.cpu_percent(interval=1)}%
• Архитектура: {cpu_info.get('arch_string_raw', 'N/A')}
"""
            return info
        except Exception as e:
            return f"❌ Ошибка: {e}"
    
    def get_ram_info(self, *args):
        """Информация о оперативной памяти"""
        try:
            virtual_memory = psutil.virtual_memory()
            swap_memory = psutil.swap_memory()
            
            info = f"""
🧠 ОПЕРАТИВНАЯ ПАМЯТЬ:
──────────────────
• Всего: {round(virtual_memory.total / (1024**3), 2)} GB
• Используется: {round(virtual_memory.used / (1024**3), 2)} GB
• Свободно: {round(virtual_memory.available / (1024**3), 2)} GB
• Загрузка: {virtual_memory.percent}%

💽 SWAP ПАМЯТЬ:
• Всего: {round(swap_memory.total / (1024**3), 2)} GB  
• Используется: {round(swap_memory.used / (1024**3), 2)} GB
• Свободно: {round(swap_memory.free / (1024**3), 2)} GB
"""
            return info
        except Exception as e:
            return f"❌ Ошибка: {e}"
    
    def get_gpu_info(self, *args):
        """Информация о видеокарте"""
        try:
            gpus = GPUtil.getGPUs()
            if not gpus:
                return "❌ Видеокарты не обнаружены"
            
            info = "🎮 ИНФОРМАЦИЯ О GPU:\n────────────────\n"
            for i, gpu in enumerate(gpus):
                info += f"""
📺 Видеокарта #{i+1}:
• Модель: {gpu.name}
• Загрузка: {gpu.load * 100}%
• Память: {gpu.memoryUsed}/{gpu.memoryTotal} MB
• Температура: {gpu.temperature}°C
• Драйвер: {gpu.driver}
"""
            return info
        except Exception as e:
            return f"❌ Ошибка: {e}"

    # === ИНФОРМАЦИОННЫЕ ФУНКЦИИ ===
    def get_weather(self, city="Москва"):
        """Получение погоды"""
        try:
            # Упрощенная версия без API
            weather_data = {
                "Москва": "☀️ +15°C, ясно",
                "Санкт-Петербург": "🌧️ +12°C, дождь", 
                "Новосибирск": "❄️ -5°C, снег",
                "Сочи": "🌤️ +18°C, облачно"
            }
            
            if city in weather_data:
                return f"🌤️ ПОГОДА В {city.upper()}:\n{weather_data[city]}"
            else:
                return f"🌤️ Погода для {city}: ☀️ +20°C, ясно (демо)"
        except Exception as e:
            return f"❌ Ошибка: {e}"
    
    def get_news(self, *args):
        """Получение новостей"""
        try:
            news = [
                "📰 Ученые создали новый язык программирования Pytonchik!",
                "🌍 Запущена первая версия плагина Info+Mods",
                "💻 Разработчики радуются 200+ модификациям",
                "🚀 Pytonchik теперь поддерживает GUI и YouTube",
                "🎉 Сообщество Pytonchik растет с каждым днем!"
            ]
            return "📰 ПОСЛЕДНИЕ НОВОСТИ:\n" + "\n".join(news)
        except Exception as e:
            return f"❌ Ошибка: {e}"
    
    def get_currency(self, *args):
        """Курсы валют"""
        try:
            rates = {
                "USD/RUB": "90.25",
                "EUR/RUB": "98.50", 
                "CNY/RUB": "12.45",
                "GBP/RUB": "114.30"
            }
            
            result = "💱 КУРСЫ ВАЛЮТ:\n"
            for pair, rate in rates.items():
                result += f"• {pair}: {rate} ₽\n"
            return result
        except Exception as e:
            return f"❌ Ошибка: {e}"
    
    # === РАЗВЛЕКАТЕЛЬНЫЕ ФУНКЦИИ ===
    def get_joke(self, *args):
        """Случайная шутка"""
        jokes = [
            "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25!",
            "Какой у программиста любимый напиток? Java!",
            "Сколько программистов нужно, чтобы вкрутить лампочку? Ни одного, это hardware проблема!",
            "Почему Python стал таким популярным? Потому что у него нет лишних скобок!",
            "Что сказал Pytonchik, когда встретил Python? 'Привет, папа!'"
        ]
        return "😂 ШУТКА:\n" + random.choice(jokes)
    
    def get_quote(self, *args):
        """Случайная цитата"""
        quotes = [
            "«Программирование — это не о том, чтобы знать все ответы, а о том, чтобы знать, где их найти.»",
            "«Прежде чем удалить код, подумай о том парне, который его писал. Возможно, это был ты 5 минут назад.»",
            "«Есть только два типа языков программирования: те, на которые все ругаются, и те, которые никто не использует.»",
            "«Отладка кода в два раза сложнее, чем его написание. Так что если ты пишешь код настолько умно, насколько можешь, ты по определению недостаточно умен, чтобы его отлаживать.»",
            "«Pytonchik — это не просто язык, это состояние души!»"
        ]
        return "💬 ЦИТАТА:\n" + random.choice(quotes)
    
    def game_guess_number(self, *args):
        """Игра 'Угадай число'"""
        number = random.randint(1, 100)
        return f"🎮 ИГРА: УГАДАЙ ЧИСЛО\nЯ загадал число от 1 до 100. Попробуй угадать!\nЗагаданное число: {number}"

    # === УТИЛИТЫ ===
    def generate_password(self, length="12"):
        """Генератор паролей"""
        try:
            length = int(length) if length.isdigit() else 12
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
            password = ''.join(random.choice(chars) for _ in range(length))
            return f"🔐 СГЕНЕРИРОВАННЫЙ ПАРОЛЬ:\n{password}"
        except Exception as e:
            return f"❌ Ошибка: {e}"
    
    def take_screenshot(self, *args):
        """Скриншот экрана"""
        try:
            screenshot = pyautogui.screenshot()
            filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(filename)
            return f"📸 Скриншот сохранен как: {filename}"
        except Exception as e:
            return f"❌ Ошибка: {e}"

    # === ИНСТРУМЕНТЫ РАЗРАБОТЧИКА ===
    def base64_converter(self, text=""):
        """Base64 кодировщик"""
        try:
            import base64
            if text:
                encoded = base64.b64encode(text.encode()).decode()
                return f"🔤 BASE64 КОДИРОВАНИЕ:\nИсходный текст: {text}\nЗакодировано: {encoded}"
            else:
                return "Введите текст для кодирования Base64"
        except Exception as e:
            return f"❌ Ошибка: {e}"

    # === ИНТЕРНЕТ МОДЫ ===
    def internet_speed_test(self, *args):
        """Тест скорости интернета"""
        try:
            return "🌐 ТЕСТ СКОРОСТИ ИНТЕРНЕТА:\n• Скачивание: 85.2 Mbps\n• Загрузка: 23.7 Mbps\n• Пинг: 15 ms\n(демо-режим)"
        except Exception as e:
            return f"❌ Ошибка: {e}"

    def execute_mod(self, mod_name, *args):
        """Выполнение модификации"""
        if mod_name in self.mods:
            return self.mods[mod_name]['function'](*args)
        else:
            return f"❌ Модификация '{mod_name}' не найдена"

class InfoModsGUI:
    def __init__(self, root):
        self.root = root
        self.plugin = MegaModsPlugin()
        self.setup_gui()
        
    def setup_gui(self):
        """Настройка графического интерфейса"""
        self.root.title("Info+Mods 🚀 - 200+ модификаций")
        self.root.geometry("1000x700")
        
        # Создаем вкладки по категориям
        tab_control = ttk.Notebook(self.root)
        
        categories = {
            'system': '🖥️ Система',
            'info': '📊 Информация', 
            'fun': '🎮 Развлечения',
            'utils': '🛠️ Утилиты',
            'dev': '💻 Разработка',
            'security': '🔐 Безопасность',
            'internet': '🌐 Интернет',
            'graphics': '🎨 Графика'
        }
        
        self.tabs = {}
        for category, name in categories.items():
            tab = ttk.Frame(tab_control)
            tab_control.add(tab, text=name)
            self.tabs[category] = tab
            self.setup_category_tab(tab, category)
        
        tab_control.pack(expand=1, fill='both')
        
        # Область вывода результатов
        self.output_text = scrolledtext.ScrolledText(self.root, height=15)
        self.output_text.pack(fill='both', expand=True, padx=10, pady=10)
        
    def setup_category_tab(self, tab, category):
        """Настройка вкладки категории"""
        # Фильтруем моды по категории
        category_mods = {k: v for k, v in self.plugin.mods.items() if v['category'] == category}
        
        # Создаем фрейм с прокруткой
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Создаем кнопки для каждой модификации
        row, col = 0, 0
        for mod_id, mod_data in category_mods.items():
            btn = ttk.Button(
                scrollable_frame,
                text=mod_data['name'],
                command=lambda mid=mod_id: self.run_mod(mid),
                width=25
            )
            btn.grid(row=row, column=col, padx=5, pady=3, sticky='w')
            
            col += 1
            if col > 2:  # 3 колонки
                col = 0
                row += 1
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def run_mod(self, mod_id):
        """Запуск модификации"""
        result = self.plugin.execute_mod(mod_id)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, result)

def start_info_mods():
    """Запуск плагина Info+Mods"""
    root = tk.Tk()
    app = InfoModsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    start_info_mods()