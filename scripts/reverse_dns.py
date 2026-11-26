import socket
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)


def run():
    target = input(f"{Fore.RED}[*] {Fore.GREEN}Enter IP Address or Hostname: {Fore.RESET}").strip()
    if not target:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Invalid Input. Exiting...")
        return

    # Forward resolve (hostname -> IP)
    try:
        ip = socket.gethostbyname(target)
        print(f"{Fore.RED}[+] {Fore.GREEN}Resolved IP: {Fore.CYAN}{ip}")
    except socket.gaierror:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Unable to Resolve: {Fore.CYAN}{target}")
        return

    # Reverse resolve (IP -> hostname) + aliases
    try:
        hostname, aliases, addresses = socket.gethostbyaddr(ip)
        print(f"{Fore.RED}[+] {Fore.GREEN}Hostname: {Fore.CYAN}{hostname}")
        if aliases:
            print(f"{Fore.RED}[+] {Fore.GREEN}Aliases: {Fore.CYAN}{', '.join(aliases)}")
        if addresses:
            print(f"{Fore.RED}[+] {Fore.GREEN}Addresses: {Fore.CYAN}{', '.join(addresses)}")
    except (socket.herror, socket.gaierror):
        print(f"{Fore.RED}[-] {Fore.YELLOW}No Reverse DNS (PTR) Record Found for {Fore.CYAN}{ip}")
    except Exception as e:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Error: {e}")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
