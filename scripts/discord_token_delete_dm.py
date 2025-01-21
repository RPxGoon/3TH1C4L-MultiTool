import requests
import threading
from colorama import Fore

def run():
    try:
        
        token = input(f"{Fore.RED}[+] {Fore.GREEN}Enter Discord Token: ").strip()

        
        response = requests.get(
            'https://discord.com/api/v8/users/@me',
            headers={'Authorization': token, 'Content-Type': 'application/json'}
        )
        if response.status_code == 200:
            print(f"{Fore.RED}[+] {Fore.GREEN}Token Verified")
        else:
            print(f"{Fore.RED}[!] {Fore.RED}Invalid Token. Please try again.")
            return

        
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
            print(f"{Fore.RED}[!] No DMs found.")
            return

       
        print(f"{Fore.RED}[!] {Fore.RESET}Deleting DMs...")
        processes = []
        for channel_batch in [channels[i:i + 3] for i in range(0, len(channels), 3)]:
            t = threading.Thread(target=dm_deleter, args=(token, channel_batch))
            t.start()
            processes.append(t)

        for process in processes:
            process.join()

        print(f"{Fore.RED}[+] {Fore.GREEN}DM Deletion Completed!")

    except Exception as e:
        print(f"{Fore.RED}[!] An error occurred: {e}")
