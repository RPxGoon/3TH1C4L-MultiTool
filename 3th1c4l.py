#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --    Created by: RPxGoon  --  Please DO NOT REMOVE THIS LINE  --    Only Download From Offical Github Repo: https://github.com/RPxGoon/3TH1C4L-MultiTool   Please DO NOT REMOVE THIS LINE   --  Created by: RPxGoon  --
import os
import sys
import shutil
from colorama import init, Fore, Style
import questionary

init(autoreset=True)


def set_cmd_title_and_color():
    if os.name == 'nt': 
        os.system('title [3TH1C4L] Multi-Tool')
        os.system('color 0A')
        

#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --    Created by: RPxGoon  --  Please DO NOT REMOVE THIS LINE  --    Only Download From Offical Github Repo: https://github.com/RPxGoon/3TH1C4L-MultiTool   Please DO NOT REMOVE THIS LINE   --  Created by: RPxGoon  --

from scripts.show_my_ip import run as show_my_ip
from scripts.ip_info import run as ip_info
from scripts.ip_pinger import run_ip_pinger
from scripts.discord_token_info import discord_token_info
from scripts.ip_port_scanner import run as ip_port_scanner
from scripts.website_info_scanner import run as website_info_scanner
from scripts.youtube_downloader import youtube_downloader


def smooth_gradient_print(text, start_color, end_color):
    """
    Print text with a smooth gradient effect from start_color to end_color.

    Parameters:
        text (str): The text to print.
        start_color (tuple): RGB tuple for the starting color.
        end_color (tuple): RGB tuple for the ending color.
    """
    steps = len(text) - 1 if len(text) > 1 else 1  
    r_start, g_start, b_start = start_color
    r_end, g_end, b_end = end_color

    for i, char in enumerate(text):
        r = int(r_start + (r_end - r_start) * (i / steps))
        g = int(g_start + (g_end - g_start) * (i / steps))
        b = int(b_start + (b_end - b_start) * (i / steps))
        color = f'\033[38;2;{r};{g};{b}m'
        print(f"{color}{char}", end="")
    print(Style.RESET_ALL)


def get_terminal_width(default_width=80):
    """Get terminal width or fallback to default."""
    try:
        width = shutil.get_terminal_size().columns
    except Exception:
        width = default_width
    return max(80, width)  


def center_text(text, width=None):
    width = width or get_terminal_width()
    return text.center(width)


def print_ascii_logo():
    logo =   r"""
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

Simple OSINT / Discord Multi-tool
[https://github.com/RPxGoon/3TH1C4L-MultiTool]

"""
    start_color = (255, 0, 0)
    end_color = (75, 0, 148)
    width = get_terminal_width()
    for line in logo.splitlines():
        smooth_gradient_print(center_text(line, width), start_color, end_color)


#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --    Created by: RPxGoon  --  Please DO NOT REMOVE THIS LINE  --    Only Download From Offical Github Repo: https://github.com/RPxGoon/3TH1C4L-MultiTool   Please DO NOT REMOVE THIS LINE   --  Created by: RPxGoon  --

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    width = get_terminal_width()

    print_ascii_logo()

    section_width = width // 3

    box_border_length = section_width - 2

    print(Fore.MAGENTA + "╓" + "─" * box_border_length + "╖" + "╓" + "─" * box_border_length + "╖" + "╓" + "─" * box_border_length + "╖")
    print(Fore.MAGENTA + "  OSINT".center(box_border_length) + "        DISCORD".center(box_border_length) + "           OTHER".center(box_border_length))
    print(Fore.MAGENTA + "╙" + "─" * box_border_length + "╜" + "╙" + "─" * box_border_length + "╜" + "╙" + "─" * box_border_length + "╜")
    
    print(f"{Fore.RED}├─ [01] Show My IP".ljust(section_width) + f"{Fore.RED}├─ [06] Token Checker  ".center(section_width) + f"             {Fore.RED}├─ [11] Youtube Downloader".rjust(section_width))
    print(f"{Fore.RED}├─ [02] IP Info".ljust(section_width) + f"{Fore.RED}├─ [07] Coming Soon...".center(section_width) + f"{Fore.RED}├─ [12] Coming Soon...".rjust(section_width))
    print(f"{Fore.RED}├─ [03] IP Pinger".ljust(section_width) + f"{Fore.RED}├─ [08] Coming Soon...".center(section_width) + f"{Fore.RED}├─ [13] Coming Soon...".rjust(section_width))
    print(f"{Fore.RED}├─ [04] Port Scanner".ljust(section_width) + f"{Fore.RED}├─ [09] Coming Soon...".center(section_width) + f"{Fore.RED}├─ [14] Coming Soon...".rjust(section_width))
    print(f"{Fore.RED}├─ [05] Website Info Scanner".ljust(section_width) + f"{Fore.RED}├─ [10] Coming Soon...".center(section_width) + f"{Fore.RED}├─ [15] Coming Soon...".rjust(section_width))

    print(f"{''.rjust((126) )}{Fore.RED}                                                                             ├─ [N] Next | [E] Exit".rjust(126))
    print()

