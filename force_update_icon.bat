@echo off
echo Force updating .pt file icons...
echo.

:: Удаляем старую регистрацию
reg delete "HKEY_CLASSES_ROOT\.pt" /f >nul 2>&1
reg delete "HKEY_CLASSES_ROOT\Pytonchik.File" /f >nul 2>&1

:: Ждем
timeout /t 2 /nobreak >nul

:: Регистрируем заново
reg add "HKEY_CLASSES_ROOT\.pt" /ve /d "Pytonchik.File" /f
reg add "HKEY_CLASSES_ROOT\Pytonchik.File" /ve /d "Pytonchik Script" /f
reg add "HKEY_CLASSES_ROOT\Pytonchik.File\DefaultIcon" /ve /d "C:\Pytonchik\snake.ico,0" /f
reg add "HKEY_CLASSES_ROOT\Pytonchik.File\Shell\Open\Command" /ve /d "wscript.exe \"C:\Pytonchik\open_pt_simple.vbs\" \"%%1\"" /f

echo Registry updated!

:: Очищаем кэш иконок
echo Clearing icon cache...
taskkill /f /im explorer.exe >nul 2>&1

:: Удаляем файлы кэша
del /f /q "%localappdata%\IconCache.db" >nul 2>&1
del /f /q "%localappdata%\Microsoft\Windows\Explorer\iconcache*" >nul 2>&1

:: Перезапускаем Explorer
start explorer.exe

echo.
echo Icon cache cleared and Explorer restarted!
echo Please check your .pt files now.
echo.
pause