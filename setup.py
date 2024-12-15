import os
import subprocess
import sys

def install_requirements():
    """Ensure all requirements are installed."""
    try:
        print("[*] Installing/upgrading pip...")
        subprocess.check_call([sys.executable, '-m', 'ensurepip'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        
        print("[*] Installing required packages from requirements.txt...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("[*] All requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to install requirements: {e}")
        sys.exit(1)

def check_python():
    """Check Python version and inform if unsupported."""
    if sys.version_info < (3, 7):
        print("[!] Python 3.7 or higher is required. Please upgrade Python.")
        sys.exit(1)

def main():
    print("[*] Checking Python environment...")
    check_python()

    print("[*] Installing requirements...")
    install_requirements()

    print("[*] Setup complete. You can now run the tool using '3th1c4l.bat'.")

if __name__ == "__main__":
    main()
