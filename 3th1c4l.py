import os
import sys
import shutil
import time
import threading
import itertools
from functools import lru_cache
from colorama import init, Fore, Style
import questionary
import getpass
from importlib import import_module


init(autoreset=True)
username = getpass.getuser()

def loading_spinner():
    spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
    while not loading_spinner.done:
        sys.stdout.write(f'\r{Fore.RED}Loading {Fore.LIGHTGREEN_EX}{next(spinner)} ')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

loading_spinner.done = False

def animate_loading(duration=1.0):
    loading_spinner.done = False
    spinner_thread = threading.Thread(target=loading_spinner)
    spinner_thread.start()
    time.sleep(duration)
    loading_spinner.done = True
    spinner_thread.join()

@lru_cache(maxsize=1)
def get_terminal_width(default_width=80):
    try:
        width = shutil.get_terminal_size().columns
        return max(80, width)
    except Exception:
        return default_width

def set_cmd_title_and_color():
    if os.name == 'nt':
        os.system('title [3TH1C4L] Multi-Tool && color 0A')

# Dictionary with lazy loading for easy implementation
TOOLS = {
    '1': {'name': 'My Public IP Address', 'module': 'scripts.show_my_ip', 'function': 'run', 'page': 1},
    '2': {'name': 'IP Scanner', 'module': 'scripts.ip_scanner', 'function': 'run', 'page': 1},
    '3': {'name': 'IP Pinger', 'module': 'scripts.ip_pinger', 'function': 'run_ip_pinger', 'page': 1},
    '4': {'name': 'IP Port Scanner', 'module': 'scripts.ip_port_scanner', 'function': 'run', 'page': 1},
    '5': {'name': 'Website Info Scanner', 'module': 'scripts.website_info_scanner', 'function': 'run', 'page': 1},
    '6': {'name': 'Username Tracker', 'module': 'scripts.username_tracker', 'function': 'run', 'page': 1},
    '11': {'name': 'Password Generator', 'module': 'scripts.password_generator', 'function': 'run', 'page': 1},
    '16': {'name': 'Discord Server Info', 'module': 'scripts.discord_server_info', 'function': 'run', 'page': 2},
    '17': {'name': 'Discord Nitro Generator', 'module': 'scripts.discord_nitro_generator', 'function': 'run', 'page': 2},
    '21': {'name': 'Discord Webhook Deleter', 'module': 'scripts.discord_webhook_deleter', 'function': 'run', 'page': 2},
    '22': {'name': 'Discord Webhook Spammer', 'module': 'scripts.discord_webhook_spammer', 'function': 'run', 'page': 2},
    '26': {'name': 'Discord Token Info', 'module': 'scripts.discord_token_info', 'function': 'run', 'page': 2},
    '27': {'name': 'Token Delete DM', 'module': 'scripts.discord_token_delete_dm', 'function': 'run', 'page': 2},
    '28': {'name': 'Discord Token User ID Blocker', 'module': 'scripts.discord_token_block_friends', 'function': 'run', 'page': 2},
}

def smooth_gradient_print(text, start_color, end_color):
    steps = len(text) - 1 if len(text) > 1 else 1
    r_start, g_start, b_start = start_color
    r_end, g_end, b_end = end_color

    gradient_text = "".join(
        f'\033[38;2;{int(r_start + (r_end - r_start) * (i / steps))};'
        f'{int(g_start + (g_end - g_start) * (i / steps))};'
        f'{int(b_start + (b_end - b_start) * (i / steps))}m{char}'
        for i, char in enumerate(text)
    )
    print(gradient_text + Style.RESET_ALL)

def center_text(text, width=None):
    return text.center(width or get_terminal_width())

ASCII_LOGO = r"""
/* ++------------------------------------------------------------------++ */
/* ++------------------------------------------------------------------++ */
/* ||    ▓█████ ▄▄▄█████▓ ██░ ██  ▐██▌  ▄████▄   ▄▄▄       ██▓         || */
/* ||    ▓█   ▀ ▓  ██▒ ▓▒▓██░ ██▒ ▐██▌ ▒██▀ ▀█  ▒████▄    ▓██▒         || */
/* ||    ▒███   ▒ ▓██░ ▒░▒██▀▀██░ ▐██▌ ▒▓█    ▄ ▒██  ▀█▄  ▒██░         || */
/* ||    ▒▓█  ▄ ░ ▓██▓ ░ ░▓█ ░██  ▓██▒ ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░         || */
/* ||    ░▒████▒  ▒██▒ ░ ░▓█▒░██▓ ▒▄▄  ▒ ▓███▀ ░ ▓█   ▓██▒░██████▒     || */
/* ||    ░░ ▒░ ░  ▒ ░░    ▒ ░░▒░▒ ░▀▀▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░     || */
/* ||     ░ ░  ░    ░     ▒ ░▒░ ░ ░  ░   ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░     || */
/* ||       ░     ░       ░  ░░ ░    ░ ░          ░   ▒     ░ ░        || */
/* ||       ░  ░          ░  ░  ░ ░    ░ ░            ░  ░    ░  ░     || */
/* ||                           [RPxGoon]░                             || */
/* ++------------------------------------------------------------------++ */
/* ++------------------------------------------------------------------++ */

Simple 'CLI' Python Multi-Tool
[https://github.com/RPxGoon/3TH1C4L-MultiTool]
"""

