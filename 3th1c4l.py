import os
import sys
import shutil
import colorama
from colorama import init, Fore, Style
import questionary
import getpass

init(autoreset=True)
username = getpass.getuser()

def set_cmd_title_and_color():
    if os.name == 'nt': 
        os.system('title [3TH1C4L] Multi-Tool')
        os.system('color 0A')

# Importing scripts from the scripts folder, use filename as function
from scripts.show_my_ip import run as show_my_ip
from scripts.ip_scanner import run as ip_scanner
from scripts.ip_pinger import run_ip_pinger
from scripts.discord_token_info import run as discord_token_info
from scripts.ip_port_scanner import run as ip_port_scanner
from scripts.website_info_scanner import run as website_info_scanner
from scripts.discord_server_info import run as discord_server_info
from scripts.discord_nitro_generator import run as discord_nitro_generator
from scripts.discord_webhook_deleter import run as discord_webhook_deleter
from scripts.discord_token_delete_dm import run as discord_token_delete_dm
from scripts.discord_token_block_friends import run as discord_token_block_friends
from scripts.username_tracker import run as username_tracker
from scripts.password_generator import run as password_generator

# Dictionary to make it easier when adding new scripts
TOOLS = {
    '1': {'name': 'My Public IP Address', 'function': show_my_ip, 'page': 1},
    '2': {'name': 'IP Scanner', 'function': ip_scanner, 'page': 1},
    '3': {'name': 'IP Pinger', 'function': run_ip_pinger, 'page': 1},
    '4': {'name': 'IP Port Scanner', 'function': ip_port_scanner, 'page': 1},
    '5': {'name': 'Website Info Scanner', 'function': website_info_scanner, 'page': 1},
    '6': {'name': 'Username Tracker', 'function': username_tracker, 'page': 1},
    '11': {'name': 'Password Generator', 'function': password_generator, 'page': 1},
    '16': {'name': 'Discord Server Info', 'function': discord_server_info, 'page': 2},
    '17': {'name': 'Discord Nitro Generator', 'function': discord_nitro_generator, 'page': 2},
    '21': {'name': 'Discord Webhook Deleter', 'function': discord_webhook_deleter, 'page': 2},
    '26': {'name': 'Discord Token Info', 'function': discord_token_info, 'page': 2},
    '27': {'name': 'Token Delete DM', 'function': discord_token_delete_dm, 'page': 2},
    '28': {'name': 'Discord Token User ID Blocker', 'function': discord_token_block_friends, 'page': 2},
}

def smooth_gradient_print(text, start_color, end_color):
    steps = len(text) - 1 if len(text) > 1 else 1  
    r_start, g_start, b_start = start_color
    r_end, g_end, b_end = end_color

    gradient_text = ""
    for i, char in enumerate(text):
        r = int(r_start + (r_end - r_start) * (i / steps))
        g = int(g_start + (g_end - g_start) * (i / steps))
        b = int(b_start + (b_end - b_start) * (i / steps))
        color = f'\033[38;2;{r};{g};{b}m'
        gradient_text += f"{color}{char}"
    gradient_text += Style.RESET_ALL
    print(gradient_text)

def get_terminal_width(default_width=80):
    try:
        width = shutil.get_terminal_size().columns
    except Exception:
        width = default_width
    return max(80, width)  

def center_text(text, width=None):
    width = width or get_terminal_width()
    return text.center(width)

def print_ascii_logo():
    logo = r"""
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
    start_color = (255, 0, 0)  # Red
    end_color = (75, 0, 148)   # Purple
    width = get_terminal_width()
    for line in logo.splitlines():
        centered_line = center_text(line, width)
        smooth_gradient_print(centered_line, start_color, end_color)

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
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}17{Fore.RED}] Discord Nitro Generator".ljust(section_width) + f"{Fore.RED}         ├─ [{Fore.MAGENTA}22{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}27{Fore.RED}] Discord Token Delete DM".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}18{Fore.RED}] Coming Soon...".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}23{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}28{Fore.RED}] Discord Token Friend Blocker".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}19{Fore.RED}] Coming Soon...".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}24{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}29{Fore.RED}] Coming Soon...".rjust(section_width))
        print(f"{Fore.RED}├─ [{Fore.MAGENTA}20{Fore.RED}] Coming Soon...".ljust(section_width) + f"{Fore.RED}               ├─ [{Fore.MAGENTA}25{Fore.RED}] Coming Soon...".center(section_width) + f"{Fore.RED}                  ├─ [{Fore.MAGENTA}30{Fore.RED}] Coming Soon...".rjust(section_width))

    print(f"{''.rjust((126))}{Fore.RED}                                                                          {Fore.RED}├─ [{Fore.MAGENTA}N{Fore.RED}] Next | [{Fore.MAGENTA}B{Fore.RED}] Back | [{Fore.MAGENTA}E{Fore.RED}] Exit".rjust(126))
    print()

def run_tool():
    custom_style = questionary.Style([
        ("question", "bold fg:#39FF14"),  # Neon lime green
        ("answer", "fg:#39FF14"),
        ("pointer", "fg:#39FF14"),
        ("selected", "fg:#39FF14"),
        ("input", "fg:#39FF14"),
        ("highlighted", "fg:#39FF14"),
        ("instruction", "fg:#39FF14"),
        ("text", "fg:red bold"),  # Red for brackets [], parentheses (), and dashes ─
        ("prompt", "fg:#39FF14"),
    ])



    set_cmd_title_and_color()  
    current_page = 1

    while True:
        print_menu(current_page)
        choice = questionary.text(
            f"┌──({username}@3TH1C4L)─[~/main]\n └─$",
            qmark="",  #THIS REMOVES THE ANNOYING ASS QUESTIONMARK FROM QUESTIONARY
            style=custom_style,
        ).ask()

        if choice.lower() == 'n':
            if current_page == 1:
                current_page = 2

        elif choice.lower() == 'b':
            if current_page == 2:
                current_page = 1

        elif choice.lower() == 'e':
            print(f"{Fore.RED}[!] {Fore.LIGHTGREEN_EX}Exiting... Goodbye!")
            break

        # Handling tool selection from TOOLS dictionary
        elif choice in TOOLS:
            tool = TOOLS[choice]
            if tool['page'] == current_page:
                print(f"{Fore.MAGENTA}[{tool['name']}]")
                print()
                tool['function']()
            else:
                print(f"{Fore.RED}[!] {Fore.LIGHTGREEN_EX}Invalid Choice. Please Select a Valid Option")

        else:
            print(f"{Fore.RED}[!] {Fore.LIGHTGREEN_EX}Invalid Choice. Please Select a Valid Option")

        if choice.lower() not in ['n', 'b', 'e']:
            input(f"{Fore.RED}[*] {Fore.LIGHTGREEN_EX}Press 'Enter' to Continue...")

        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    run_tool()