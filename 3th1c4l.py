import os
import re
import sys
import shutil
import time
import threading
import itertools
from functools import lru_cache
from colorama import init, Fore, Style
import questionary
import getpass
from importlib import import_module
import requests
from packaging import version

import settings as settings_mod
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --

CURRENT_VERSION = "1.0.7"
GITHUB_REPO = "RPxGoon/3TH1C4L-MultiTool"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"

init(autoreset=True)
username = getpass.getuser()

CONFIG = settings_mod.load_config()

# ANSI escape sequences must be stripped before measuring text width, otherwise
# ljust/center/rjust count the invisible colour codes and the layout breaks.
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def visible_len(text):
    return len(ANSI_RE.sub("", text))


def pad(text, width):
    diff = width - visible_len(text)
    return text + (" " * diff if diff > 0 else "")


def center_visible(text, width):
    diff = width - visible_len(text)
    if diff <= 0:
        return text
    left = diff // 2
    return (" " * left) + text + (" " * (diff - left))


# ---------------------------------------------------------------------------
# Tool registry (single source of truth)
# ---------------------------------------------------------------------------
TOOLS = {
    # Network
    "01": {"name": "Show My IP", "module": "scripts.show_my_ip", "function": "run"},
    "02": {"name": "IP Scanner", "module": "scripts.ip_scanner", "function": "run"},
    "03": {"name": "IP Pinger", "module": "scripts.ip_pinger", "function": "run_ip_pinger"},
    "04": {"name": "IP Port Scanner", "module": "scripts.ip_port_scanner", "function": "run"},
    "05": {"name": "Website Info Scanner", "module": "scripts.website_info_scanner", "function": "run"},
    "06": {"name": "DNS Lookup", "module": "scripts.dns_lookup", "function": "run"},
    "07": {"name": "Reverse DNS Lookup", "module": "scripts.reverse_dns", "function": "run"},
    "08": {"name": "HTTP Header Grabber", "module": "scripts.http_headers", "function": "run"},
    # OSINT
    "09": {"name": "Username Tracker", "module": "scripts.username_tracker", "function": "run"},
    "10": {"name": "WHOIS Lookup", "module": "scripts.whois_lookup", "function": "run"},
    "11": {"name": "MAC Vendor Lookup", "module": "scripts.mac_lookup", "function": "run"},
    # Utilities
    "12": {"name": "Password Generator", "module": "scripts.password_generator", "function": "run"},
    "13": {"name": "Password Strength", "module": "scripts.password_strength", "function": "run"},
    "14": {"name": "Hash Generator", "module": "scripts.hash_generator", "function": "run"},
    "15": {"name": "Hash Identifier", "module": "scripts.hash_identifier", "function": "run"},
    "16": {"name": "Base64 Encode/Decode", "module": "scripts.base64_tool", "function": "run"},
    # Discord - Server
    "17": {"name": "Discord Server Info", "module": "scripts.discord_server_info", "function": "run"},
    "18": {"name": "Discord Nitro Generator", "module": "scripts.discord_nitro_generator", "function": "run"},
    # Discord - Webhooks
    "19": {"name": "Webhook Deleter", "module": "scripts.discord_webhook_deleter", "function": "run"},
    "20": {"name": "Webhook Spammer", "module": "scripts.discord_webhook_spammer", "function": "run"},
    "21": {"name": "Webhook Info", "module": "scripts.discord_webhook_info", "function": "run"},
    "22": {"name": "Webhook Sender", "module": "scripts.discord_webhook_sender", "function": "run"},
    # Discord - Tokens
    "23": {"name": "Token Info", "module": "scripts.discord_token_info", "function": "run"},
    "24": {"name": "Token Delete DM", "module": "scripts.discord_token_delete_dm", "function": "run"},
    "25": {"name": "Token Friend Blocker", "module": "scripts.discord_token_block_friends", "function": "run"},
}

# Menu layout: each page is a list of columns, each column is (title, [tool ids]).
MENU = {
    1: [
        ("NETWORK", ["01", "02", "03", "04", "05", "06", "07", "08"]),
        ("OSINT", ["09", "10", "11"]),
        ("UTILITIES", ["12", "13", "14", "15", "16"]),
    ],
    2: [
        ("DISCORD · SERVER", ["17", "18"]),
        ("DISCORD · WEBHOOKS", ["19", "20", "21", "22"]),
        ("DISCORD · TOKENS", ["23", "24", "25"]),
    ],
}
TOTAL_PAGES = len(MENU)


