import os
import sys
from colorama import init, Fore

init(autoreset=True)


from scripts.show_my_ip import run as show_my_ip
from scripts.ip_info import run as ip_info
from scripts.ip_pinger import run_ip_pinger
from scripts.token_checker import check_token  


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
        print(f"{color}{char}", end="")
    print()


def center_text(text, width=80):
    return text.center(width)


start_color = (255, 0, 0)
end_color = (128, 0, 128)


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
/* ||                                  ░                               || */
/* ++------------------------------------------------------------------++ */
/* ++------------------------------------------------------------------++ */

Simple OSINT / Discord Multi-tool
[https://github.com/RPxGoon/3TH1C4L-MultiTool]
    """
    for line in logo.splitlines():
        smooth_gradient_print(center_text(line), start_color, end_color, len(line))


def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_ascii_logo()

    print(Fore.LIGHTBLACK_EX + "=" * 80)
    print(f"{Fore.CYAN}{'OSINT'.center(26)}|{'DISCORD'.center(26)}|{'OTHER'.center(26)}")
    print(Fore.LIGHTBLACK_EX + "=" * 80)

    print(f"{Fore.RED}[01] Show My IP".ljust(26) +
          f"{Fore.RED}  [04] Token Checker".center(26) +
          f"{Fore.RED}[07] Exit".rjust(26)) 

    print(f"{Fore.RED}[02] IP Info".ljust(26) +
          f"{Fore.RED}[05] Server Nuker".center(26) +
          f"{Fore.RED}[08] Coming Soon...".rjust(26))

    print(f"{Fore.RED}[03] IP Pinger".ljust(26) +
          f"{Fore.RED}[06] Mass DM Tool".center(26) +
          f"{Fore.RED}[09] Coming Soon...".rjust(26))

    print(Fore.LIGHTBLACK_EX + "=" * 80)
    print()


def run_tool():
    while True:
        print_menu()

        
        choice = input(f"{Fore.LIGHTGREEN_EX}3TH1C4L > {Fore.RESET}")

        if choice == '1':
            show_my_ip()
        elif choice == '2':
            ip_info()
        elif choice == '3':
            run_ip_pinger()
        elif choice == '4':
            
            token_discord = input(f"{Fore.LIGHTYELLOW_EX}Enter Discord token: {Fore.RESET}")
            check_token(token_discord)  
        elif choice == '7':
            print(f"{Fore.LIGHTGREEN_EX}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid choice. Please select a valid option.")

        input(f"{Fore.LIGHTBLACK_EX}Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    run_tool()
