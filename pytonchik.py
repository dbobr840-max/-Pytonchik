import os
import sys
import subprocess

def create_project(name):
    if not name:
        print("Project name required: pt create project_name")
        return
    
    project_dir = os.path.join(os.getcwd(), name)
    os.makedirs(project_dir, exist_ok=True)
    
    main_content = '''# main.pt
x = 10
y = 5
=^("Hello from Pytonchik!")
=^("x = " + str(x))
=^("y = " + str(y))
'''
    main_file = os.path.join(project_dir, "main.pt")
    with open(main_file, "w", encoding="utf-8") as f:
        f.write(main_content)
    
    print(f"Project created: {name}")
    print(f"Folder: {project_dir}")

def edit_file(filename):
    if not filename:
        print("File name required: pt edit file.pt")
        return
    
    if not filename.endswith('.pt'):
        filename += '.pt'
    
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return
    
    try:
        subprocess.run(["code", filename])
    except:
        try:
            subprocess.run(["notepad", filename])
        except:
            os.startfile(filename)

def run_file(filename):
    if not filename:
        filename = "main.pt"
    
    if not filename.endswith('.pt'):
        filename += '.pt'
    
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return
    
    print(f"Running: {filename}")
    print("=" * 40)
    
    # Simple interpreter
    variables = {}
    output = []
    
    def evaluate(expr):
        expr = str(expr).strip()
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        try: return int(expr)
        except: pass
        try: return float(expr)
        except: pass
        if expr in variables:
            return variables[expr]
        return expr
    
    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()
    
    for line in code.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        if line.startswith('=^(') and line.endswith(')'):
            content = line[3:-1].strip()
            result = evaluate(content)
            output.append(str(result))
        elif '=' in line and not line.startswith('=^'):
            parts = line.split('=', 1)
            if len(parts) == 2:
                var_name = parts[0].strip()
                value_expr = parts[1].strip()
                variables[var_name] = evaluate(value_expr)
    
    for result in output:
        print(result)
    
    print("=" * 40)

def main():
    if len(sys.argv) < 2:
        print("Pytonchik Language")
        print("Commands:")
        print("  pt start [file.pt]  - run file")
        print("  pt edit [file.pt]   - edit file")  
        print("  pt create [name]    - create project")
        return
    
    command = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) > 2 else None
    
    if command == "create":
        create_project(filename)
    elif command == "edit":
        edit_file(filename)
    elif command in ["start", "run"]:
        run_file(filename)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
    import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

class PytonchikGUI:
    def __init__(self):
        self.plugins = {}
        self.load_plugins()
    
    def load_plugins(self):
        """Загрузка плагинов"""
        plugins_dir = "C:\\Pytonchik\\plugins"
        if not os.path.exists(plugins_dir):
            os.makedirs(plugins_dir)
        
        # Автоматически загружаем GUI плагин
        self.plugins['gui'] = {
            'name': 'GUI Plugin',
            'version': '1.0',
            'commands': ['окно', 'кнопка', 'метка', 'показать']
        }
    
    def execute_gui_command(self, command, args):
        """Выполнение GUI команд"""
        if command == 'окно':
            return self.create_window(args)
        elif command == 'кнопка':
            return self.create_button(args)
        elif command == 'метка':
            return self.create_label(args)
        elif command == 'показать':
            return self.show_gui()
        return None
    
    def create_window(self, args):
        """Создание окна"""
        title = args[0] if args else "Pytonchik GUI"
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("400x300")
        self.widgets = []
        return f"Окно создано: {title}"
    
    def create_button(self, args):
        """Создание кнопки"""
        if not hasattr(self, 'root'):
            return "Сначала создайте окно: окно('Заголовок')"
        
        text = args[0] if args else "Кнопка"
        btn = tk.Button(self.root, text=text)
        btn.pack(pady=5)
        self.widgets.append(btn)
        return f"Кнопка создана: {text}"
    
    def create_label(self, args):
        """Создание метки"""
        if not hasattr(self, 'root'):
            return "Сначала создайте окно: окно('Заголовок')"
        
        text = args[0] if args else "Метка"
        label = tk.Label(self.root, text=text)
        label.pack(pady=5)
        self.widgets.append(label)
        return f"Метка создана: {text}"
    
    def show_gui(self):
        """Показать GUI"""
        if hasattr(self, 'root'):
            self.root.mainloop()
            return "GUI запущено"
        return "Сначала создайте окно"

# Добавляем в основной класс
class PytonchikInterpreter:
    def __init__(self):
        self.variables = {}
        self.output = []
        self.gui = PytonchikGUI()
    
    def execute_line(self, line):
        line = line.strip()
        if not line or line.startswith('#'):
            return None
        
        # GUI команды
        if line.startswith('окно(') or line.startswith('кнопка(') or line.startswith('метка(') or line.startswith('показать()'):
            return self.execute_gui_line(line)
        
        # Остальной код остается без изменений...
        # [предыдущий код execute_line]
    
    def execute_gui_line(self, line):
        """Выполнение GUI команд"""
        if line.startswith('окно('):
            args = self.parse_args(line[5:-1])
            result = self.gui.create_window(args)
            self.output.append(result)
        elif line.startswith('кнопка('):
            args = self.parse_args(line[6:-1])
            result = self.gui.create_button(args)
            self.output.append(result)
        elif line.startswith('метка('):
            args = self.parse_args(line[5:-1])
            result = self.gui.create_label(args)
            self.output.append(result)
        elif line == 'показать()':
            result = self.gui.show_gui()
            self.output.append(result)
        return True
    
    def parse_args(self, args_str):
        """Парсинг аргументов"""
        if not args_str:
            return []
        return [arg.strip().strip('"') for arg in args_str.split(',')]