# ---------------------------------------------------------------------------
# Update checker (optional GUI, degrades gracefully when no display)
# ---------------------------------------------------------------------------
class UpdateCheckerGUI:
    def __init__(self):
        import customtkinter as ctk
        self.ctk = ctk
        self.root = ctk.CTk()
        self.root.title("3TH1C4L Updater")

        window_width, window_height = 400, 200
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        ctk.set_appearance_mode("dark")

        self.frame = ctk.CTkFrame(self.root, fg_color="#0a0a0a", corner_radius=12)
        self.frame.pack(expand=True, fill="both", padx=2, pady=2)
        self.content_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title_label = ctk.CTkLabel(
            self.content_frame, text="3TH1C4L", font=("Segoe UI", 32, "bold"),
            text_color="#ff0000")
        self.title_label.pack(pady=(0, 15))
        self.status = ctk.CTkLabel(
            self.content_frame, text="Checking for updates...",
            font=("Segoe UI", 14), text_color="#660bb1")
        self.status.pack(pady=(0, 20))
        self.progress = ctk.CTkProgressBar(
            self.content_frame, width=300, height=3, corner_radius=1,
            progress_color="#ff0000", fg_color="#1a1a1a")
        self.progress.pack()
        self.progress.start()

        self.root.update_idletasks()
        self.root.lift()

    def update_status(self, text):
        self.status.configure(text=text)
        self.root.update()

    def close(self):
        self.root.destroy()


def check_for_updates():
    if not CONFIG.get("check_updates", True):
        return

    if os.name == "nt":
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    try:
        gui = UpdateCheckerGUI()
    except Exception:
        # No display / missing GUI deps: fall back to a silent console check.
        _console_update_check()
        if os.name == "nt":
            import ctypes
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        return

    gui.root.lift()
    try:
        response = requests.get(GITHUB_API_URL, timeout=10)
        if response.status_code == 200:
            latest_version = response.json()["tag_name"].replace("v", "")
            if version.parse(latest_version) > version.parse(CURRENT_VERSION):
                gui.update_status("Update found! Downloading...")
                time.sleep(1)
                download_url = response.json()["zipball_url"]
                r = requests.get(download_url, stream=True, timeout=30)
                with open("update.zip", "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                gui.update_status("Installing update...")
                time.sleep(1)
                import zipfile
                with zipfile.ZipFile("update.zip", "r") as zip_ref:
                    zip_ref.extractall("update_temp")
                update_folder = os.path.join("update_temp", os.listdir("update_temp")[0])
                for item in os.listdir(update_folder):
                    src = os.path.join(update_folder, item)
                    dst = os.path.join(os.path.dirname(__file__), item)
                    if os.path.isfile(src):
                        shutil.copy2(src, dst)
                    elif os.path.isdir(src):
                        if os.path.exists(dst):
                            shutil.rmtree(dst)
                        shutil.copytree(src, dst)
                shutil.rmtree("update_temp")
                os.remove("update.zip")
                gui.update_status("Update complete! Restarting...")
                time.sleep(2)
                gui.close()
                if os.name == "nt":
                    import ctypes
                    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                gui.update_status("No updates available")
                time.sleep(1)
                gui.close()
    except Exception:
        gui.update_status("Update check failed")
        time.sleep(1)
        gui.close()

    if os.name == "nt":
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
    try:
        gui.root.destroy()
    except Exception:
        pass


def _console_update_check():
    try:
        response = requests.get(GITHUB_API_URL, timeout=10)
        if response.status_code == 200:
            latest_version = response.json()["tag_name"].replace("v", "")
            theme = settings_mod.get_theme(CONFIG)
            if version.parse(latest_version) > version.parse(CURRENT_VERSION):
                print(f"{theme['primary']}[!] {theme['text']}Update available: "
                      f"{theme['value']}v{latest_version}{theme['text']} "
                      f"(you have v{CURRENT_VERSION})")
                time.sleep(1.5)
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Loading animation
# ---------------------------------------------------------------------------
def loading_spinner():
    theme = settings_mod.get_theme(CONFIG)
    spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])
    while not loading_spinner.done:
        sys.stdout.write(f"\r{theme['primary']}Loading {theme['accent']}{next(spinner)} ")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()


loading_spinner.done = False


