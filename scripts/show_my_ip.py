import requests
from colorama import Fore
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
def run():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        data = response.json()
        print(f"{Fore.RED}[+]{Fore.GREEN} Your Public IP Address: {Fore.RED}[{data['ip']}]")
    except Exception as e:
        print(f"{Fore.RED}[!]{Fore.GREEN} Error Fetching Your IP Address... Please Check Your Connection: {Fore.RED}[{e}]{Fore.RESET}")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --