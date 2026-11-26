import base64
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)


def run():
    print(f"{Fore.RED}[*] {Fore.GREEN}Select Mode:")
    print(f"  {Fore.RED}[{Fore.MAGENTA}1{Fore.RED}] {Fore.GREEN}Encode")
    print(f"  {Fore.RED}[{Fore.MAGENTA}2{Fore.RED}] {Fore.GREEN}Decode")
    mode = input(f"{Fore.RED}[*] {Fore.GREEN}Mode (1/2): {Fore.RESET}").strip()

    if mode not in ("1", "2"):
        print(f"{Fore.RED}[!] {Fore.YELLOW}Invalid Mode. Exiting...")
        return

    text = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Text: {Fore.RESET}")
    if text == "":
        print(f"{Fore.RED}[!] {Fore.YELLOW}No Input Provided. Exiting...")
        return

    try:
        if mode == "1":
            result = base64.b64encode(text.encode("utf-8")).decode("utf-8")
            print(f"\n{Fore.RED}[+] {Fore.GREEN}Encoded: {Fore.CYAN}{result}")
        else:
            padded = text + "=" * (-len(text) % 4)
            result = base64.b64decode(padded).decode("utf-8", errors="replace")
            print(f"\n{Fore.RED}[+] {Fore.GREEN}Decoded: {Fore.CYAN}{result}")
    except Exception as e:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Operation Failed: {Fore.CYAN}{e}")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
