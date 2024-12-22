import socket
import concurrent.futures
import requests
from urllib.parse import urlparse
import ssl
import urllib3
from requests.exceptions import RequestException
import time
import dns.resolver
from bs4 import BeautifulSoup
import whois
from colorama import Fore, init


init(autoreset=True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


BEFORE = '\033[1m'
AFTER = '\033[0m'
ADD = '\033[92m'  
white = '\033[97m'
red = '\033[91m'

def current_time_hour():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def website_info_scanner(website_url):
    if not urlparse(website_url).scheme:
        website_url = "https://" + website_url

    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} [+] Scanning Website: {white}{website_url}{red}")

    def website_domain(website_url):
        parsed_url = urlparse(website_url)
        domain = parsed_url.netloc or website_url
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} [+] Domain: {white}{domain}{red}")
        return domain

    def website_ip(domain):
        try:
            ip = socket.gethostbyname(domain)
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} [+] IP: {white}{ip}{red}")
            return ip
        except socket.gaierror:
            print(f"{BEFORE + current_time_hour() + AFTER} {red}[!] Error: Unable to Resolve IP for {domain}{red}")
            return None

    def ip_type(ip):
        if ':' in ip:
            ip_type = "IPv6"
        elif '.' in ip:
            ip_type = "IPv4"
        else:
            ip_type = "Unknown"
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} [+] IP Type: {white}{ip_type}{red}")

    def website_secure(website_url):
        secure = website_url.startswith("https://")
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} [+] Secure: {white}{secure}{red}")

    def website_status(website_url):
        try:
            response = requests.get(website_url, timeout=5, verify=False)
            status_code = response.status_code
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} [+] Status Code: {white}{status_code}{red}")
        except RequestException as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {red}[!] Error: Unable to get Status for {website_url} ({e}){red}")

    def ip_info(ip):
        if not ip:
            return
        api_url = f"https://ipinfo.io/{ip}/json"
        try:
            response = requests.get(api_url, timeout=5)
            api = response.json()
            for key, value in api.items():
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {key.capitalize()}: {white}{value}{red}")
        except RequestException as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {red}[!] Error: Unable to get IP Info for {ip} ({e}){red}")

    def website_port(ip):
        if not ip:
            return
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP", 443: "HTTPS"
        }
        port_list = [21, 22, 23, 25, 53, 80, 443]

        def scan_port(ip, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    protocol = port_protocol_map.get(port, "Unknown")
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} [+] Port: {white}{port}{red} [+] Status: {white}Open{red} [+] Protocol: {white}{protocol}{red}")
                sock.close()
            except Exception:
                pass

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda port: scan_port(ip, port), port_list)

    
    domain = website_domain(website_url)
    ip = website_ip(domain)
    if ip:
        ip_type(ip)
        website_secure(website_url)
        website_status(website_url)
        ip_info(ip)
        website_port(ip)

def run():
    website_url = input(f"{Fore.LIGHTGREEN_EX}[*] Enter Target Website/URL: {Fore.RESET}").strip()
    if not website_url:
        print(f"{Fore.RED}[!] Invalid Website/URL. Exiting...{Fore.RESET}")
        return
    website_info_scanner(website_url)
