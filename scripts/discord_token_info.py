import requests
from datetime import datetime, timezone
from colorama import Fore, init

init(autoreset=True)

def run():
    token_info = input(f"{Fore.RED}[*] {Fore.LIGHTGREEN_EX}Enter Discord Token: {Fore.RESET}").strip()
    
    try:
        # Fetch data using the provided token
        api = requests.get(
            'https://discord.com/api/v8/users/@me',
            headers={'Authorization': token_info}
        ).json()

        response = requests.get(
            'https://discord.com/api/v8/users/@me',
            headers={'Authorization': token_info, 'Content-Type': 'application/json'}
        )

        # Check token validity
        status = "Valid" if response.status_code == 200 else "Invalid"

        # Parse response data
        username_discord = api.get('username', "None") + '#' + api.get('discriminator', "None")
        display_name_discord = api.get('global_name', "None")
        user_id_discord = api.get('id', "None")
        email_discord = api.get('email', "None")
        email_verified_discord = api.get('verified', "None")
        phone_discord = api.get('phone', "None")
        mfa_discord = api.get('mfa_enabled', "None")
        country_discord = api.get('locale', "None")
        avatar_discord = api.get('avatar', "None")
        banner_discord = api.get('banner', "None")
        banner_color_discord = api.get('banner_color', "None")
        accent_color_discord = api.get("accent_color", "None")
        nsfw_discord = api.get('nsfw_allowed', "None")
        public_flags_discord = api.get('public_flags', "None")
        flags_discord = api.get('flags', "None")
        bio_discord = api.get('bio', "None") or "None"

        # Calculate account creation time
        try:
            created_at_discord = datetime.fromtimestamp(
                ((int(user_id_discord) >> 22) + 1420070400000) / 1000, timezone.utc
            )
        except:
            created_at_discord = "None"

        # Nitro status
        premium_type = api.get('premium_type', 0)
        nitro_discord = {
            0: "None",
            1: "Nitro Classic",
            2: "Nitro Boost",
            3: "Nitro Basic"
        }.get(premium_type, "None")

        # Avatar URL
        avatar_url_discord = (
            f"https://cdn.discordapp.com/avatars/{user_id_discord}/{avatar_discord}.gif"
            if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{avatar_discord}.gif").status_code == 200
            else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{avatar_discord}.png"
        ) if avatar_discord != "None" else "None"

        # Linked users
        linked_users_discord = api.get('linked_users', None)
        linked_users_discord = " / ".join(linked_users_discord) if linked_users_discord else "None"

        # Print gathered data
        print(f"""
{Fore.RED}[+] {Fore.GREEN}Status       : {Fore.RED}{status}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Token        : {Fore.RED}{token_info}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Username     : {Fore.RED}{username_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Display Name : {Fore.RED}{display_name_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}ID           : {Fore.RED}{user_id_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Created      : {Fore.RED}{created_at_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Country      : {Fore.RED}{country_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Email        : {Fore.RED}{email_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Verified     : {Fore.RED}{email_verified_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Phone        : {Fore.RED}{phone_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Nitro        : {Fore.RED}{nitro_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Linked Users : {Fore.RED}{linked_users_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Avatar URL   : {Fore.RED}{avatar_url_discord}{Fore.RESET}
{Fore.RED}[+] {Fore.GREEN}Bio          : {Fore.RED}{bio_discord}{Fore.RESET}
""")

    except Exception as e:
        print(f"{Fore.RED}[!] Error Retrieving Information: {Fore.RED}{e}{Fore.RESET}")
