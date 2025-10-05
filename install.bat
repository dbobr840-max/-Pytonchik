@echo off
echo Installing Pytonchik...

:: Copy to System32
echo Step 1: Installing pt command...
copy "C:\Pytonchik\pt.bat" "C:\Windows\System32\" > nul 2>&1

if errorlevel 1 (
    echo @echo off > "C:\Windows\System32\pt.bat"
    echo python "C:\Pytonchik\pytonchik.py" %%* >> "C:\Windows\System32\pt.bat"
)

:: Register file association
echo Step 2: Registering .pt files...
reg add "HKEY_CLASSES_ROOT\.pt" /ve /d "Pytonchik.File" /f > nul 2>&1
reg add "HKEY_CLASSES_ROOT\Pytonchik.File" /ve /d "Pytonchik Script" /f > nul 2>&1
reg add "HKEY_CLASSES_ROOT\Pytonchik.File\Shell\Open\Command" /ve /d "wscript.exe \"C:\Pytonchik\open_pt_simple.vbs\" \"%%1\"" /f > nul 2>&1

echo.
echo SUCCESS: Pytonchik installed!
echo.
echo Commands:
echo   pt start [file.pt]  - run file
echo   pt edit [file.pt]   - edit file
echo   pt create [name]    - create project
echo.
pause