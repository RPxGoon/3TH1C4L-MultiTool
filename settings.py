import os
import json
import random
from colorama import Fore, Style
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".3th1c4l")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_CONFIG = {
    "theme": "ethical",
    "show_tips": True,
    "animations": True,
    "clear_screen": True,
    "check_updates": True,
    "columns": 3,
}

# --- Color themes ------------------------------------------------------------
# Each theme defines the palette used by the main menu + logo. "logo" is the
# (start_rgb, end_rgb) pair used for the animated gradient on the ASCII banner.
THEMES = {
    "ethical": {
        "label": "Ethical (default)",
        "primary": Fore.RED, "accent": Fore.MAGENTA, "text": Fore.GREEN,
        "value": Fore.CYAN, "dim": Fore.LIGHTBLACK_EX,
        "logo": ((255, 0, 0), (102, 11, 193)),
    },
    "matrix": {
        "label": "Matrix",
        "primary": Fore.GREEN, "accent": Fore.LIGHTGREEN_EX, "text": Fore.GREEN,
        "value": Fore.LIGHTGREEN_EX, "dim": Fore.LIGHTBLACK_EX,
        "logo": ((0, 255, 70), (0, 110, 25)),
    },
    "bloodmoon": {
        "label": "Blood Moon",
        "primary": Fore.RED, "accent": Fore.LIGHTRED_EX, "text": Fore.LIGHTRED_EX,
        "value": Fore.YELLOW, "dim": Fore.LIGHTBLACK_EX,
        "logo": ((255, 30, 30), (90, 0, 0)),
    },
    "ocean": {
        "label": "Ocean",
        "primary": Fore.CYAN, "accent": Fore.BLUE, "text": Fore.LIGHTCYAN_EX,
        "value": Fore.LIGHTBLUE_EX, "dim": Fore.LIGHTBLACK_EX,
        "logo": ((0, 210, 255), (0, 60, 200)),
    },
    "cyberpunk": {
        "label": "Cyberpunk",
        "primary": Fore.MAGENTA, "accent": Fore.CYAN, "text": Fore.LIGHTMAGENTA_EX,
        "value": Fore.LIGHTCYAN_EX, "dim": Fore.LIGHTBLACK_EX,
        "logo": ((255, 0, 200), (0, 220, 255)),
    },
    "mono": {
        "label": "Monochrome",
        "primary": Fore.WHITE, "accent": Fore.LIGHTWHITE_EX, "text": Fore.LIGHTBLACK_EX,
        "value": Fore.WHITE, "dim": Fore.LIGHTBLACK_EX,
        "logo": ((235, 235, 235), (90, 90, 90)),
    },
}

# --- Rotating tips shown above the menu --------------------------------------
TIPS = [
    "You can type a tool number with or without a leading zero (e.g. '1' or '01').",
    "Press [S] on the main menu to open Settings and switch colour themes.",
    "Turn these tips off anytime from the Settings menu.",
    "Use the Hash Identifier before cracking to know which algorithm you're facing.",
    "The Website Info Scanner pulls WHOIS, DNS, open ports and geo-IP in one shot.",
    "Only run these tools against systems you own or are authorised to test.",
    "DNS Lookup supports A, AAAA, MX, NS, TXT and CNAME record types.",
    "Base64 is encoding, not encryption - never use it to protect secrets.",
    "Disable the startup update check in Settings if you run fully offline.",
    "Found a bug or want a feature? Open an issue on the official GitHub repo.",
    "The Password Strength checker estimates entropy, not real-world crackability.",
    "Switch to the 'Matrix' or 'Cyberpunk' theme for a fresh look in Settings.",
]


def tip():
    return random.choice(TIPS)


def get_theme(config):
    return THEMES.get(config.get("theme", "ethical"), THEMES["ethical"])


def load_config():
    config = dict(DEFAULT_CONFIG)
    try:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                saved = json.load(f)
            if isinstance(saved, dict):
                config.update({k: saved[k] for k in saved if k in DEFAULT_CONFIG})
    except Exception:
        # Corrupt / unreadable config should never stop the tool launching.
        pass
    if config.get("theme") not in THEMES:
        config["theme"] = "ethical"
    return config


def save_config(config):
    try:
        os.makedirs(CONFIG_DIR, exist_ok=True)
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
        return True
    except Exception:
        return False


def reset_config():
    config = dict(DEFAULT_CONFIG)
    save_config(config)
    return config
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
