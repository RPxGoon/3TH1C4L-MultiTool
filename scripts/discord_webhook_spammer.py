import requests
from colorama import Fore, init
import os
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)

def extract_webhooks(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"{Fore.RED}[!] File not found: {file_path}")
            return []
        
        with open(file_path, 'r') as file:
            
            for _ in range(2):
                next(file, None)
            # Read remaining lines
            webhooks = [line.strip() for line in file if line.strip()]
        return webhooks
    except Exception as e:
        print(f"{Fore.RED}[!] Error reading webhooks file: {e}")
        return []

def display_webhooks(webhooks):
    print(f"\n{Fore.RED}[*] {Fore.GREEN}Available Webhooks:")
    for i, webhook in enumerate(webhooks, 1):
        print(f"{Fore.RED}[{i}] {Fore.GREEN}{webhook}")

def spam_single_message(webhook, message):
    try:
        response = requests.post(webhook, json={"content": message})
        if response.status_code == 429:  
            retry_after = float(response.headers.get('Retry-After', 0.5))
            time.sleep(retry_after)
            # Retry the request
            response = requests.post(webhook, json={"content": message})
        
        if response.status_code == 204:
            print(f"{Fore.GREEN}[*] Successfully sent message to webhook: {Fore.RED}{webhook}{Fore.RESET}")
        else:
            print(f"{Fore.RED}[!] Failed to send message to webhook: {Fore.RED}{webhook} (Status: {response.status_code}){Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error sending message to webhook: {e}")

def spam_webhook(webhook, message, count=1):
    with ThreadPoolExecutor(max_workers=7) as executor: 
        futures = [
            executor.submit(spam_single_message, webhook, message)
            for _ in range(count)
        ]
        for _ in as_completed(futures):
            pass


def run():
    webhooks_file_path = "input/discord-webhooks.txt"
    webhooks = extract_webhooks(webhooks_file_path)
    
    if not webhooks:
        print(f"{Fore.RED}[!] No webhooks found in /input/discord-webhooks.txt  -  Exiting...")
        return
    
    display_webhooks(webhooks)
    
    choice = input(f"\n{Fore.RED}[*] {Fore.GREEN}Select webhook or enter 'A' to use all: ").strip()
    
    if choice.lower() == 'a':
        selected_webhooks = webhooks 
    elif choice.isdigit() and 1 <= int(choice) <= len(webhooks):
        selected_webhooks = [webhooks[int(choice) - 1]]  
    else:
        print(f"{Fore.RED}[!] Invalid choice. Exiting...")
        return
    
    message = input(f"\n{Fore.RED}[+] {Fore.GREEN}Message -> ").strip()
    count = input(f"\n{Fore.RED}[+] {Fore.GREEN}Number of messages to send -> ").strip()
    
    try:
        count = int(count)
        if count < 1:
            raise ValueError
    except ValueError:
        print(f"{Fore.RED}[!] Invalid number. Exiting...")
        return
    
    for webhook in selected_webhooks:
        spam_webhook(webhook, message, count)
    
    print(f"\n{Fore.RED}[*] {Fore.LIGHTGREEN_EX}Finished sending {count} messages to {len(selected_webhooks)} webhook(s)!")

if __name__ == "__main__":
    run()