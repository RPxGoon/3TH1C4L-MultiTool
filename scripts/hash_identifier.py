import re
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

HEX = re.compile(r"^[a-fA-F0-9]+$")

# Length (hex chars) -> possible algorithms
HEX_LENGTHS = {
    32: ["MD5", "MD4", "NTLM", "LM"],
    40: ["SHA-1", "RIPEMD-160"],
    56: ["SHA-224", "SHA3-224"],
    64: ["SHA-256", "SHA3-256", "BLAKE2s"],
    96: ["SHA-384", "SHA3-384"],
    128: ["SHA-512", "SHA3-512", "BLAKE2b", "Whirlpool"],
}


def identify(value):
    guesses = []
    value = value.strip()

    if value.startswith("$2a$") or value.startswith("$2b$") or value.startswith("$2y$"):
        guesses.append("bcrypt")
    if value.startswith("$1$"):
        guesses.append("MD5 Crypt (Unix)")
    if value.startswith("$6$"):
        guesses.append("SHA-512 Crypt (Unix)")
    if value.startswith("$5$"):
        guesses.append("SHA-256 Crypt (Unix)")
    if value.startswith("$argon2"):
        guesses.append("Argon2")

    if HEX.match(value):
        guesses.extend(HEX_LENGTHS.get(len(value), []))

    return guesses


def run():
    value = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Hash to Identify: {Fore.RESET}").strip()
    if not value:
        print(f"{Fore.RED}[!] {Fore.YELLOW}No Hash Provided. Exiting...")
        return

    print(f"\n{Fore.RED}[+] {Fore.GREEN}Length: {Fore.CYAN}{len(value)} characters")
    guesses = identify(value)

    if guesses:
        print(f"{Fore.RED}[+] {Fore.GREEN}Possible Hash Types:\n")
        for guess in guesses:
            print(f"  {Fore.RED}[>] {Fore.MAGENTA}{guess}")
    else:
        print(f"{Fore.RED}[-] {Fore.YELLOW}Could Not Identify the Hash Type.")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