def animate_loading(duration=1.0):
    if not CONFIG.get("animations", True):
        return
    loading_spinner.done = False
    spinner_thread = threading.Thread(target=loading_spinner)
    spinner_thread.start()
    time.sleep(duration)
    loading_spinner.done = True
    spinner_thread.join()


@lru_cache(maxsize=1)
def get_terminal_width(default_width=80):
    try:
        width = shutil.get_terminal_size().columns
        return max(80, width)
    except Exception:
        return default_width


def set_cmd_title_and_color():
    if os.name == "nt":
        os.system("title [3TH1C4L] Multi-Tool && color 0A")


# ---------------------------------------------------------------------------
# ASCII logo + gradient
# ---------------------------------------------------------------------------
def smooth_gradient_print(text, start_color, end_color):
    steps = len(text) - 1 if len(text) > 1 else 1
    r_start, g_start, b_start = start_color
    r_end, g_end, b_end = end_color
    gradient_text = "".join(
        f"\033[38;2;{int(r_start + (r_end - r_start) * (i / steps))};"
        f"{int(g_start + (g_end - g_start) * (i / steps))};"
        f"{int(b_start + (b_end - b_start) * (i / steps))}m{char}"
        for i, char in enumerate(text)
    )
    print(gradient_text + Style.RESET_ALL)


ASCII_LOGO = r"""
/* ++------------------------------------------------------------------++ */
/* ++------------------------------------------------------------------++ */
/* ||    ▓█████ ▄▄▄█████▓ ██░ ██  ▐██▌  ▄████▄   ▄▄▄       ██▓         || */
/* ||    ▓█   ▀ ▓  ██▒ ▓▒▓██░ ██▒ ▐██▌ ▒██▀ ▀█  ▒████▄    ▓██▒         || */
/* ||    ▒███   ▒ ▓██░ ▒░▒██▀▀██░ ▐██▌ ▒▓█    ▄ ▒██  ▀█▄  ▒██░         || */
/* ||    ▒▓█  ▄ ░ ▓██▓ ░ ░▓█ ░██  ▓██▒ ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░         || */
/* ||    ░▒████▒  ▒██▒ ░ ░▓█▒░██▓ ▒▄▄  ▒ ▓███▀ ░ ▓█   ▓██▒░██████▒     || */
/* ||    ░░ ▒░ ░  ▒ ░░    ▒ ░░▒░▒ ░▀▀▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░     || */
/* ||     ░ ░  ░    ░     ▒ ░▒░ ░ ░  ░   ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░     || */
/* ||       ░     ░       ░  ░░ ░    ░ ░          ░   ▒     ░ ░        || */
/* ||       ░  ░          ░  ░  ░ ░    ░ ░            ░  ░    ░  ░     || */
/* ||                           [RPxGoon]░                             || */
/* ++------------------------------------------------------------------++ */
/* ++------------------------------------------------------------------++ */

Simple 'CLI' Python Multi-Tool
[https://github.com/RPxGoon/3TH1C4L-MultiTool]
"""


def print_ascii_logo():
    width = get_terminal_width()
    theme = settings_mod.get_theme(CONFIG)
    start_color, end_color = theme["logo"]
    for line in ASCII_LOGO.splitlines():
        smooth_gradient_print(center_visible(line, width), start_color, end_color)


# ---------------------------------------------------------------------------
# Boxed column rendering (ANSI aware -> always aligned)
# ---------------------------------------------------------------------------
def build_column_box(title, tool_ids, inner_width, theme):
    p, a, t, d = theme["primary"], theme["accent"], theme["text"], theme["dim"]
    r = Fore.RESET
    lines = []
    lines.append(f"{p}╭{'─' * inner_width}╮{r}")
    lines.append(f"{p}│{a}{center_visible(title, inner_width)}{p}│{r}")
    lines.append(f"{p}├{'─' * inner_width}┤{r}")
    for tid in tool_ids:
        name = TOOLS[tid]["name"]
        content = f" {p}[{a}{tid}{p}] {t}{name}"
        lines.append(f"{p}│{pad(content, inner_width)}{p}│{r}")
    lines.append(f"{p}╰{'─' * inner_width}╯{r}")
    return lines


