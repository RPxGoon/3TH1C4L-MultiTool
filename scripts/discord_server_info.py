import requests
from colorama import init, Fore
init(autoreset=True)
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
def run():
    """
    Fetches and displays detailed information about a Discord server based on an invite link or code.
    """
    try:
        invite = input(f"{Fore.GREEN}[*] Server Invitation -> ")
        print()

        
       
        try:
            invite_code = invite.split("/")[-1]
        except:
            invite_code = invite.strip()

        
        response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}", timeout=10)
        if response.status_code == 200:
            api = response.json()

            
            inviter_info = api.get('inviter', {})
            server_info = api.get('guild', {})
            channel_info = api.get('channel', {})

            
            print(f"""
{Fore.RED}[+] Invitation         : {Fore.GREEN}{invite}
{Fore.RED}[+] Type               : {Fore.GREEN}{api.get('type', 'None')}
{Fore.RED}[+] Code               : {Fore.GREEN}{api.get('code', 'None')}
{Fore.RED}[+] Expired            : {Fore.GREEN}{api.get('expires_at', 'None')}
{Fore.RED}[+] Server ID          : {Fore.GREEN}{server_info.get('id', 'None')}
{Fore.RED}[+] Server Name        : {Fore.GREEN}{server_info.get('name', 'None')}
{Fore.RED}[+] Channel ID         : {Fore.GREEN}{channel_info.get('id', 'None')}
{Fore.RED}[+] Channel Name       : {Fore.GREEN}{channel_info.get('name', 'None')}
{Fore.RED}[+] Channel Type       : {Fore.GREEN}{channel_info.get('type', 'None')}
{Fore.RED}[+] Server Description : {Fore.GREEN}{server_info.get('description', 'None')}
{Fore.RED}[+] Server Icon        : {Fore.GREEN}{server_info.get('icon', 'None')}
{Fore.RED}[+] Server Features    : {Fore.GREEN}{' / '.join(server_info.get('features', []))}
{Fore.RED}[+] Server NSFW Level  : {Fore.GREEN}{server_info.get('nsfw_level', 'None')}
{Fore.RED}[+] Server NSFW        : {Fore.GREEN}{server_info.get('nsfw', 'None')}
{Fore.RED}[+] Flags              : {Fore.GREEN}{api.get('flags', 'None')}
{Fore.RED}[+] Verification Level : {Fore.GREEN}{server_info.get('verification_level', 'None')}
{Fore.RED}[+] Boost Count        : {Fore.GREEN} {server_info.get('premium_subscription_count', 'None')}
""")

           
            if inviter_info:
                print(f"""
{Fore.RED}[+] Inviter ID         : {Fore.GREEN}{inviter_info.get('id', 'None')}
{Fore.RED}[+] Username           : {Fore.GREEN}{inviter_info.get('username', 'None')}
{Fore.RED}[+] Discriminator      : {Fore.GREEN}{inviter_info.get('discriminator', 'None')}
{Fore.RED}[+] Avatar             : {Fore.GREEN}{inviter_info.get('avatar', 'None')}
{Fore.RED}[+] Public Flags       : {Fore.GREEN}{inviter_info.get('public_flags', 'None')}
{Fore.RED}[+] Flags              : {Fore.GREEN}{inviter_info.get('flags', 'None')}
{Fore.RED}[+] Banner             : {Fore.GREEN}{inviter_info.get('banner', 'None')}
{Fore.RED}[+] Accent Color       : {Fore.GREEN}{inviter_info.get('accent_color', 'None')}
{Fore.RED}[+] Banner Color       : {Fore.GREEN}{inviter_info.get('banner_color', 'None')}
""")

        else:
            print("[!] Error: Invalid invite URL or invite not found.") 
    except Exception as e:
        print(f"Error: {e}")

                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --