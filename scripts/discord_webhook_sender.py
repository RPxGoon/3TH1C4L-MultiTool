import requests
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)


def run():
    webhook_url = input(f"{Fore.RED}[*] {Fore.GREEN}Enter the Webhook URL: ").strip()
    if not webhook_url.startswith("https://"):
        print(f"{Fore.RED}[!] {Fore.YELLOW}Invalid Webhook URL. Exiting...")
        return

    message = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Message to Send: ")
    if not message.strip():
        print(f"{Fore.RED}[!] {Fore.YELLOW}Message Cannot Be Empty. Exiting...")
        return

    username = input(f"{Fore.RED}[*] {Fore.GREEN}Custom Username (Leave Empty to Skip): ").strip()

    payload = {"content": message}
    if username:
        payload["username"] = username

    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        if response.status_code in (200, 204):
            print(f"\n{Fore.RED}[+] {Fore.GREEN}Message Successfully Sent :)")
        elif response.status_code == 404:
            print(f"{Fore.RED}[x] {Fore.YELLOW}Webhook Not Found or Deleted.")
        elif response.status_code == 429:
            print(f"{Fore.RED}[x] {Fore.YELLOW}Rate Limited by Discord. Try Again Later.")
        else:
            print(f"{Fore.RED}[x] {Fore.YELLOW}Failed to Send. Status Code: {Fore.CYAN}{response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Error: {Fore.CYAN}{e}")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
