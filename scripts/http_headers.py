import requests
import urllib3
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Security headers worth flagging when present / missing.
SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]


def run():
    url = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Target Website/URL: {Fore.RESET}").strip()
    if not url:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Invalid URL. Exiting...")
        return
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=8, verify=False, allow_redirects=True)
    except requests.RequestException as e:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Request Failed: {Fore.CYAN}{e}")
        return

    print(f"\n{Fore.RED}[+] {Fore.GREEN}Final URL: {Fore.CYAN}{response.url}")
    print(f"{Fore.RED}[+] {Fore.GREEN}Status Code: {Fore.CYAN}{response.status_code}\n")

    print(f"{Fore.RED}[*] {Fore.GREEN}Response Headers:")
    for key, value in response.headers.items():
        print(f"  {Fore.RED}[+] {Fore.MAGENTA}{key}: {Fore.CYAN}{value}")

    print(f"\n{Fore.RED}[*] {Fore.GREEN}Security Header Audit:")
    for header in SECURITY_HEADERS:
        if header in response.headers:
            print(f"  {Fore.GREEN}[+] {header}: Present")
        else:
            print(f"  {Fore.RED}[-] {Fore.YELLOW}{header}: Missing")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
