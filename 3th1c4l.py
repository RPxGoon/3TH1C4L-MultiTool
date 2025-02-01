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

Simple OSINT / Discord Multi-tool
[https://github.com/RPxGoon/3TH1C4L-MultiTool]
"""
    start_color = (255, 0, 0)  # Red
    end_color = (75, 0, 148)   # Purple
    width = get_terminal_width()
    for line in logo.splitlines():
        centered_line = center_text(line, width)
        smooth_gradient_print(centered_line, start_color, end_color)


#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --    Created by: RPxGoon  --  Please DO NOT REMOVE THIS LINE  --    Only Download From Offical Github Repo: https://github.com/RPxGoon/3TH1C4L-MultiTool   Please DO NOT REMOVE THIS LINE   --  Created by: RPxGoon  --

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
    current_page = 1

    while True:
        print_menu(current_page)
        choice = questionary.text("[3TH1C4L] >>", style=style).ask()

        if choice.lower() == 'n': 
            if current_page == 1:
                current_page = 2

        elif choice.lower() == 'b': 
            if current_page == 2:
                current_page = 1

        elif choice == '1' and current_page == 1:
            print(f"{Fore.MAGENTA}[Show My IP]")
            print()
            show_my_ip()

        elif choice == '2' and current_page == 1:
            print(f"{Fore.MAGENTA}[IP Info]")
            print()
            ip_scanner()

        elif choice == '3' and current_page == 1:
            print(f"{Fore.MAGENTA}[IP Pinger]")
            print()
            run_ip_pinger()

        elif choice == '4' and current_page == 1:
            print(f"{Fore.MAGENTA}[IP Port Scanner]")
            print()
            ip_port_scanner()

        elif choice == '5' and current_page == 1:
            print(f"{Fore.MAGENTA}[Website Info Scanner]")
            print()
            website_info_scanner()

        elif choice == '26' and current_page == 2:
            print(f"{Fore.MAGENTA}[Discord Token Info]")
            print()
            discord_token_info()

        elif choice == '16' and current_page == 2:
            print(f"{Fore.MAGENTA}[Discord Server Info]")
            discord_server_info()

        elif choice == '17' and current_page == 2:
            print(f"{Fore.MAGENTA}[Discord Nitro Generator]")
            print()
            discord_nitro_generator()

        elif choice == '27' and current_page == 2:
            print(f"{Fore.MAGENTA}[Token Delete DM]")
            print()
            discord_token_delete_dm()

        elif choice == '6' and current_page == 1:
            print(f"{Fore.MAGENTA}[Username Tracker]")
            print()
            username_tracker()

        elif choice == '11' and current_page == 1:
             print(f"{Fore.MAGENTA}[Password Generator]")
             print()
             password_generator()

        elif choice == "21" and current_page == 2:
            print(f"{Fore.MAGENTA}[Discord Webhook Deleter]")
            print()
            discord_webhook_deleter()
        
        elif choice == "28" and current_page == 2:
            print(f"{Fore.MAGENTA}[Discord Token User ID Blocker]") 
            print()
            discord_token_block_friends()

        elif choice.lower() == 'e': 
            print(f"{Fore.RED}[!] {Fore.GREEN}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.RED}[!] {Fore.GREEN}Invalid Choice. Please Select a Valid Option")

        if choice.lower() not in ['n', 'b', 'e']:  
            input(f"{Fore.RED}[*] {Fore.GREEN}Press 'Enter' to Continue...")

        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    run_tool()


#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --    Created by: RPxGoon  --  Please DO NOT REMOVE THIS LINE  --    Only Download From Offical Github Repo: https://github.com/RPxGoon/3TH1C4L-MultiTool   Please DO NOT REMOVE THIS LINE   --  Created by: RPxGoon  --                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      --    Created by: RPxGoon  --  Please DO NOT REMOVE THIS LINE  --    Only Download From Offical Github Repo: https://github.com/RPxGoon/3TH1C4L-MultiTool   Please DO NOT REMOVE THIS LINE   --  Created by: RPxGoon  --