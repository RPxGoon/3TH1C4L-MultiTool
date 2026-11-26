import hashlib
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

ALGORITHMS = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]


def run():
    text = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Text to Hash: {Fore.RESET}")
    if text == "":
        print(f"{Fore.RED}[!] {Fore.YELLOW}No Input Provided. Exiting...")
        return

    data = text.encode("utf-8")
    print(f"\n{Fore.RED}[+] {Fore.GREEN}Hashes for Input:\n")
    for algo in ALGORITHMS:
        digest = hashlib.new(algo, data).hexdigest()
        print(f"{Fore.RED}[+] {Fore.MAGENTA}{algo.upper():<8}{Fore.GREEN}-> {Fore.CYAN}{digest}")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
