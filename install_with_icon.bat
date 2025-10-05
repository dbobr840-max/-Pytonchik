@echo off
chcp 65001
echo Installing Pytonchik with Snake Icon...
echo.

:: Check if icon exists, if not download a sample
if not exist "C:\Pytonchik\snake.ico" (
    echo Downloading snake icon...
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://cdn.icon-icons.com/icons2/195/IconPNG/32/snake_23849.png', 'C:\Pytonchik\snake.png')"
    if exist "C:\Pytonchik\snake.png" (
        echo Convert PNG to ICO...
        powershell -Command "Add-Type -AssemblyName System.Drawing; [System.Drawing.Bitmap]::new('C:\Pytonchik\snake.png').Save('C:\Pytonchik\snake.ico', [System.Drawing.Imaging.ImageFormat]::Icon)"
        del "C:\Pytonchik\snake.png"
    ) else (
        echo Using default icon...
        echo Creating simple icon...
        powershell -Command "[Reflection.Assembly]::LoadWithPartialName('System.Drawing'); [Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); $bmp = New-Object Drawing.Bitmap(32,32); $g = [Drawing.Graphics]::FromImage($bmp); $g.Clear([Drawing.Color]::FromArgb(0,255,0)); $g.DrawString('PT', (New-Object Drawing.Font('Arial',12)), (New-Object Drawing.SolidBrush([Drawing.Color]::Black)), 8, 8); $bmp.Save('C:\Pytonchik\snake.ico', [Drawing.Imaging.ImageFormat]::Icon)"
    )
)

:: Register with icon
echo Registering .pt files with snake icon...
regedit /s "C:\Pytonchik\register_with_icon.reg"

echo.
echo ✅ Pytonchik installed with snake icon!
echo.
echo Now .pt files will have a snake icon
echo.
pause