def print_ascii_logo():
    width = get_terminal_width()
    start_color = (255, 0, 0)
    end_color = (75, 0, 148)
    for line in ASCII_LOGO.splitlines():
        smooth_gradient_print(center_text(line, width), start_color, end_color)

def print_menu(page=1):
    os.system('cls' if os.name == 'nt' else 'clear')
    width = get_terminal_width()
    print_ascii_logo()

    if page == 1:
        section_width = width // 3
        box_border_length = section_width - 2

        print(Fore.MAGENTA + "╓" + "─" * box_border_length + "╖" + "╓" + "─" * box_border_length + "╖" + "╓" + "─" * box_border_length + "╖")
        print(Fore.MAGENTA + "  NETWORK SCANNERS".center(box_border_length) + "        OSINT".center(box_border_length) + "           OTHER".center(box_border_length))
        print(Fore.MAGENTA + "╙" + "─" * box_border_length + "╜" + "╙" + "─" * box_border_length + "╜" + "╙" + "─" * box_border_length + "╜")

        print(f"{Fore.RED}├─ [{Fore.MAGENTA}01{Fore.RED}] Show My IP".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}06{Fore.RED}] Username Tracker".center(section_width) + f"{Fore.RED}                ├─ [{Fore.MAGENTA}11{Fore.RED}] Password Generator".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}02{Fore.RED}] IP Scanner".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}07{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}12{Fore.RED}] Coming Soon...".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}03{Fore.RED}] IP Pinger".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}08{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}13{Fore.RED}] Coming Soon...".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}04{Fore.RED}] IP Port Scanner".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}09{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}14{Fore.RED}] Coming Soon...".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}05{Fore.RED}] Website Info Scanner".ljust(section_width) + f"{Fore.RED}            ├─ [{Fore.MAGENTA}10{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}15{Fore.RED}] Coming Soon...".rjust(section_width))

    elif page == 2:
        section_width = width // 3

        print(Fore.MAGENTA + "╓" + "─" * (width - 2) + "╖")
        print(Fore.MAGENTA + " " * ((width - len("DISCORD TOOLS")) // 2) + "DISCORD TOOLS")
        print(Fore.MAGENTA + "╙" + "─" * (width - 2) + "╜")

        print(f"{Fore.RED}├─ [{Fore.MAGENTA}16{Fore.RED}] Discord Server Info".ljust(section_width) + f"{Fore.RED}             ├─ [{Fore.MAGENTA}21{Fore.RED}] Delete Discord Webhook".center(section_width) + f"{Fore.RED}          ├─ [{Fore.MAGENTA}26{Fore.RED}] Discord Token Info".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}17{Fore.RED}] Discord Nitro Generator".ljust(section_width) + f"{Fore.RED}         ├─ [{Fore.MAGENTA}22{Fore.RED}] Discord Webhook Spammer".center(section_width) + f"{Fore.RED}         ├─ [{Fore.MAGENTA}27{Fore.RED}] Discord Token Delete DM".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}18{Fore.RED}] Coming Soon...".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}23{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}28{Fore.RED}] Discord Token Friend Blocker".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}19{Fore.RED}] Coming Soon...".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}24{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}29{Fore.RED}] Coming Soon...".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}20{Fore.RED}] Coming Soon...".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}25{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}30{Fore.RED}] Coming Soon...".rjust(section_width))

    print(f"{''.rjust((126))}{Fore.RED}                                                                          {Fore.RED}├─ [{Fore.MAGENTA}N{Fore.RED}] Next | [{Fore.MAGENTA}B{Fore.RED}] Back | [{Fore.MAGENTA}E{Fore.RED}] Exit".rjust(126))
    print()


CUSTOM_STYLE = questionary.Style([
    ("question", "bold lime"),
    ("answer", "lime"),
    ("pointer", "lime"),
    ("selected", "lime"),
    ("input", "lime"),
    ("highlighted", "lime"),
    ("instruction", "lime"),
    ("text", "red bold"),
    ("prompt", "lime"),
])

def run_tool():
    set_cmd_title_and_color()
    current_page = 1

    while True:
        print_menu(current_page)
        choice = questionary.text(
            f"┌──({username}@3TH1C4L)─[~/main]\n └─$",
            qmark="",
            style=CUSTOM_STYLE,
        ).ask()

        if choice.lower() == 'n' and current_page == 1:
            animate_loading(0.3)  # Add loading animation for page change
            current_page = 2
        elif choice.lower() == 'b' and current_page == 2:
            animate_loading(0.3)  
            current_page = 1
        elif choice.lower() == 'e':
            animate_loading(0.5)
            print(f"{Fore.RED}[!] {Fore.LIGHTGREEN_EX}Exiting... Goodbye!")
            break
        elif choice in TOOLS:
            tool = TOOLS[choice]
            if tool['page'] == current_page:
                animate_loading(0.3)
                print(f"{Fore.MAGENTA}[{tool['name']}]")
                print()
                module = import_module(tool['module'])
                getattr(module, tool['function'])()
            else:
                animate_loading(0.3)
                print(f"{Fore.RED}[!] Invalid Choice. Please Select a Valid Option")
        else:
            animate_loading(0.3)
            print(f"{Fore.RED}[!] Invalid Choice. Please Select a Valid Option")

        if choice.lower() not in ['n', 'b', 'e']:
            input(f"{Fore.RED}[*] {Fore.LIGHTGREEN_EX}Press 'Enter' to Continue...")
            
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    run_tool()