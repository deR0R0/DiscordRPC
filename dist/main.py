import sys
import os

# ------------------------------
# These following import is for pyinstaller (hidden imports)
# You may remove these imports if you are running the script through python and not exe/unix exec file
import psutil
import colorama
import pypresence
# ------------------------------

from utils import *
from rpcs import *
from menus import *

# Functions
def get_program_path():
    # Just to check for inconsistencies
    # For pyinstaller and the actual python script
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
        return application_path
    return os.path.dirname(os.path.abspath(__file__))

# Set the path
Settings.set_program_path(get_program_path())

# Actual Program Now
Logger.clear() 

# Load data
Logger.text_normal(Config.LOADING_TEXT)
Logger.text_normal("██╗░░░░░░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░")
Logger.text_normal("██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░")
Logger.text_normal("██║░░░░░██║░░██║███████║██║░░██║██║██╔██╗██║██║░░██╗░")
Logger.text_normal("██║░░░░░██║░░██║██╔══██║██║░░██║██║██║╚████║██║░░╚██╗")
Logger.text_normal("███████╗╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚██████╔╝")
Logger.text_normal("╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░")

# Load up file and set settings
Logger.log_info("MainProcess", "Loading File: settings.json")
f = File("settings", "json")
Settings.settings.update(f.read())

# Get Latest Version
Logger.log_info("MainProcess", "Checking for Updates...")
Config.set_latest_version(UpdateChecker.checkForUpdates())

if __name__ == "__main__":
    while True:
        Main.show()