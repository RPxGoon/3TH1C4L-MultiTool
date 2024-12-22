import os
import subprocess
import sys

def install_requirements():
    print("[*] Upgrading pip...")
    subprocess.run([sys.executable, "-m", "ensurepip"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("[*] Installing required Python packages from requirements.txt...")
    result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("[!] Failed to install some requirements. Check your internet connection or requirements.txt.")
        sys.exit(1)

def main():

    install_requirements()

    print("[*] Setup Complete! You can now run [3TH1C4L] using '3th1c4l.py' or '3th1c4l.bat")
    
if __name__ == "__main__":
    main()
