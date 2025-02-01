@echo off
echo [*] [3TH1C4L] MultiTool - (https://github.com/RPxGoon/3TH1C4L-MultiTool)
echo [*] Thanks for the Support :)
echo.
echo [!] Checking for Python installation...
echo.


REM Check if Python is installed and available in PATH
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python is NOT INSTALLED! - Attempting to Install Python Silently...
    echo.


    REM Check if winget is available
    where winget >nul 2>&1
    if errorlevel 1 (
        echo [!] winget is not available on your system. Please ensure you are running Windows 10 or 11 with winget installed.
        pause
        exit /b 1
    )

    REM Use winget to install Python silently with the correct argument
    echo [*] Installing Python via winget...
    winget install --id Python.Python.3.11 --source winget --silent --accept-package-agreements --verbose-logs > install_log.txt 2>&1

    REM Wait for the installation process to complete (added delay)
    timeout /t 10 /nobreak >nul

    REM Reopen the batch file to check installation after the installation process
    echo [*] Reopening setup.bat to verify installation...
    start "" "%~f0"
    exit /b
)

echo [*] Python is Installed! Checking and Installing Required Packages...
echo.
echo [!] Upgrading pip...
python -m ensurepip >nul 2>&1
python -m pip install --upgrade pip >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Failed to Upgrade 'pip'. Ensure Python is Properly Installed.
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

echo [*] Setup Complete! The Main Tool Will Now Open Automatically...
pause
