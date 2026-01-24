#!/bin/bash

# 3TH1C4L MultiTool - Universal Linux Setup
# Official Repo: https://github.com/RPxGoon/3TH1C4L-MultiTool
#
# Usage:
# Local:  ./setup.sh
# Remote: curl -sSL https://raw.githubusercontent.com/RPxGoon/3TH1C4L-MultiTool/main/setup.sh | bash

set -e

clear
echo -e "\e[31m"
echo "╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                                                                                                       ║"
echo "║                                                    3TH1C4L MultiTool - Linux Setup                                                                   ║"
echo "║                                                                                                                                                       ║"
echo "║                                              https://github.com/RPxGoon/3TH1C4L-MultiTool                                                           ║"
echo "║                                                                                                                                                       ║"
echo "║                                                         Thanks for the Support :)                                                                    ║"
echo "║                                                                                                                                                       ║"
echo "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"
echo -e "\e[0m"
echo

# Check if we need to download the repository first
if [ ! -f "3th1c4l.py" ]; then
    echo -e "\e[34m[*] 3th1c4l.py not found - downloading repository...\e[0m"
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        echo -e "\e[31m[!] Git is not installed. Please install git first.\e[0m"
        exit 1
    fi
    
    # Set installation directory
    INSTALL_DIR="$HOME/3TH1C4L-MultiTool"
    
    # Remove existing installation if it exists
    if [ -d "$INSTALL_DIR" ]; then
        echo -e "\e[34m[*] Removing existing installation...\e[0m"
        rm -rf "$INSTALL_DIR"
    fi
    
    # Clone the repository
    echo -e "\e[34m[*] Downloading 3TH1C4L MultiTool...\e[0m"
    git clone https://github.com/RPxGoon/3TH1C4L-MultiTool.git "$INSTALL_DIR"
    
    # Navigate to the directory
    cd "$INSTALL_DIR"
    echo -e "\e[32m[✓] Repository downloaded successfully\e[0m"
fi

# Detect Linux distribution
echo -e "\e[34m[*] Detecting Linux distribution...\e[0m"
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo -e "\e[31m[!] Could not detect Linux distribution\e[0m"
    exit 1
fi

echo -e "\e[32m[✓] Detected: $PRETTY_NAME\e[0m"

# Check if Python 3 and Tkinter are installed
echo -e "\e[34m[*] Checking for Python 3 and Tkinter...\e[0m"
NEED_INSTALL=false

if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    PYTHON_CMD="python3"
    
    # Check for Tkinter
    if $PYTHON_CMD -c "import tkinter" &> /dev/null; then
        echo -e "\e[32m[✓] Python 3 ($PYTHON_VERSION) and Tkinter are installed\e[0m"
    else
        echo -e "\e[33m[!] Python 3 found ($PYTHON_VERSION) but Tkinter is missing\e[0m"
        NEED_INSTALL=true
    fi
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1 | cut -d' ' -f2)
    if [[ $PYTHON_VERSION == 3* ]]; then
        PYTHON_CMD="python"
        
        # Check for Tkinter
        if $PYTHON_CMD -c "import tkinter" &> /dev/null; then
             echo -e "\e[32m[✓] Python 3 ($PYTHON_VERSION) and Tkinter are installed\e[0m"
        else
             echo -e "\e[33m[!] Python 3 found ($PYTHON_VERSION) but Tkinter is missing\e[0m"
             NEED_INSTALL=true
        fi
    else
        echo -e "\e[33m[!] Python 2 detected, need to install Python 3\e[0m"
        NEED_INSTALL=true
        PYTHON_CMD="python3"
    fi
else
    echo -e "\e[33m[!] Python 3 not found, installing...\e[0m"
    NEED_INSTALL=true
    PYTHON_CMD="python3"
fi

# Install Python 3 and/or Tkinter if needed
if [ "$NEED_INSTALL" = true ]; then
    echo -e "\e[34m[*] Installing Python 3 and dependencies...\e[0m"
    
    case $DISTRO in
        ubuntu|debian|linuxmint|pop|elementary|zorin|kali|parrot)
            sudo apt update && sudo apt install -y python3 python3-pip python3-venv python3-tk
            ;;
        fedora|rhel|centos|rocky|almalinux)
            if command -v dnf &> /dev/null; then
                sudo dnf install -y python3 python3-pip python3-tkinter
            else
                sudo yum install -y python3 python3-pip tkinter
            fi
            ;;
        arch|manjaro|endeavouros|garuda|cachyos|artix)
            sudo pacman -S --noconfirm python python-pip tk
            ;;
        opensuse*|sles)
            sudo zypper install -y python3 python3-pip python3-tk
            ;;
        alpine)
            sudo apk add python3 py3-pip tk
            ;;
        gentoo)
            sudo emerge -av dev-lang/python:3.11
            ;;
        void)
            sudo xbps-install -S python3 python3-pip python3-tkinter
            ;;
        *)
            echo -e "\e[31m[!] Unsupported distribution: $DISTRO\e[0m"
            echo -e "\e[33m[!] Please install Python 3 and Tkinter manually and run this script again\e[0m"
            exit 1
            ;;
    esac
    
    # Check if installation was successful
    if ! command -v $PYTHON_CMD &> /dev/null; then
        echo -e "\e[31m[!] Python 3 installation failed!\e[0m"
        exit 1
    fi
    
    if ! $PYTHON_CMD -c "import tkinter" &> /dev/null; then
        echo -e "\e[31m[!] Tkinter installation failed!\e[0m"
        exit 1
    fi
    
    echo -e "\e[32m[✓] Python 3 and Tkinter installed successfully\e[0m"
fi

# Check if pip is available
echo -e "\e[34m[*] Checking for pip...\e[0m"
if ! $PYTHON_CMD -m pip --version &> /dev/null; then
    echo -e "\e[33m[!] pip not found, installing...\e[0m"
    
    case $DISTRO in
        ubuntu|debian|linuxmint|pop|elementary|zorin|kali)
            sudo apt install -y python3-pip
            ;;
        fedora|rhel|centos|rocky|almalinux)
            if command -v dnf &> /dev/null; then
                sudo dnf install -y python3-pip
            else
                sudo yum install -y python3-pip
            fi
            ;;
        arch|manjaro|endeavouros|garuda|cachyos|artix)
            sudo pacman -S --noconfirm python-pip
            ;;
        opensuse*|sles)
            sudo zypper install -y python3-pip
            ;;
        alpine)
            sudo apk add py3-pip
            ;;
        *)
            echo -e "\e[31m[!] Please install pip manually\e[0m"
            exit 1
            ;;
    esac
fi

echo -e "\e[32m[✓] pip is available\e[0m"

# Create virtual environment to avoid system package conflicts
echo -e "\e[34m[*] Creating virtual environment...\e[0m"
if [ -d ".venv" ]; then
    rm -rf .venv
fi
$PYTHON_CMD -m venv .venv

# Activate virtual environment
echo -e "\e[34m[*] Activating virtual environment...\e[0m"
source .venv/bin/activate

# Install requirements in virtual environment
echo -e "\e[34m[*] Installing requirements in virtual environment...\e[0m"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo -e "\e[32m[✓] All requirements installed successfully!\e[0m"
    
    # Create launcher script
    echo -e "\e[34m[*] Creating launcher script...\e[0m"
    cat > 3th1c4l.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
source .venv/bin/activate
python 3th1c4l.py
EOF
    chmod +x 3th1c4l.sh
    
    echo -e "\e[32m[✓] Setup complete!\e[0m"
    echo -e "\e[34m[*] For future usage, you can simply run: \e[32m./3th1c4l.sh\e[0m"
    echo
    
    # Attempt to reconnect to a TTY if stdin is a pipe (fix for curl | bash)
    if [ ! -t 0 ] && [ -e /dev/tty ]; then
        exec < /dev/tty
    fi

    # Launch the tool
    echo -e "\e[34m[*] Launching 3TH1C4L MultiTool...\e[0m"
    sleep 1
    python 3th1c4l.py
else
    echo -e "\e[31m[!] Failed to install requirements\e[0m"
    exit 1
fi
