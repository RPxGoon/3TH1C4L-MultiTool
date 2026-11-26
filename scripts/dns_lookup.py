import dns.resolver
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA"]


def run():
    domain = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Target Domain: {Fore.RESET}").strip()
    if not domain:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Invalid Domain. Exiting...")
        return

    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]
    print(f"\n{Fore.RED}[+] {Fore.GREEN}DNS Records for: {Fore.CYAN}{domain}\n")

    found_any = False
    for record_type in RECORD_TYPES:
        try:
            answers = dns.resolver.resolve(domain, record_type, raise_on_no_answer=False)
            if not answers.rrset:
                continue
            for rdata in answers:
                found_any = True
                print(f"{Fore.RED}[+] {Fore.MAGENTA}{record_type:<6}{Fore.GREEN}-> {Fore.CYAN}{rdata.to_text()}")
        except (dns.resolver.NoAnswer, dns.resolver.NoNameservers):
            continue
        except dns.resolver.NXDOMAIN:
            print(f"{Fore.RED}[!] {Fore.YELLOW}Domain Does Not Exist (NXDOMAIN).")
            return
        except Exception:
            continue

    if not found_any:
        print(f"{Fore.RED}[-] {Fore.YELLOW}No DNS Records Found for {Fore.CYAN}{domain}")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