def render_page(page, theme):
    width = get_terminal_width()
    columns = MENU[page]
    ncols = len(columns)
    gutter = 2
    usable = min(width, 118)
    col_outer = (usable - gutter * (ncols - 1)) // ncols
    inner = col_outer - 2

    boxes = [build_column_box(title, ids, inner, theme) for title, ids in columns]
    height = max(len(box) for box in boxes)
    # Pad shorter boxes with blank interior rows (before the closing border).
    for box in boxes:
        while len(box) < height:
            box.insert(len(box) - 1, f"{theme['primary']}│{' ' * inner}│{Fore.RESET}")

    block_width = col_outer * ncols + gutter * (ncols - 1)
    left_margin = max(0, (width - block_width) // 2)
    pad_left = " " * left_margin

    for row in range(height):
        line = (" " * gutter).join(boxes[c][row] for c in range(ncols))
        print(pad_left + line)


def print_menu(page=1):
    if CONFIG.get("clear_screen", True):
        os.system("cls" if os.name == "nt" else "clear")
    theme = settings_mod.get_theme(CONFIG)
    width = get_terminal_width()
    print_ascii_logo()

    if CONFIG.get("show_tips", True):
        tip_text = f"{theme['accent']}TIP: {theme['dim']}{settings_mod.tip()}"
        print(center_visible(tip_text, width))
        print()

    render_page(page, theme)
    print()

    # Footer / navigation bar
    p, a, t = theme["primary"], theme["accent"], theme["text"]
    nav_parts = []
    if page < TOTAL_PAGES:
        nav_parts.append(f"{p}[{a}N{p}] {t}Next")
    if page > 1:
        nav_parts.append(f"{p}[{a}B{p}] {t}Back")
    nav_parts.append(f"{p}[{a}S{p}] {t}Settings")
    nav_parts.append(f"{p}[{a}E{p}] {t}Exit")
    pageinfo = f"{theme['dim']}Page {page}/{TOTAL_PAGES}"
    nav = f"{theme['dim']} · ".join(nav_parts) + f"   {pageinfo}"
    print(center_visible(nav, width))
    print()


def build_questionary_style(theme):
    name_map = {
        Fore.RED: "red", Fore.GREEN: "green", Fore.MAGENTA: "magenta",
        Fore.CYAN: "cyan", Fore.BLUE: "blue", Fore.WHITE: "white",
        Fore.YELLOW: "yellow",
        Fore.LIGHTRED_EX: "#ff6b6b", Fore.LIGHTGREEN_EX: "#8aff80",
        Fore.LIGHTMAGENTA_EX: "#ff8aff", Fore.LIGHTCYAN_EX: "#8affff",
        Fore.LIGHTBLUE_EX: "#8ab4ff", Fore.LIGHTWHITE_EX: "#ffffff",
        Fore.LIGHTBLACK_EX: "#888888",
    }
    accent = name_map.get(theme["accent"], "magenta")
    text = name_map.get(theme["text"], "green")
    primary = name_map.get(theme["primary"], "red")
    return questionary.Style([
        ("question", f"bold {text}"),
        ("answer", text),
        ("pointer", f"bold {accent}"),
        ("highlighted", f"bold {accent}"),
        ("selected", accent),
        ("input", text),
        ("instruction", "italic #888888"),
        ("text", primary),
        ("prompt", text),
    ])


# ---------------------------------------------------------------------------
# Settings menu
# ---------------------------------------------------------------------------
def on_off(value):
    return "ON" if value else "OFF"


def settings_menu():
    theme = settings_mod.get_theme(CONFIG)
    style = build_questionary_style(theme)

    while True:
        if CONFIG.get("clear_screen", True):
            os.system("cls" if os.name == "nt" else "clear")
        theme = settings_mod.get_theme(CONFIG)
        style = build_questionary_style(theme)
        print_ascii_logo()
        print(center_visible(f"{theme['accent']}S E T T I N G S", get_terminal_width()))
        print()

        choices = [
            f"Theme            →  {theme['label']}",
            f"Tips             →  {on_off(CONFIG['show_tips'])}",
            f"Animations       →  {on_off(CONFIG['animations'])}",
            f"Clear Screen     →  {on_off(CONFIG['clear_screen'])}",
            f"Startup Updates  →  {on_off(CONFIG['check_updates'])}",
            "About / Credits",
            "Reset to Defaults",
            "Back to Menu",
        ]
        answer = questionary.select(
            "Select an option:", choices=choices, qmark="»", style=style,
            instruction="(↑/↓ then Enter)",
        ).ask()

        if answer is None or answer.startswith("Back"):
            break
        elif answer.startswith("Theme"):
            theme_menu(style)
        elif answer.startswith("Tips"):
            CONFIG["show_tips"] = not CONFIG["show_tips"]
            settings_mod.save_config(CONFIG)
        elif answer.startswith("Animations"):
            CONFIG["animations"] = not CONFIG["animations"]
            settings_mod.save_config(CONFIG)
        elif answer.startswith("Clear Screen"):
            CONFIG["clear_screen"] = not CONFIG["clear_screen"]
            settings_mod.save_config(CONFIG)
        elif answer.startswith("Startup Updates"):
            CONFIG["check_updates"] = not CONFIG["check_updates"]
            settings_mod.save_config(CONFIG)
        elif answer.startswith("About"):
            about_screen(theme)
        elif answer.startswith("Reset"):
            CONFIG.update(settings_mod.reset_config())


def theme_menu(style):
    theme = settings_mod.get_theme(CONFIG)
    labels = {key: data["label"] for key, data in settings_mod.THEMES.items()}
    choices = [f"{labels[k]}" + ("  (current)" if k == CONFIG["theme"] else "")
               for k in settings_mod.THEMES]
    choices.append("Back")

    answer = questionary.select(
        "Choose a theme:", choices=choices, qmark="»", style=style,
    ).ask()
    if answer is None or answer.startswith("Back"):
        return
    chosen = answer.replace("  (current)", "")
    for key, data in settings_mod.THEMES.items():
        if data["label"] == chosen:
            CONFIG["theme"] = key
            settings_mod.save_config(CONFIG)
            break


def about_screen(theme):
    if CONFIG.get("clear_screen", True):
        os.system("cls" if os.name == "nt" else "clear")
    print_ascii_logo()
    p, a, t, v = theme["primary"], theme["accent"], theme["text"], theme["value"]
    width = get_terminal_width()
    lines = [
        f"{a}3TH1C4L MultiTool  {t}v{CURRENT_VERSION}",
        "",
        f"{p}[+] {t}Author:   {v}RPxGoon",
        f"{p}[+] {t}Repo:     {v}https://github.com/{GITHUB_REPO}",
        f"{p}[+] {t}Tools:    {v}{len(TOOLS)} utilities across Network, OSINT, Utilities & Discord",
        f"{p}[+] {t}License:  {v}See LICENSE",
        "",
        f"{theme['dim']}For educational & authorised testing only.",
        f"{theme['dim']}The author is not responsible for misuse.",
    ]
    for line in lines:
        print(center_visible(line, width))
    print()
    input(center_visible(f"{p}[*] {t}Press 'Enter' to go back...", width))


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
def run_tool():
    set_cmd_title_and_color()
    current_page = 1

    while True:
        theme = settings_mod.get_theme(CONFIG)
        style = build_questionary_style(theme)
        print_menu(current_page)

        choice = questionary.text(
            f"┌──({username}@3TH1C4L)─[~/main]\n └─$",
            qmark="",
            style=style,
        ).ask()

        if choice is None:
            choice = "e"
        choice = choice.strip()
        key = choice.lower()

        # Normalise numeric input ("1" -> "01") so both forms work.
        lookup = choice.zfill(2) if choice.isdigit() else choice

        ran_tool = False

        if key == "n" and current_page < TOTAL_PAGES:
            animate_loading(0.3)
            current_page += 1
        elif key == "b" and current_page > 1:
            animate_loading(0.3)
            current_page -= 1
        elif key == "s":
            settings_menu()
        elif key == "e":
            animate_loading(0.5)
            print(f"{theme['primary']}[!] {theme['text']}Exiting... Goodbye!")
            break
        elif lookup in TOOLS:
            tool = TOOLS[lookup]
            animate_loading(0.3)
            print(f"{theme['accent']}[{tool['name']}]")
            print()
            try:
                module = import_module(tool["module"])
                getattr(module, tool["function"])()
            except KeyboardInterrupt:
                print(f"\n{theme['primary']}[!] {theme['text']}Tool interrupted.")
            except Exception as e:
                print(f"\n{theme['primary']}[!] {theme['text']}Tool error: {theme['value']}{e}")
            ran_tool = True
        else:
            animate_loading(0.3)
            print(f"{theme['primary']}[!] {theme['text']}Invalid Choice. Please Select a Valid Option")
            ran_tool = True

        if ran_tool:
            input(f"{theme['primary']}[*] {theme['text']}Press 'Enter' to Continue...")

        if CONFIG.get("clear_screen", True):
            os.system("cls" if os.name == "nt" else "clear")
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    check_for_updates()
    run_tool()
