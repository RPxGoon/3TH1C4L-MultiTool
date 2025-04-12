import requests
from datetime import datetime, timezone
from colorama import Fore, init
import os
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

def extract_tokens(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        tokens = [line.strip() for line in lines[2:] if line.strip()]
        return tokens
    except Exception as e:
        print(f"{Fore.RED}[!] Error reading tokens file: {e}")
        return []

def get_token_info(token):
    try:
        response = requests.get(
            'https://discord.com/api/v8/users/@me',
            headers={'Authorization': token, 'Content-Type': 'application/json'}
        )
        api = response.json()
        status = "Valid" if response.status_code == 200 else "Invalid"
        
        username_discord = api.get('username', "None") + '#' + api.get('discriminator', "None")
        return status, username_discord, token
    except:
        return "Invalid", "None", token

def display_tokens(tokens):
    token_info_list = []
    print(f"\n{Fore.GREEN}Available Tokens:")
    
    for idx, token in enumerate(tokens, start=1):
        status, username, short_token = get_token_info(token)
        short_token = token[:40] + "..." if len(token) > 40 else token  # Truncate for display
        print(f"{Fore.RED}[{Fore.MAGENTA}{idx}{Fore.RED}] -> {Fore.GREEN}Status: {Fore.RED}{status} {Fore.GREEN}| {Fore.GREEN}User: {Fore.RED}{username} {Fore.GREEN}| {Fore.GREEN}Token: {Fore.RED}{short_token}{Fore.RESET}")
        token_info_list.append((status, username, token))
    
    return token_info_list

def run():
    tokens_file_path = "input/discord-tokens.txt"
    tokens = extract_tokens(tokens_file_path)
    
    if not tokens:
        print(f"{Fore.RED}[!] No tokens found in /input/discord-tokens.txt  -  Exiting...")
        return
    
    token_info_list = display_tokens(tokens)
    
    choice = input(f"\n{Fore.RED}[+] {Fore.GREEN}Enter token choice or 'A' to use all: {Fore.RESET}").strip()
    
    if choice.lower() == 'a':
        selected_tokens = tokens 
    elif choice.isdigit() and 1 <= int(choice) <= len(tokens):
        selected_tokens = [tokens[int(choice) - 1]]  
    else:
        print(f"{Fore.RED}[!] Invalid choice. Exiting...")
        return
    print(f"{Fore.YELLOW}Fetching info for selected token(s)...")
    
    for token in selected_tokens:
        response = requests.get(
            'https://discord.com/api/v8/users/@me',
            headers={'Authorization': token, 'Content-Type': 'application/json'}
        )
        api = response.json()
        status = "Valid" if response.status_code == 200 else "Invalid"
        
        username_discord = api.get('username', "None") + '#' + api.get('discriminator', "None")
        display_name_discord = api.get('global_name', "None")
        user_id_discord = api.get('id', "None")
        email_discord = api.get('email', "None")
        email_verified_discord = api.get('verified', "None")
        phone_discord = api.get('phone', "None")
        mfa_discord = api.get('mfa_enabled', "None")
        country_discord = api.get('locale', "None")
        avatar_discord = api.get('avatar', "None")
        nitro_discord = {0: "None", 1: "Nitro Classic", 2: "Nitro Boost", 3: "Nitro Basic"}.get(api.get('premium_type', 0), "None")
        
        try:
            created_at_discord = datetime.fromtimestamp(((int(user_id_discord) >> 22) + 1420070400000) / 1000, timezone.utc)
        except:
            created_at_discord = "None"
        
        avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{avatar_discord}.png" if avatar_discord != "None" else "None"
        
        print(f"""
{Fore.RED}[+] {Fore.GREEN}Status       : {Fore.RED}{status}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Token        : {Fore.RED}{token}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Username     : {Fore.RED}{username_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Display Name : {Fore.RED}{display_name_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}ID           : {Fore.RED}{user_id_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Created      : {Fore.RED}{created_at_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Country      : {Fore.RED}{country_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Email        : {Fore.RED}{email_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Verified     : {Fore.RED}{email_verified_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Phone        : {Fore.RED}{phone_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Nitro        : {Fore.RED}{nitro_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Avatar URL   : {Fore.RED}{avatar_url_discord}{Fore.RESET}
""")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()