@echo off
echo [*] Checking for Python installation...

python --version >nul 2>&1
if errorlevel 1 (
    echo [*] Python is not installed. Downloading and installing Python...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe -OutFile python_installer.exe"
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
    echo [*] Python installed successfully.
)

echo [*] Upgrading pip...
python -m ensurepip >nul 2>&1
python -m pip install --upgrade pip >nul

echo [*] Installing required Python packages from requirements.txt...
python -m pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [!] Failed to install some requirements. Check your internet connection or requirements.txt.
    pause
    exit /b 1
)


echo [*] Setup Complete! You can now run the tool using '3th1c4l.bat' or '3th1c4l.py'.
pause
