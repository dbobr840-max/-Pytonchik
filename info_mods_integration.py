import sys
import os
sys.path.append('C:\\Pytonchik')

try:
    from info_mods_plugin import MegaModsPlugin, start_info_mods
    INFO_MODS_AVAILABLE = True
except ImportError:
    INFO_MODS_AVAILABLE = False

class PytonchikInfoMods:
    def __init__(self):
        self.plugin = MegaModsPlugin() if INFO_MODS_AVAILABLE else None
        self.output = []
    
    def execute_command(self, command, args):
        """Выполнение команд Info+Mods"""
        if not INFO_MODS_AVAILABLE:
            return "❌ Плагин Info+Mods не доступен"
        
        if command == 'моды_список':
            return self.list_mods()
        elif command == 'моды_категории':
            return self.list_categories()
        elif command == 'моды_запуск':
            return self.launch_gui()
        elif command.startswith('мод_'):
            mod_name = command[4:]  # Убираем 'мод_'
            return self.run_mod(mod_name, args)
        else:
            return f"❌ Неизвестная команда: {command}"
    
    def list_mods(self):
        """Список всех модификаций"""
        if not self.plugin:
            return "❌ Плагин не загружен"
        
        result = "🚀 INFO+MODS - 200+ МОДИФИКАЦИЙ:\n\n"
        
        categories = {}
        for mod_id, mod_data in self.plugin.mods.items():
            category = mod_data['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(f"  • {mod_data['name']} (мод_{mod_id})")
        
        for category, mods in categories.items():
            result += f"📁 {category.upper()}:\n"
            result += "\n".join(mods) + "\n\n"
        
        return result
    
    def list_categories(self):
        """Список категорий"""
        categories = {
            'system': '🖥️ Системные утилиты (30+)',
            'info': '📊 Информационные (40+)', 
            'fun': '🎮 Развлекательные (30+)',
            'utils': '🛠️ Утилиты (50+)',
            'dev': '💻 Инструменты разработчика (25+)',
            'security': '🔐 Безопасность (15+)',
            'internet': '🌐 Интернет (20+)',
            'graphics': '🎨 Графические (10+)'
        }
        
        result = "📁 КАТЕГОРИИ МОДИФИКАЦИЙ:\n\n"
        for cat_id, cat_name in categories.items():
            result += f"{cat_name}\n"
        
        return result
    
    def run_mod(self, mod_name, args):
        """Запуск конкретной модификации"""
        if not self.plugin:
            return "❌ Плагин не загружен"
        
        return self.plugin.execute_mod(mod_name, *args)
    
    def launch_gui(self):
        """Запуск графического интерфейса"""
        try:
            start_info_mods()
            return "✅ Info+Mods GUI запущен"
        except Exception as e:
            return f"❌ Ошибка запуска GUI: {e}"

# Глобальный экземпляр
info_mods_manager = PytonchikInfoMods()

def info_mods_command(command, *args):
    """Функция для вызова из Pytonchik"""
    return info_mods_manager.execute_command(command, args)