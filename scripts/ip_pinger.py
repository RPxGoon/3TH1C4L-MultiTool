import socket
import time
from colorama import Fore

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
        print(f"{Fore.GREEN}[+] Hostname: {hostname} {Fore.RED}[+] Time: {elapsed_time:.2f}ms {Fore.RED}[+] Port: {port} {Fore.RED}[+] Bytes: {bytes} {Fore.RED}[=] Status: Succeed")
    except:
        elapsed_time = 0
        print(f"{Fore.GREEN}[+] Hostname: {hostname} {Fore.RED}[+] Time: {elapsed_time}ms {Fore.RED}[+] Port: {port} {Fore.RED}[+] Bytes: {bytes} {Fore.RED}[=] Status: Fail")

def run_ip_pinger():
    
    hostname = input(f"{Fore.GREEN}[*] Enter Target IP or Hostname: ")

    try:
        port_input = input(f"{Fore.GREEN}[*] Enter Port (default is 80): ")
        if port_input.strip():
            port = int(port_input)
        else:
            port = 80

        bytes_input = input(f"{Fore.GREEN}[*] Enter Bytes (default is 64): ")
        if bytes_input.strip():
            bytes = int(bytes_input)
        else:
            bytes = 64
    except Exception as e:
        print(f"{Fore.RED}[!] Error: Invalid Input for Port or Bytes: {e}")
        return

    while True:
        ping_ip(hostname, port, bytes)
