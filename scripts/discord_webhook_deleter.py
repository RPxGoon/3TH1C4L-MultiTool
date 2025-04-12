import requests
from colorama import Fore, init

                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
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

                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
