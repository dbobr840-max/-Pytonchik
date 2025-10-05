@echo off
chcp 65001
echo Installing Pytonchik GUI Support...
echo.

echo Step 1: Creating plugin directory...
if not exist "C:\Pytonchik\plugins" mkdir "C:\Pytonchik\plugins"

echo Step 2: Creating GUI examples...
echo Creating example GUI programs...

:: Пример 1: Простое окно
echo # simple_gui.pt - простое GUI окно
echo окно("Моя программа")
echo метка("Привет, мир!")
echo кнопка("Нажми меня")
echo показать()
> "C:\Pytonchik\plugins\simple_gui.pt"

:: Пример 2: Калькулятор
echo # calculator.pt - простой калькулятор
echo окно("Калькулятор")
echo метка("Простой калькулятор на Pytonchik")
echo кнопка("Сложение")
echo кнопка("Вычитание") 
echo кнопка("Умножение")
echo кнопка("Деление")
echo показать()
> "C:\Pytonchik\plugins\calculator.pt"

echo Step 3: Updating main interpreter...
:: Копируем обновленный файл (вы должны обновить pytonchik.py вручную)
echo Please update pytonchik.py with the new GUI code manually

echo.
echo ✅ GUI support installed!
echo.
echo Now you can create GUI programs with commands:
echo   окно("Заголовок")    - создать окно
echo   метка("Текст")       - создать текстовую метку
echo   кнопка("Текст")      - создать кнопку
echo   показать()           - показать окно
echo.
echo Examples:
echo   pt start plugins/simple_gui.pt
echo.
pause