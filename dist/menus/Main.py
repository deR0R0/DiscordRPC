import sys

sys.path.insert(1, sys.path[0].replace("menus", ""))
from utils import *
from .CPUandRAM import CPUandRAM

# Config
MAIN_MENU_TEXT = "Made by Robert Zhao"
MAIN_MENU_OPTIONS = [
    "CPU & RAM Usage",
    "Settings",
    "Exit",
]


class Main:
    # Display stuff
    @staticmethod
    def show(incorrectInput: bool = False):
        # Show Menu
        Logger.clear()

        # Show Error if incorrect input
        if(incorrectInput):
            Logger.text_warn(Config.INVALID_OPTION)

        # Giant Watermark, lol
        Logger.text_normal("░█████╗░██████╗░██████╗░░█████╗░")
        Logger.text_normal("██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
        Logger.text_normal("██║░░╚═╝██████╔╝██████╔╝██║░░╚═╝")
        Logger.text_normal("██║░░██╗██╔══██╗██╔═══╝░██║░░██╗")
        Logger.text_normal("╚█████╔╝██║░░██║██║░░░░░╚█████╔╝")
        Logger.text_normal("░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░")

        # Show who made it and the version
        Logger.text_info(f"{MAIN_MENU_TEXT}")
        Logger.text_info(f"Current Version: {Config.CURRENT_VERSION}")

        if Config.CURRENT_VERSION != Config.LATEST_VERSION:
            Logger.text_warn(f"New Version Available: {Config.LATEST_VERSION} | Download at https://github.com/deR0R0/discordRPC/releases/latest")

        for i, option in enumerate(MAIN_MENU_OPTIONS):
            Logger.text_normal(f"[{i+1}] {option}")

        # Prompt user for input
        i = Prompt.prompt()
        
        # Call Respected Menus based on input
        match i:
            case "1":
                CPUandRAM.main()
                Main.show()
            case "2":
                Main.settings()
            case "3":
                Logger.log_info("MainMenu", "Exiting Program")
                ExitHandler.exit()
            case _:
                Main.show(True)
                return
            
        Main.show()

    @staticmethod
    def settings():
        Logger.clear()
        Logger.text_info("Settings isn't done yet, please check back later.")
        Logger.text_warn("Press Enter to Continue")
        Prompt.enter()
        return