@echo off
echo === Debug Icon Information ===
echo.

echo 1. Checking .pt registration:
reg query "HKEY_CLASSES_ROOT\.pt" /ve
echo.

echo 2. Checking Pytonchik.File class:
reg query "HKEY_CLASSES_ROOT\Pytonchik.File" /ve
echo.

echo 3. Checking icon path:
reg query "HKEY_CLASSES_ROOT\Pytonchik.File\DefaultIcon" /ve 2>nul
if %errorlevel% neq 0 echo DefaultIcon key not found!
echo.

echo 4. Checking if icon file exists:
if exist "C:\Pytonchik\snake.ico" (
    echo Icon file EXISTS: C:\Pytonchik\snake.ico
) else (
    echo Icon file NOT FOUND: C:\Pytonchik\snake.ico
)
echo.

echo 5. Current directory:
dir "C:\Pytonchik\snake.*"
echo.

pause