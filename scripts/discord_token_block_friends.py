import requests
import threading
from colorama import Fore, init
from datetime import datetime, timezone
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

def ErrorModule(e):
    
    print(f"{Fore.RED}[!] {Fore.RED}Error: {e}")

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

def BlockFriends(token, friends):
    
    for friend in friends:
        try:
            requests.put(
                f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}',
                headers={'Authorization': token},
                json={"type": 2}
            )
            print(f"{Fore.RED}[+] Blocked {Fore.MAGENTA}{friend['user']['username']}#{friend['user']['discriminator']}")
        except Exception as e:
            print(f"{Fore.RED}[!] {Fore.RED}Failed to block {Fore.MAGENTA}{friend['user']['username']}#{friend['user']['discriminator']}: {e}")

def run():

    try:
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

        for token in selected_tokens:
            
            friends = requests.get(
                "https://discord.com/api/v9/users/@me/relationships",
                headers={'Authorization': token}
            ).json()

            if not friends:
                print(f"{Fore.RED}[!] No friends found for token: {token}.")
                continue

            block_choice = input(
                f"{Fore.RED}[*] {Fore.GREEN}Enter 'all' to Block All Friends or Enter Specific Friend IDs Separated by Commas: {Fore.RESET}"
            ).strip()

            if block_choice.lower() == 'all':
                print(f"{Fore.RED}[*] {Fore.GREEN}Blocking All Friends for token: {token}...")
                threads = []
                for chunk in [friends[i:i + 3] for i in range(0, len(friends), 3)]:
                    thread = threading.Thread(target=BlockFriends, args=(token, chunk))
                    thread.start()
                    threads.append(thread)
                for thread in threads:
                    thread.join()
            else:
               
                friend_ids_to_block = [friend_id.strip() for friend_id in block_choice.split(",")]
                friends_to_block = [friend for friend in friends if str(friend['id']) in friend_ids_to_block]

                if not friends_to_block:
                    print(f"{Fore.RED}[!] {Fore.RED}No matching friends found for token: {token}.")
                else:
                    print(f"{Fore.RED}[*] {Fore.GREEN}Blocking Specified Friends for token: {token}...")
                    threads = []
                    for chunk in [friends_to_block[i:i + 3] for i in range(0, len(friends_to_block), 3)]:
                        thread = threading.Thread(target=BlockFriends, args=(token, chunk))
                        thread.start()
                        threads.append(thread)
                    for thread in threads:
                        thread.join()

    except Exception as e:
        ErrorModule(e)
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()
