@echo off
chcp 65001
echo 📦 Установка Info+Mods плагина...
echo.

echo Установка зависимостей...
pip install psutil GPUtil screeninfo pygame pyautogui pyperclip > nul 2>&1
pip install speechrecognition pyttsx3 translate qrcode python-barcode > nul 2>&1
pip install speedtest-cli geocoder timezonefinder pytz currency-converter > nul 2>&1
pip install wolframalpha newsapi-python wikipedia deep-translator emoji > nul 2>&1
pip install forex-python weathercom beautifulsoup4 pyjokes > nul 2>&1

echo.
echo ✅ Info+Mods плагин установлен!
echo.
echo 🚀 Запуск:
echo   python C:\Pytonchik\info_mods_plugin.py
echo   или
echo   C:\Pytonchik\info_mods.bat
echo.
pause