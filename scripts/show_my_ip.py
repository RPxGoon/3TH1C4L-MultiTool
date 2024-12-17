import requests
from colorama import Fore

def run():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        data = response.json()
        print(f"{Fore.GREEN}Your IP Address: {data['ip']}")
    except Exception as e:
        print(f"{Fore.GREEN}Error fetching IP address: {e}")
