import requests
import threading
from colorama import Fore, init
from datetime import datetime, timezone
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
    
    print(f"{Fore.RED}[!] WARNING: This will DELETE ALL DMs for the selected account(s)!" )
    confirm = input(f"{Fore.RED}[?] {Fore.GREEN}Are you sure you want to proceed? (y/n): {Fore.RESET}").strip().lower()
    if confirm != 'y':
        print()
        print(f"{Fore.RED}[!] Action cancelled. Exiting...")
        return
    
    for token in selected_tokens:
        def dm_deleter(token, channels):
            for channel in channels:
                try:
                    requests.delete(
                        f'https://discord.com/api/v7/channels/{channel["id"]}',
                        headers={'Authorization': token}
                    )
                    print(
                        f"{Fore.RED}[+] {Fore.RESET}Status: {Fore.RED}Deleted{Fore.RESET} | "
                        f"Channel ID: {Fore.RED}{channel['id']}{Fore.RESET}"
                    )
                except Exception as e:
                    print(
                        f"{Fore.RED}[!] Error Deleting Channel ID {Fore.MAGENTA}{channel['id']}: {e}"
                    )

        print(f"{Fore.RED}[*] {Fore.GREEN}Retrieving DM Channels...")
        channels_response = requests.get(
            "https://discord.com/api/v9/users/@me/channels",
            headers={'Authorization': token}
        )
        channels = channels_response.json()

        if not channels:
            print(f"{Fore.RED}[!] No DMs found for token: {token}.")
            continue

        print(f"{Fore.RED}[!] {Fore.RESET}Deleting All DMs for token: {token}...")
        processes = []
        for channel_batch in [channels[i:i + 3] for i in range(0, len(channels), 3)]:
            t = threading.Thread(target=dm_deleter, args=(token, channel_batch))
            t.start()
            processes.append(t)

        for process in processes:
            process.join()

        print(f"{Fore.RED}[+] {Fore.GREEN}DM Deletion Completed for Token: {token}!")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()