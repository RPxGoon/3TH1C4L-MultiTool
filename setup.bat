@echo off
echo [*] [3TH1C4L] MultiTool - (https://github.com/RPxGoon/3TH1C4L-MultiTool)
echo [*] Thanks for the Support :)
echo [!] Checking for Python installation...

python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python is NOT INSTALLED! - Checking System Architecture...
    
    set "PYTHON_VERSION=3.11.5"
    set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%"
    
    for /f "tokens=2 delims==" %%a in ('wmic os get osarchitecture /value 2^>nul') do set "ARCH=%%a"
    
    if /i "%ARCH%"=="64-bit" (
        set "PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe"
    ) else (
        set "PYTHON_INSTALLER=python-%PYTHON_VERSION%-32.exe"
    )
    
    echo [!] Downloading %PYTHON_INSTALLER%...
    powershell -Command "Invoke-WebRequest -Uri %PYTHON_URL%/%PYTHON_INSTALLER% -OutFile python_installer.exe"
    
    if not exist python_installer.exe (
        echo [!] Failed to Download Python Installer. Check Your Internet Connection or Try Again.
        pause
        exit /b 1
    )
    
    echo [!] Installing Python. Please Wait...
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 > installation_log.txt 2>&1
    
    if %errorlevel% neq 0 (
        echo [!] Python Installation Failed. Check installation_log.txt for Details.
        pause
        exit /b 1
    )
    
    del python_installer.exe
    echo [*] Python Installed Successfully! :]
) else (
    echo [*] Python is Already Installed! :]
)

echo [!] Upgrading pip...
python -m ensurepip >nul 2>&1
python -m pip install --upgrade pip >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Failed to Upgrade pip. Ensure Python is Properly Installed.
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

echo [*] Setup Complete! Press Enter to Close this Window and Open the Main Tool. You Can Now Run the Tool Using '3th1c4l.bat' or '3th1c4l.py'.
pause

start "" "%~dp0\3th1c4l.bat"
