@echo off
echo [*] [3TH1C4L] MultiTool - (https://github.com/RPxGoon/3TH1C4L-MultiTool)
echo [*] Thanks for the Support :)
echo.
echo [!] Checking for Python installation...
echo.

REM Check if Python is installed and available in PATH
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python is NOT INSTALLED!
    echo.

    REM Check if winget is available
    where winget >nul 2>&1
    if errorlevel 1 (
        echo [!] winget is not available on your system. Please ensure you are running Windows 10 or 11 with winget installed.
        pause
        exit /b 1
    )

    REM Use winget to install Python silently with the correct argument
    echo [*] Installing Python via winget... Accept UAC popup in taskbar
    winget install --id Python.Python.3.11 --source winget --silent --accept-package-agreements >nul 2>&1

    REM Wait for the installation process to complete (added delay)
    timeout /t 10 /nobreak >nul

)

echo [*] Python is Installed! Checking and Installing Required Packages...
echo.
echo [!] Upgrading pip...
python -m ensurepip >nul 2>&1
python -m pip install --upgrade pip >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Restart setup.bat to finish installation 
    pause
    exit /b 1
)

echo [!] Installing Required Python Packages from requirements.txt...
python -m pip install -r requirements.txt >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Failed to Install Some Requirements! Check Your Internet Connection or requirements.txt
    pause
    exit /b 1
)

echo [*] All Required Packages Installed Successfully! :)

echo [*] Running the Main Tool (3th1c4l.py)...
start "" python "%~dp0\3th1c4l.py"

pause