#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --    Created by: RPxGoon  --  Please DO NOT REMOVE THIS LINE  --    Only Download From Offical Github Repo: https://github.com/RPxGoon/3TH1C4L-MultiTool   Please DO NOT REMOVE THIS LINE   --  Created by: RPxGoon  --

def run_tool():
    style = questionary.Style([ 
        ("question", "bold fg:green"),
        ("answer", "fg:green"),
        ("questionmark", "fg:red"),
        ("pointer", "fg:green"),
        ("selected", "fg:green"),
        ("input", "fg:green"),
        ("highlighted", "fg:green"),
        ("inactive", "fg:green"),
        ("instructions", "fg:green"),
        ("prompt", "fg:green"),
    ])

    set_cmd_title_and_color()  

    while True:
        print_menu()
        choice = questionary.text("[3TH1C4L] >>", style=style).ask()

        if choice == '1':
            print(f"{Fore.LIGHTGREEN_EX}[Show My IP]")
            show_my_ip()
        elif choice == '2':
            print(f"{Fore.LIGHTGREEN_EX}[IP Info]")
            ip_info()
        elif choice == '3':
            print(f"{Fore.LIGHTGREEN_EX}[IP Pinger]")
            run_ip_pinger()
        elif choice == '4':
            print(f"{Fore.LIGHTGREEN_EX}[IP Port Scanner]")
            ip_port_scanner()
        elif choice == '5':
            print(f"{Fore.LIGHTGREEN_EX}[Website Info Scanner]")
            website_info_scanner()   
        elif choice == '6':
            print(f"{Fore.LIGHTGREEN_EX}[Discord Token Checker]")
            token_info = input(f"{Fore.LIGHTGREEN_EX}Enter Discord Token: {Fore.RESET}")
            print(f"{Fore.LIGHTGREEN_EX}Checking Discord Token...")
            discord_token_info(token_info)
        elif choice == '11':
            print(f"{Fore.LIGHTGREEN_EX}[Youtube Downloader]")
            youtube_downloader()
        elif choice.lower() == 'n': 
            print(f"{Fore.LIGHTGREEN_EX} [!] Next Page / More Free Tools COMING SOON!...")
            print(f"{Fore.LIGHTGREEN_EX} [!] You May be Missing Features! Make Sure Your Tool is Up to Date! [https://github.com/RPxGoon/3TH1C4L-MultiTool]")
            print(f"{Fore.LIGHTGREEN_EX} [!] Thank You for Your Support! -[RPxGoon] :)")
        elif choice.lower() == 'e': 
            print(f"{Fore.LIGHTGREEN_EX} [!] Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.LIGHTRED_EX}[!] Invalid Choice. Please select a valid option.")

        input(f"{Fore.LIGHTGREEN_EX}[*] Press 'Enter' to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    run_tool()


#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --    Created by: RPxGoon  --  Please DO NOT REMOVE THIS LINE  --    Only Download From Offical Github Repo: https://github.com/RPxGoon/3TH1C4L-MultiTool   Please DO NOT REMOVE THIS LINE   --  Created by: RPxGoon  --