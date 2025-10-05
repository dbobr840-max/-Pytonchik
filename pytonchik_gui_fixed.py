import os
import sys
import tkinter as tk
from tkinter import messagebox
import subprocess

class PytonchikGUIInterpreter:
    def __init__(self):
        self.variables = {}
        self.output = []
        self.root = None
        self.widgets = []
    
    def evaluate(self, expr):
        """Вычисление выражений"""
        if not expr:
            return ""
        expr = str(expr).strip()
        
        # Строки
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        
        # Числа
        try: return int(expr)
        except: pass
        try: return float(expr)
        except: pass
        
        # Переменные
        if expr in self.variables:
            return self.variables[expr]
            
        return expr
    
    def execute_line(self, line):
        """Выполнение одной строки кода"""
        line = line.strip()
        if not line or line.startswith('#'):
            return None
        
        # GUI команды
        if line.startswith('окно(') and line.endswith(')'):
            title = line[5:-1].strip('"')
            self.create_window(title)
            self.output.append(f"✅ Окно создано: {title}")
            return True
            
        elif line.startswith('метка(') and line.endswith(')'):
            text = line[6:-1].strip('"')
            self.create_label(text)
            self.output.append(f"✅ Метка создана: {text}")
            return True
            
        elif line.startswith('кнопка(') and line.endswith(')'):
            text = line[7:-1].strip('"')
            self.create_button(text)
            self.output.append(f"✅ Кнопка создана: {text}")
            return True
            
        elif line == 'показать()':
            if self.root:
                self.output.append("🎨 Запускается графический интерфейс...")
            else:
                self.output.append("❌ Сначала создайте окно: окно('Заголовок')")
            return True
        
        # Обычные команды Pytonchik
        elif line.startswith('=^(') and line.endswith(')'):
            content = line[3:-1].strip()
            result = self.evaluate(content)
            self.output.append(str(result))
            return True
        
        elif ' = ' in line:
            parts = line.split(' = ', 1)
            if len(parts) == 2:
                var_name = parts[0].strip()
                value_expr = parts[1].strip()
                self.variables[var_name] = self.evaluate(value_expr)
                self.output.append(f"📦 Переменная {var_name} = {self.variables[var_name]}")
                return True
        
        return False
    
    def create_window(self, title="Pytonchik GUI"):
        """Создает главное окно"""
        if self.root:
            self.root.destroy()
            
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("500x400")
        self.root.configure(bg='lightblue')
        self.widgets = []
        
        # Заголовок
        title_label = tk.Label(self.root, text=title, 
                              font=("Arial", 16, "bold"), 
                              bg='lightblue', fg='darkblue')
        title_label.pack(pady=15)
        self.widgets.append(title_label)
    
    def create_label(self, text):
        """Создает текстовую метку"""
        if not self.root:
            self.create_window("Pytonchik GUI")
            
        label = tk.Label(self.root, text=text, 
                        font=("Arial", 11),
                        bg='lightblue')
        label.pack(pady=8)
        self.widgets.append(label)
    
    def create_button(self, text):
        """Создает кнопку"""
        if not self.root:
            self.create_window("Pytonchik GUI")
            
        button = tk.Button(self.root, text=text, 
                          font=("Arial", 10, "bold"),
                          bg='lightgreen',
                          command=lambda: self.button_click(text))
        button.pack(pady=10, padx=20, fill='x')
        self.widgets.append(button)
    
    def button_click(self, button_text):
        """Обработчик нажатия кнопки"""
        messagebox.showinfo("Pytonchik GUI", f"Вы нажали: {button_text}")
    
    def show_gui(self):
        """Показывает GUI"""
        if self.root:
            self.root.mainloop()
    
    def run(self, code):
        """Запускает код"""
        lines = code.split('\n')
        
        for line in lines:
            self.execute_line(line)
        
        return self.output

def run_pt_file(filename):
    """Запускает .pt файл"""
    if not filename.endswith('.pt'):
        filename += '.pt'
    
    if not os.path.exists(filename):
        print(f"❌ Файл не найден: {filename}")
        return False
    
    print(f"🚀 Запускаем: {filename}")
    print("=" * 50)
    
    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()
    
    interpreter = PytonchikGUIInterpreter()
    results = interpreter.run(code)
    
    # Выводим результаты выполнения
    for result in results:
        print(result)
    
    print("=" * 50)
    
    # Запускаем GUI если есть окно
    if interpreter.root:
        print("🎨 Запускается графическое окно...")
        print("ℹ️  Закройте окно чтобы завершить программу")
        interpreter.show_gui()
    else:
        print("✅ Программа завершена (без GUI)")
    
    return True

def create_example():
    """Создает рабочий пример"""
    example_code = '''# Рабочий пример GUI программы
окно("Моя первая программа на Pytonchik")
метка("Добро пожаловать!")
метка("Это графический интерфейс")
метка("Создано на языке Pytonchik")
кнопка("Приветствие")
кнопка("Информация")
кнопка("Тестовая кнопка")
показать()
'''
    
    with open("working_example.pt", "w", encoding="utf-8") as f:
        f.write(example_code)
    
    print("✅ Создан рабочий пример: working_example.pt")
    return "working_example.pt"

def create_project(name):
    """Создает новый проект"""
    os.makedirs(name, exist_ok=True)
    
    project_code = f'''# main.pt - проект {name}
окно("Программа {name}")
метка("Добро пожаловать в {name}")
метка("Это ваша первая GUI программа")
кнопка("Старт")
кнопка("Настройки")
кнопка("Выход")
показать()
'''
    
    with open(f"{name}/main.pt", "w", encoding="utf-8") as f:
        f.write(project_code)
    
    print(f"✅ Создан проект: {name}")
    print(f"📁 Папка: {name}")
    print(f"📄 Файл: {name}/main.pt")
    return f"{name}/main.pt"

def main():
    if len(sys.argv) < 2:
        print("🐍 Pytonchik GUI System")
        print("=" * 30)
        print("Команды:")
        print("  run <file.pt>     - запустить файл")
        print("  example           - создать пример")
        print("  create <name>     - создать проект")
        print("  test              - тестовый запуск")
        print()
        print("Пример:")
        print("  python pytonchik_gui_fixed.py run working_example.pt")
        return
    
    command = sys.argv[1]
    
    if command == "run":
        filename = sys.argv[2] if len(sys.argv) > 2 else "main.pt"
        run_pt_file(filename)
        
    elif command == "example":
        filename = create_example()
        print(f"📝 Запустите: python pytonchik_gui_fixed.py run {filename}")
        
    elif command == "create":
        name = sys.argv[2] if len(sys.argv) > 2 else "my_gui_app"
        filename = create_project(name)
        print(f"📝 Запустите: python pytonchik_gui_fixed.py run {filename}")
        
    elif command == "test":
        # Автоматический тест
        test_code = '''# Тестовый код
окно("Тест Pytonchik GUI")
метка("Тест прошел успешно!")
метка("GUI работает корректно")
кнопка("Тестовая кнопка")
показать()
'''
        print("🧪 Запускаем тест...")
        interpreter = PytonchikGUIInterpreter()
        results = interpreter.run(test_code)
        
        for result in results:
            print(result)
            
        if interpreter.root:
            print("🎉 Тест пройден! Запускается GUI...")
            interpreter.show_gui()
        else:
            print("❌ Тест не пройден")
            
    else:
        print(f"❌ Неизвестная команда: {command}")

if __name__ == "__main__":
    main()