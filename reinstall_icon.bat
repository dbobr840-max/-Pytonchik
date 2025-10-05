@echo off
echo === COMPLETE Icon Reinstall ===
echo.

echo Step 1: Kill Explorer...
taskkill /f /im explorer.exe >nul 2>&1
timeout /t 1 /nobreak >nul

echo Step 2: Clean old registration...
reg delete "HKEY_CLASSES_ROOT\.pt" /f >nul 2>&1
reg delete "HKEY_CLASSES_ROOT\Pytonchik.File" /f >nul 2>&1

echo Step 3: Wait...
timeout /t 2 /nobreak >nul

echo Step 4: Register .pt extension...
reg add "HKEY_CLASSES_ROOT\.pt" /ve /d "Pytonchik.File" /f

echo Step 5: Register file type...
reg add "HKEY_CLASSES_ROOT\Pytonchik.File" /ve /d "Pytonchik Script" /f

echo Step 6: Set icon...
reg add "HKEY_CLASSES_ROOT\Pytonchik.File" /v "AlwaysShowExt" /t REG_SZ /d "" /f
reg add "HKEY_CLASSES_ROOT\Pytonchik.File" /v "EditFlags" /t REG_DWORD /d 1 /f
reg add "HKEY_CLASSES_ROOT\Pytonchik.File\DefaultIcon" /ve /d "C:\Pytonchik\snake.ico,0" /f

echo Step 7: Set open command...
reg add "HKEY_CLASSES_ROOT\Pytonchik.File\Shell\Open\Command" /ve /d "wscript.exe \"C:\Pytonchik\open_pt_simple.vbs\" \"%%1\"" /f

echo Step 8: Clear icon cache...
del /f /q "%localappdata%\IconCache.db" >nul 2>&1
del /f /q "%localappdata%\Microsoft\Windows\Explorer\iconcache_*.db" >nul 2>&1
del /f /q "%localappdata%\Microsoft\Windows\Explorer\thumbcache_*.db" >nul 2>&1

echo Step 9: Restart Explorer...
start explorer.exe

echo Step 10: Wait for cache rebuild...
timeout /t 3 /nobreak >nul

echo.
echo ✅ COMPLETE! Icon should be updated.
echo Please check any .pt file or create a new one.
echo.
pause