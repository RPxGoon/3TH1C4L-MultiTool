import requests
from datetime import datetime, timezone

def check_token(token_discord):
    try:
        print(f"Information Recovery...")
        api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()

        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})

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

        # Additional data collection for linked users, bio, guilds, payment methods, etc.
        linked_users_discord = api.get('linked_users', 'None')
        linked_users_discord = ' / '.join(linked_users_discord) if linked_users_discord else "None"

        bio_discord = "\n" + api.get('bio', 'None') if api.get('bio') else "None"

        # Print results
        print(f"""
    Status       : {status}
    Token        : {token_discord}
    Username     : {username_discord}
    Display Name : {display_name_discord}
    Id           : {user_id_discord}
    Created      : {created_at_discord}
    Country      : {country_discord}
    Email        : {email_discord}
    Verified     : {email_verified_discord}
    Phone        : {phone_discord}
    Nitro        : {nitro_discord}
    Linked Users : {linked_users_discord}
    Avatar URL   : {avatar_url_discord}
    Bio          : {bio_discord}
    """)

    except Exception as e:
        print(f"Error when retrieving information: {e}")
