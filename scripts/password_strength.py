import math
import string
import getpass
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

COMMON = {
    "password", "123456", "123456789", "qwerty", "111111", "12345678",
    "abc123", "password1", "iloveyou", "admin", "welcome", "letmein",
    "monkey", "dragon", "000000", "qwerty123",
}


def charset_size(password):
    size = 0
    if any(c in string.ascii_lowercase for c in password):
        size += 26
    if any(c in string.ascii_uppercase for c in password):
        size += 26
    if any(c in string.digits for c in password):
        size += 10
    if any(c in string.punctuation for c in password):
        size += len(string.punctuation)
    if any(c == " " for c in password):
        size += 1
    return size


def rating(entropy):
    if entropy < 28:
        return "Very Weak", Fore.RED
    if entropy < 36:
        return "Weak", Fore.LIGHTRED_EX
    if entropy < 60:
        return "Reasonable", Fore.YELLOW
    if entropy < 128:
        return "Strong", Fore.GREEN
    return "Very Strong", Fore.LIGHTGREEN_EX


def run():
    password = getpass.getpass(f"{Fore.RED}[*] {Fore.GREEN}Enter Password (hidden): ")
    if not password:
        print(f"{Fore.RED}[!] {Fore.YELLOW}No Password Provided. Exiting...")
        return

    size = charset_size(password)
    entropy = len(password) * math.log2(size) if size else 0
    label, color = rating(entropy)

    print(f"\n{Fore.RED}[+] {Fore.GREEN}Length: {Fore.CYAN}{len(password)}")
    print(f"{Fore.RED}[+] {Fore.GREEN}Character Pool: {Fore.CYAN}{size}")
    print(f"{Fore.RED}[+] {Fore.GREEN}Estimated Entropy: {Fore.CYAN}{entropy:.1f} bits")
    print(f"{Fore.RED}[+] {Fore.GREEN}Rating: {color}{label}")

    if password.lower() in COMMON:
        print(f"{Fore.RED}[!] {Fore.YELLOW}This is a commonly used password - avoid it entirely!")

    tips = []
    if len(password) < 12:
        tips.append("Use at least 12 characters.")
    if not any(c in string.ascii_uppercase for c in password):
        tips.append("Add uppercase letters.")
    if not any(c in string.digits for c in password):
        tips.append("Add numbers.")
    if not any(c in string.punctuation for c in password):
        tips.append("Add special characters.")
    if tips:
        print(f"\n{Fore.RED}[*] {Fore.GREEN}Suggestions:")
        for t in tips:
            print(f"  {Fore.RED}[>] {Fore.MAGENTA}{t}")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
