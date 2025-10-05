@echo off
chcp 65001
echo 📦 Установка YouTube+ плагина...
echo.

echo Создаем необходимые файлы...

:: Создаем файл для API ключа
if not exist "C:\Pytonchik\youtube_api_key.txt" (
    echo ВСТАВЬТЕ_ВАШ_API_КЛЮЧ_ЗДЕСЬ > "C:\Pytonchik\youtube_api_key.txt"
    echo ✅ Создан файл для API ключа
)

:: Создаем примеры
if not exist "C:\Pytonchik\examples" mkdir "C:\Pytonchik\examples"

echo.
echo 🎬 YouTube+ плагин установлен!
echo.
echo 📝 Инструкция:
echo 1. Получите API ключ на https://console.cloud.google.com/
echo 2. Включите YouTube Data API v3
echo 3. Вставьте ключ в C:\Pytonchik\youtube_api_key.txt
echo 4. Запустите: python C:\Pytonchik\youtube_plugin.py
echo.
pause