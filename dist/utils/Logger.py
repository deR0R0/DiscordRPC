from colorama import Fore as fore
from datetime import datetime
from sys import platform
from os import system, mkdir
from . import Settings, Config

# Save to file
def save(message):
    try:
        with open(rf"{Settings.program_path}/data/log.txt", "a") as file:
            file.write(f"{datetime.now().replace(microsecond=0)} -> {message}\n")
    except FileNotFoundError:
        try:
            with open(rf"{Settings.program_path}/data/log.txt", "w") as file:
                file.write(f"{datetime.now().replace(microsecond=0)} -> {message}\n")
        except FileNotFoundError:
            mkdir(rf"{Settings.program_path}/data")
            save(message)

# Normal Text
def text_normal(message):
    print(f"{fore.RESET}{message}")

# Information Text, like tips and stuff
def text_info(message):
    print(f"{fore.LIGHTBLUE_EX}{message}")

# Warning Text, like dangerous or important stuff
def text_warn(message):
    print(f"{fore.LIGHTYELLOW_EX}{message}")

# Normal Info Stuff
def log_info(location, message):
    save(f"[INFO] {location} | {message}")

# Unhandled Errors
def log_err(location, message):
    save(f"[ERR] {location} | {message}")

# Handled Error
def log_warn(location, message):
    save(f"[WARN] {location} | {message}")

# Clear, have to make this functions
# because of the stupid inconsistencies between linux, mac, and windows
def clear():
    if platform == "darwin" or platform == "linux":
        system("clear")
    elif platform == "win32":
        system("cls")
    else:
        log_warn("Logger", "Unknown platform, defaulting to linux clear")
        system("clear")

def prompt():
    return input(f"{Config.PROMPT_COLOR}{Config.PROMPT_TEXT}")