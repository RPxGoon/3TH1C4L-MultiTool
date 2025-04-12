import socket
import time
from colorama import Fore
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
def ping_ip(hostname, port, bytes):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        start_time = time.time()
        sock.connect((hostname, port))
        data = b'\x00' * bytes
        sock.sendall(data)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"{Fore.RED}[+] {Fore.GREEN}Hostname: {hostname}  {Fore.RED}[+] {Fore.GREEN}Time: {elapsed_time:.2f}ms   {Fore.RED}[+] {Fore.GREEN}Port: {port}   {Fore.RED}[+] {Fore.GREEN}Bytes: {bytes}   {Fore.GREEN}[=] Status: Succeed")
    except:
        elapsed_time = 0
        print(f"{Fore.RED}[+] {Fore.GREEN}Hostname: {hostname}  {Fore.RED}[+] {Fore.GREEN}Time: {elapsed_time}ms   {Fore.RED}[+] {Fore.GREEN}Port: {port}   {Fore.RED}[+] {Fore.GREEN}Bytes: {bytes}   {Fore.RED}[=] Status: Fail")

def run_ip_pinger():
    
    hostname = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Target IP or Hostname: ")

    try:
        port_input = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Port (default is 80): ")
        if port_input.strip():
            port = int(port_input)
        else:
            port = 80

        bytes_input = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Bytes (default is 64): ")
        if bytes_input.strip():
            bytes = int(bytes_input)
        else:
            bytes = 64
    except Exception as e:
        print(f"{Fore.RED}[!] Error: Invalid Input for Port or Bytes: {e}")
        return
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
    while True:
        ping_ip(hostname, port, bytes)
