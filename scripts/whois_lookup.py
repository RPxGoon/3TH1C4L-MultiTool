import whois
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

FIELDS = [
    ("Domain Name", "domain_name"),
    ("Registrar", "registrar"),
    ("WHOIS Server", "whois_server"),
    ("Creation Date", "creation_date"),
    ("Expiration Date", "expiration_date"),
    ("Updated Date", "updated_date"),
    ("Name Servers", "name_servers"),
    ("Status", "status"),
    ("Emails", "emails"),
    ("Registrant Org", "org"),
    ("Country", "country"),
]


def _fmt(value):
    if isinstance(value, (list, tuple, set)):
        unique = []
        for item in value:
            item = str(item)
            if item not in unique:
                unique.append(item)
        return ", ".join(unique)
    return str(value)


def run():
    domain = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Target Domain: {Fore.RESET}").strip()
    if not domain:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Invalid Domain. Exiting...")
        return

    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]
    print(f"\n{Fore.RED}[+] {Fore.GREEN}WHOIS Lookup for: {Fore.CYAN}{domain}\n")

    try:
        data = whois.whois(domain)
    except Exception as e:
        print(f"{Fore.RED}[!] {Fore.YELLOW}WHOIS Lookup Failed: {Fore.CYAN}{e}")
        return

    if not data or not data.get("domain_name"):
        print(f"{Fore.RED}[-] {Fore.YELLOW}No WHOIS Data Found for {Fore.CYAN}{domain}")
        return

    for label, key in FIELDS:
        value = data.get(key)
        if value:
            print(f"{Fore.RED}[+] {Fore.GREEN}{label:<16}: {Fore.CYAN}{_fmt(value)}")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
