import requests
from colorama import Fore, init
import os
import json
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

def extract_webhooks(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"{Fore.RED}[!] File not found: {file_path}")
            return []
        
        with open(file_path, 'r') as file:
            for _ in range(2):
                next(file, None)
            webhooks = [line.strip() for line in file if line.strip()]
        return webhooks
    except Exception as e:
        print(f"{Fore.RED}[!] Error reading webhooks file: {e}")
        return []

def display_webhooks(webhooks):
    print(f"\n{Fore.GREEN}Available Webhooks:")
    for i, webhook in enumerate(webhooks, 1):
        short_webhook = webhook[:50] + "..." if len(webhook) > 50 else webhook
        print(f"{Fore.RED}[{Fore.MAGENTA}{i}{Fore.RED}] -> {Fore.GREEN}URL: {Fore.RED}{short_webhook}{Fore.RESET}")

def get_webhook_info(webhook_url):
    try:
        headers = {
            'Content-Type': 'application/json',
        }
        
        response = requests.get(webhook_url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            info = {
                "name": data.get("name", "None"),
                "id": data.get("id", "None"),
                "token": data.get("token", "None"),
                "avatar": data.get("avatar", "None"),
                "type": "bot" if data.get("type") == 1 else "webhook utilisateur",
                "channel_id": data.get("channel_id", "None"),
                "guild_id": data.get("guild_id", "None"),
                "application_id": data.get("application_id", "None")
            }
            
            if 'user' in data:
                user = data['user']
                raw_flags = user.get("flags", "None")
                info.update({
                    "user_id": user.get("id", "None"),
                    "username": user.get("username", "None"),
                    "global_name": user.get("global_name", "None"),
                    "discriminator": user.get("discriminator", "None"),
                    "user_avatar": user.get("avatar", "None"),
                    "flags": f"{raw_flags} (Public: {raw_flags})",
                    "accent_color": user.get("accent_color", "None"),
                    "avatar_decoration": user.get("avatar_decoration_data", "None"),
                    "banner": user.get("banner", "None"),
                    "banner_color": user.get("banner_color", "None")
                })
            
            return info, True
        else:
            print(f"{Fore.RED}[!] Failed to get webhook info (Status: {response.status_code})")
            return None, False
            
    except Exception as e:
        print(f"{Fore.RED}[!] Error fetching webhook info: {e}")
        return None, False

def display_webhook_info(info):
    print(f"""
{Fore.RED}[+] {Fore.GREEN}Name         : {Fore.RED}{info.get('name', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}ID           : {Fore.RED}{info.get('id', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Token        : {Fore.RED}{info.get('token', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Type         : {Fore.RED}{info.get('type', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Channel ID   : {Fore.RED}{info.get('channel_id', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Server ID    : {Fore.RED}{info.get('guild_id', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Avatar       : {Fore.RED}{info.get('avatar', 'None')}{Fore.RESET}""")

    if 'user_id' in info:
        print(f"""
{Fore.RED}[+] {Fore.GREEN}User Information:
{Fore.RED}[+] {Fore.GREEN}User ID      : {Fore.RED}{info.get('user_id', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Username     : {Fore.RED}{info.get('username', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Display Name : {Fore.RED}{info.get('global_name', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Number       : {Fore.RED}{info.get('discriminator', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Avatar       : {Fore.RED}{info.get('user_avatar', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Flags        : {Fore.RED}{info.get('flags', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Color        : {Fore.RED}{info.get('accent_color', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Decoration   : {Fore.RED}{info.get('avatar_decoration', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Banner       : {Fore.RED}{info.get('banner', 'None')}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Banner Color : {Fore.RED}{info.get('banner_color', 'None')}{Fore.RESET}""")

def run():
    webhooks_file_path = "input/discord-webhooks.txt"
    webhooks = extract_webhooks(webhooks_file_path)
    
    if not webhooks:
        print(f"{Fore.RED}[!] No webhooks found in /input/discord-webhooks.txt  -  Exiting...")
        return
    
    display_webhooks(webhooks)
    choice = input(f"{Fore.RED}[+] {Fore.GREEN}Select Webhook >> ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(webhooks):
        selected_webhook = webhooks[int(choice) - 1]
        info, success = get_webhook_info(selected_webhook)
        
        if success and info:
            display_webhook_info(info)
    else:
        print(f"{Fore.RED}[!] Invalid choice. Exiting...")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()