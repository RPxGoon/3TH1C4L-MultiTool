import os
import sys
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Import the Show My IP, IP Info Lookup, and IP Pinger functions
from scripts.show_my_ip import run as show_my_ip
from scripts.ip_info_lookup import run as ip_info_lookup
from scripts.ip_pinger import run_ip_pinger

# Define a smooth gradient function for text
def smooth_gradient_print(text, start_color, end_color, steps):
    r_start, g_start, b_start = start_color
    r_end, g_end, b_end = end_color
    for i, char in enumerate(text):
        r = int(r_start + (r_end - r_start) * (i / steps))
        g = int(g_start + (g_end - g_start) * (i / steps))
        b = int(b_start + (b_end - b_start) * (i / steps))
        color = f'\033[38;2;{r};{g};{b}m'
        print(f"{color}{char}", end="")
    print()

# Define the colors (from red to purple)
start_color = (255, 0, 0)
end_color = (128, 0, 128)

def print_ascii_logo():
    logo = r"""
                   )                      (     
     )   *   )  ( /(     )    (        )  )\ )  
  ( /( ` )  /(  )\()) ( /(    )\    ( /( (()/(  
  )\()) ( )(_))((_)\  )\()) (((_)   )\()) /(_)) 
 ((_)\ (_(_())  _((_)((_)\  )\___  ((_)\ (_))   
|__ (_)|_   _| | || | / (_)((/ __|| | (_)| |    
 |_ \    | |   | __ | | |   | (__ |_  _| | |__  
|___/    |_|   |_||_| |_|    \___|  |_|  |____| 
                                               
                [3TH1C4L x RPxGoon]
	 Simple OSINT / Discord Multi-tool
			     
    """
    smooth_gradient_print(logo, start_color, end_color, len(logo))

def run_tool():
    while True:
        # Print the logo with gradient
        print_ascii_logo()

        # Show menu with gradient text
        print(f"{Fore.GREEN}Select an option:")

        # Menu options (color gradient will be applied)
        print(f"{Fore.RED}1.) Show My IP Address")
        print(f"{Fore.RED}2.) IP Info Lookup")
        print(f"{Fore.RED}3.) IP Pinger")
        print(f"{Fore.RED}4.) Exit")
        
        # Get the user's choice (input prompt stays green)
        choice = input(f"{Fore.GREEN}Enter Your Choice: ")

        if choice == '1':
            show_my_ip()  # Calls the run() function from the show_my_ip module
        elif choice == '2':
            ip_info_lookup()  # Calls the run() function from the ip_info_lookup module
        elif choice == '3':  
            run_ip_pinger()  # Calls the run_ip_pinger() function from the ip_pinger module
        elif choice == '4':
            print(f"{Fore.GREEN}Exiting... Goodbye!")  # Exit message with gradient color
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option.")

        input(f"{Fore.GREEN}Press Enter to continue...")  # Prompt for continue (input stays green)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen after selection

if __name__ == "__main__":
    run_tool()
