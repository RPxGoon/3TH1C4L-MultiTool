import os
import sys
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Import the Show My IP, IP Info Lookup, and IP Pinger functions
from scripts.show_my_ip import run as show_my_ip
from scripts.ip_info_lookup import run as ip_info_lookup
from scripts.ip_pinger import run_ip_pinger
from scripts.token_checker import check_token  # Import the token checker

# Define a smooth gradient function for text
def smooth_gradient_print(text, start_color, end_color, steps):
    if steps == 0:  # Prevent division by zero for empty lines
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

# Center text helper function
def center_text(text, width=80):
    return text.center(width)

# Define the colors (red to purple gradient)
start_color = (255, 0, 0)
end_color = (128, 0, 128)

# Function to print the ASCII logo
def print_ascii_logo():
    logo = r"""
                   )                      (     
     )   *   )  ( /(     )    (        )  )\ )  
  ( /(  )  /(  )\()) ( /(    )\    ( /( (()/(  
  )\()) ( )(_))((_\  )\()) (((_)   )\()) /(_)) 
 ((_\ (_(_())  _((_)((_\  )\___  ((_\ (_))   
|__ (_)|_   _| | || | / (_)((/ __|| | (_)| |    
 |_ \    | |   | __ | | |   | (__ |_  _| | |__  
|___/    |_|   |_||_| |_|    \___|  |_|  |____| 
                                               
          [3TH1C4L x RPxGoon]
        Simple OSINT / Discord Multi-tool
    """
    for line in logo.splitlines():
        smooth_gradient_print(center_text(line), start_color, end_color, len(line))

# Function to print the main menu
def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_ascii_logo()

    print(Fore.LIGHTBLACK_EX + "=" * 80)
    print(f"{Fore.CYAN}{'OSINT'.center(26)}|{'DISCORD'.center(26)}|{'OTHER'.center(26)}")
    print(Fore.LIGHTBLACK_EX + "=" * 80)

    print(f"{Fore.RED}[01] Show My IP".ljust(26) +
          f"{Fore.RED}[04] Token Checker".center(26) +
          f"{Fore.RED}[07] Exit".rjust(26))

    print(f"{Fore.RED}[02] IP Info Lookup".ljust(26) +
          f"{Fore.RED}[05] Server Nuker".center(26) +
          f"{Fore.RED}[08] Coming Soon...".rjust(26))

    print(f"{Fore.RED}[03] IP Pinger".ljust(26) +
          f"{Fore.RED}[06] Mass DM Tool".center(26) +
          f"{Fore.RED}[09] Coming Soon...".rjust(26))

    print(Fore.LIGHTBLACK_EX + "=" * 80)
    print()

# Main function to run the tool
def run_tool():
    while True:
        print_menu()

        # Linux terminal-like prompt
        choice = input(f"{Fore.LIGHTGREEN_EX}3TH1C4L > {Fore.RESET}")

        if choice == '1':
            show_my_ip()
        elif choice == '2':
            ip_info_lookup()
        elif choice == '3':
            run_ip_pinger()
        elif choice == '4':
            # Token checker option
            token_discord = input(f"{Fore.LIGHTYELLOW_EX}Enter your Discord token: {Fore.RESET}")
            check_token(token_discord)  # Call the token checker
        elif choice == '7':
            print(f"{Fore.LIGHTGREEN_EX}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid choice. Please select a valid option.")

        input(f"{Fore.LIGHTBLACK_EX}Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

# Run the tool if this script is executed directly
if __name__ == "__main__":
    run_tool()
