@echo off
chcp 65001
echo Pytonchik GUI Setup
echo.

echo This will install GUI support for Pytonchik
echo.

:: Проверяем Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python first
    pause
    exit /b 1
)

:: Проверяем tkinter
python -c "import tkinter; print('tkinter OK')" >nul 2>&1
if errorlevel 1 (
    echo ERROR: tkinter not available!
    echo On Windows, tkinter is usually included with Python
    echo On other systems: sudo apt-get install python3-tk
    pause
    exit /b 1
)

:: Устанавливаем
echo Installing GUI support...
call "C:\Pytonchik\install_gui.bat"

echo.
echo 🎨 GUI support ready!
echo Create your first GUI program:
echo.
echo   pt create my_gui_app
echo   cd my_gui_app
echo   pt edit main.pt
echo.
echo Then add GUI commands to main.pt
pause