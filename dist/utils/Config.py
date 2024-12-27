from colorama import Fore as fore

# General Stuff
INVALID_OPTION = "Invalid Option!"
CRUSAGE_CLIENT_ID = "1320878832164798504"
CURRENT_VERSION = "v2.0.0"
LATEST_VERSION  = ""

# Logger Stuff
PROMPT_TEXT_OPTION = "[?]: "
PROMPT_TEXT_INT = "[#]: "
PROMPT_TEXT_TEXT = "[>]: "
PROMPT_COLOR = fore.LIGHTGREEN_EX

# Loading
LOADING_TEXT = "Loading Your Data..."


def set_latest_version(version: str):
    global LATEST_VERSION
    LATEST_VERSION = version
    return