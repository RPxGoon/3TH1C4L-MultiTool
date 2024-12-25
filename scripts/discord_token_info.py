import requests
from datetime import datetime, timezone
from colorama import Fore

def discord_token_info(token_info):
    try:
        api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_info}).json()

        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_info, 'Content-Type': 'application/json'})

        if response.status_code == 200:
            status = "Valid"
        else:
            status = "Invalid"

        username_discord = api.get('username', "None") + '#' + api.get('discriminator', "None")
        display_name_discord = api.get('global_name', "None")
        user_id_discord = api.get('id', "None")
        email_discord = api.get('email', "None")
        email_verified_discord = api.get('verified', "None")
        phone_discord = api.get('phone', "None")
        mfa_discord = api.get('mfa_enabled', "None")
        country_discord = api.get('locale', "None")
        avatar_discord = api.get('avatar', "None")
        avatar_decoration_discord = api.get('avatar_decoration_data', "None")
        public_flags_discord = api.get('public_flags', "None")
        flags_discord = api.get('flags', "None")
        banner_discord = api.get('banner', "None")
        banner_color_discord = api.get('banner_color', "None")
        accent_color_discord = api.get("accent_color", "None")
        nsfw_discord = api.get('nsfw_allowed', "None")

        try:
            created_at_discord = datetime.fromtimestamp(((int(api.get('id', 'None')) >> 22) + 1420070400000) / 1000, timezone.utc)
        except:
            created_at_discord = "None"

        nitro_discord = "None"
        try:
            if api.get('premium_type', 'None') == 0:
                nitro_discord = 'False'
            elif api.get('premium_type', 'None') == 1:
                nitro_discord = 'Nitro Classic'
            elif api.get('premium_type', 'None') == 2:
                nitro_discord = 'Nitro Boosts'
            elif api.get('premium_type', 'None') == 3:
                nitro_discord = 'Nitro Basic'
            else:
                nitro_discord = 'False'
        except:
            nitro_discord = "None"

        avatar_url_discord = "None"
        try:
            avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.png"
        except:
            avatar_url_discord = "None"

        linked_users_discord = api.get('linked_users', 'None')
        linked_users_discord = ' / '.join(linked_users_discord) if linked_users_discord else "None"

        bio_discord = "\n" + api.get('bio', 'None') if api.get('bio') else "None"

        print(f"""
    {Fore.RED}[+] {Fore.RESET}Status       : {Fore.RED}{status}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Token        : {Fore.RED}{token_info}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Username     : {Fore.RED}{username_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Display Name : {Fore.RED}{display_name_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Id           : {Fore.RED}{user_id_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Created      : {Fore.RED}{created_at_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Country      : {Fore.RED}{country_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Email        : {Fore.RED}{email_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Verified     : {Fore.RED}{email_verified_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Phone        : {Fore.RED}{phone_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Nitro        : {Fore.RED}{nitro_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Linked Users : {Fore.RED}{linked_users_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Avatar URL   : {Fore.RED}{avatar_url_discord}{Fore.RESET}
    {Fore.RED}[+] {Fore.RESET}Bio          : {Fore.RED}{bio_discord}{Fore.RESET}
    """)

    except Exception as e:
        print(f"{Fore.RED}[!] {Fore.RESET}{Fore.GREEN}Error Retrieving Information: {Fore.RED}{e}{Fore.RESET}")
