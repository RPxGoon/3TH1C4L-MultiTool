import requests
from colorama import Fore

def run():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        data = response.json()
        print(f"{Fore.RED}[+]{Fore.GREEN} Your Public IP Address: {Fore.RED}[{data['ip']}]")
    except Exception as e:
        print(f"{Fore.RED}[!]{Fore.GREEN} Error Fetching Your IP Address... Please Check Your Connection: {Fore.RED}[{e}]{Fore.RESET}")
