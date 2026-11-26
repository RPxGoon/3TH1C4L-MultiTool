import re
import requests
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

MAC_RE = re.compile(r"^[0-9A-Fa-f]{2}([:-]?[0-9A-Fa-f]{2}){5}$")


def run():
    mac = input(f"{Fore.RED}[*] {Fore.GREEN}Enter MAC Address: {Fore.RESET}").strip()
    if not MAC_RE.match(mac):
        print(f"{Fore.RED}[!] {Fore.YELLOW}Invalid MAC Address Format. Example: {Fore.CYAN}00:1A:2B:3C:4D:5E")
        return

    clean = re.sub(r"[^0-9A-Fa-f]", "", mac).upper()
    oui = ":".join(clean[i:i + 2] for i in range(0, 6, 2))
    print(f"\n{Fore.RED}[+] {Fore.GREEN}OUI (Vendor Prefix): {Fore.CYAN}{oui}")

    try:
        response = requests.get(f"https://api.macvendors.com/{clean}", timeout=8)
        if response.status_code == 200 and response.text.strip():
            print(f"{Fore.RED}[+] {Fore.GREEN}Vendor: {Fore.CYAN}{response.text.strip()}")
        elif response.status_code == 404:
            print(f"{Fore.RED}[-] {Fore.YELLOW}Vendor Not Found in Database.")
        else:
            print(f"{Fore.RED}[!] {Fore.YELLOW}Lookup Returned Status: {Fore.CYAN}{response.status_code}")
    except requests.RequestException as e:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Lookup Failed: {Fore.CYAN}{e}")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
