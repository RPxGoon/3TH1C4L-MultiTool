import requests
from colorama import Fore, init


init(autoreset=True)

def run():
    
    webhook_url = input(f"{Fore.RED}[*] {Fore.GREEN}Enter the Webhook URL to Delete: ")

    try:
        response = requests.delete(webhook_url)

        if response.status_code == 204:
            print()
            print(f"{Fore.RED}[+] {Fore.GREEN}Webhook Successfully Deleted :)")
        elif response.status_code == 404:
            print(f"{Fore.RED}[x] {Fore.RED}Webhook Not Found or Already Deleted.")
        else:
            print(f"{Fore.RED}[x] {Fore.RED}Failed to Delete Webhook. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[!] {Fore.RED}Error: {e}")

# Run the function
if __name__ == "__main__":
    run()
