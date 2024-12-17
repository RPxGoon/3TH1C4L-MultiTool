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
        print(f"{Fore.GREEN}Hostname: {hostname} {Fore.RED}time: {elapsed_time:.2f}ms {Fore.RED}port: {port} {Fore.RED}bytes: {bytes} {Fore.RED}status: succeed")
    except:
        elapsed_time = 0
        print(f"{Fore.GREEN}Hostname: {hostname} {Fore.RED}time: {elapsed_time}ms {Fore.RED}port: {port} {Fore.RED}bytes: {bytes} {Fore.RED}status: fail")

def run_ip_pinger():
    print(f"{Fore.CYAN}IP Pinger - Please provide the details")
    
    hostname = input(f"{Fore.GREEN}Enter IP or Hostname: ")

    try:
        port_input = input(f"{Fore.GREEN}Enter Port (default is 80): ")
        if port_input.strip():
            port = int(port_input)
        else:
            port = 80

        bytes_input = input(f"{Fore.GREEN}Enter Bytes (default is 64): ")
        if bytes_input.strip():
            bytes = int(bytes_input)
        else:
            bytes = 64
    except Exception as e:
        print(f"{Fore.RED}Error: Invalid input for port or bytes: {e}")
        return

    while True:
        ping_ip(hostname, port, bytes)
