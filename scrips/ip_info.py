import requests
from colorama import Fore

def run():
    ip_address = input(f"{Fore.GREEN}Enter the IP address: ")
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        for key, value in data.items():
            print(f"{Fore.GREEN}{key.capitalize()}: {value}")
    except Exception as e:
        print(f"{Fore.GREEN}Error fetching IP information: {e}")
