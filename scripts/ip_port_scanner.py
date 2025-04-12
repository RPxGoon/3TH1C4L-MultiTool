import socket
import concurrent.futures
from colorama import Fore 
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
def port_scanner(ip):
    port_protocol_map = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
        1521: "Oracle DB", 3389: "RDP"
    }

    def scan_port(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.1)
                if sock.connect_ex((ip, port)) == 0:
                    protocol = port_protocol_map.get(port, "Unknown")
                    print(f"{Fore.GREEN}[+] Port {port} is OPEN ({protocol})")  
        except Exception:
            pass

    print(f"{Fore.RED}[*] {Fore.GREEN}Scanning IP: {ip} (Ports 1-1024)...")  
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda p: scan_port(ip, p), range(1, 1025)) 
    print(f"{Fore.RED}[*] {Fore.GREEN}Scan Complete!")  

def run(): 
    ip = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Target IP Address: {Fore.RESET}").strip() 
    if not ip:
        print(f"{Fore.RED}[!] {Fore.GREEN}Invalid IP Address. Exiting...") 
        return
    port_scanner(ip)

                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --