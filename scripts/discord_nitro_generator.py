import string
import json
import requests
import threading
import random

# Color codes for terminal output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'

INFO = f"{BLUE}[INFO]{RESET}"
SUCCESS = f"{GREEN}[+]{RESET}"
ERROR = f"{RED}[-]{RESET}"
INVALID = f"{RED}[INVALID]{RESET}"
VALID = f"{GREEN}[VALID]{RESET}"

def error_handler(error_message):
    print(f"{ERROR} {error_message}")
    print()

def print_title(title):
    print(f"\n{YELLOW}{'=' * 50}\n{title.center(50)}\n{'=' * 50}{RESET}\n")

def send_webhook(webhook_url, url_nitro, username_webhook, avatar_webhook, color_webhook):
    payload = {
        'embeds': [{
            'title': 'Nitro Valid!',
            'description': f"**Nitro:**\n```{url_nitro}```",
            'color': int(color_webhook, 16),  # Convert hex to int
            'footer': {
                "text": username_webhook,
                "icon_url": avatar_webhook,
            }
        }],
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }

    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        print(f"{SUCCESS} Webhook sent: {url_nitro}")
    except requests.RequestException as e:
        error_handler(f"Failed to send webhook: {e}")

def nitro_check(webhook_url, webhook_enabled, username_webhook, avatar_webhook, color_webhook):
    code_nitro = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    url_nitro = f'https://discord.gift/{code_nitro}'
    api_url = f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true'

    try:
        response = requests.get(api_url, timeout=1)
        if response.status_code == 200:
            print(f"{VALID} Nitro Code: {WHITE}{url_nitro}{RESET}")
            if webhook_enabled:
                send_webhook(webhook_url, url_nitro, username_webhook, avatar_webhook, color_webhook)
        else:
            print(f"{INVALID} Nitro Code: {WHITE}{url_nitro}{RESET}")
    except requests.RequestException as e:
        error_handler(f"Error checking Nitro code: {e}")

def run():
    print_title("Discord Nitro Generator")

    # Ask for webhook details
    webhook_enabled = input(f"{INFO} Use a webhook? (y/n): ").lower() in ['y', 'yes']
    webhook_url = None
    if webhook_enabled:
        webhook_url = input(f"{INFO} Enter Webhook URL: ")

    username_webhook = input(f"{INFO} Webhook Username (default: Nitro Bot): ") or "Nitro Bot"
    avatar_webhook = input(f"{INFO} Webhook Avatar URL (optional): ") or ""
    color_webhook = "00FF00"  # Hexadecimal string

    try:
        threads_number = int(input(f"{INFO} Enter the number of threads: "))
    except ValueError:
        error_handler("Invalid number of threads. Please enter a valid number.")
        return

    def create_threads():
        threads = []
        for _ in range(threads_number):
            t = threading.Thread(target=nitro_check, args=(webhook_url, webhook_enabled, username_webhook, avatar_webhook, color_webhook))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

    try:
        while True:
            create_threads()
    except KeyboardInterrupt:
        print(f"\n{INFO} Nitro generator stopped by user.")