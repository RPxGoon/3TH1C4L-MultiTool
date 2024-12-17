import os
import sys
from colorama import init, Fore, Style
import questionary

# Initialize colorama
init(autoreset=True)

# Import scripts
from scripts.show_my_ip import run as show_my_ip
from scripts.ip_info import run as ip_info
from scripts.ip_pinger import run_ip_pinger
from scripts.token_checker import check_token
from scripts.ip_port_scanner import run as ip_port_scanner
from scripts.website_info_scanner import run as website_info_scanner


def smooth_gradient_print(text, start_color, end_color, steps):
    if steps == 0:
        print(text)
        return
    r_start, g_start, b_start = start_color
    r_end, g_end, b_end = end_color
    for i, char in enumerate(text):
        r = int(r_start + (r_end - r_start) * (i / steps))
        g = int(g_start + (g_end - g_start) * (i / steps))
        b = int(b_start + (b_end - b_start) * (i / steps))
        color = f'\033[38;2;{r};{g};{b}m'
        print(f"{color}{char}", end="")  # Print each character with color
    print()


def center_text(text, width=80):
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
    start_color = (255, 0, 0)
    end_color = (128, 0, 128)
    for line in logo.splitlines():
        smooth_gradient_print(center_text(line), start_color, end_color, len(line))


def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_ascii_logo()

    print(Fore.LIGHTBLACK_EX + "=" * 80)
    print(f"{Fore.CYAN}{'OSINT'.center(26)}|{'DISCORD'.center(26)}|{'OTHER'.center(26)}")
    print(Fore.LIGHTBLACK_EX + "=" * 80)

    print(f"{Fore.RED}[01] Show My IP".ljust(26) +
          f"{Fore.RED}[06] Server Nuker".center(26) +
          f"{Fore.RED}[08] Coming Soon...".rjust(26))
    print(f"{Fore.RED}[02] IP Info".ljust(26) +
          f"{Fore.RED}[07] Token Checker".center(26) +
          f"{Fore.RED}[09] Coming Soon...".rjust(26))
    print(f"{Fore.RED}[03] IP Pinger".ljust(26))
    print(f"{Fore.RED}[04] IP Port Scanner".ljust(26))
    print(f"{Fore.RED}[05] Website Info Scanner".ljust(26))

    # Move 'Exit' to the bottom right with the letter E
    print(f"{''.ljust(52)}{Fore.RED}[E] Exit".rjust(26))
    
    print(Fore.LIGHTBLACK_EX + "=" * 80)
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

    while True:
        print_menu()
        choice = questionary.text("[3TH1C4L] >> ", style=style).ask()

        if choice == '1':
            print(f"{Fore.LIGHTGREEN_EX}Running Show My IP...")
            show_my_ip()
        elif choice == '2':
            print(f"{Fore.LIGHTGREEN_EX}Running IP Info...")
            ip_info()
        elif choice == '3':
            print(f"{Fore.LIGHTGREEN_EX}Running IP Pinger...")
            run_ip_pinger()
        elif choice == '4':
            print(f"{Fore.LIGHTGREEN_EX}Running IP Port Scanner...")
            ip_port_scanner()
        elif choice == '5':
            print(f"{Fore.LIGHTGREEN_EX}Running Website Info Scanner...")
            website_info_scanner()   
        elif choice == '7':
            token_discord = input(f"{Fore.LIGHTGREEN_EX}Enter Discord token: {Fore.RESET}")
            print(f"{Fore.LIGHTGREEN_EX}Checking token...")
            check_token(token_discord)
        elif choice.lower() == 'e':  # Accept both 'E' and 'e'
            print(f"{Fore.LIGHTGREEN_EX}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid choice. Please select a valid option.")

        input(f"{Fore.LIGHTGREEN_EX}Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    run_tool()
