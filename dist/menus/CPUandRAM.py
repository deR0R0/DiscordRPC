import sys
from time import time
from threading import Thread

sys.path.insert(1, sys.path[0].replace("menus", ""))
from utils import *
from rpcs import CRUsage

# Config
CRUSAGE_MAIN_TEXT = "CPU and RAM Usage Mode"
CRUSAGE_MAIN_OPTIONS = [
    "Start",
    "Back",
]

class CPUandRAM:

    @staticmethod
    def main(incorrectInput: bool = False):
        # Clear screen and show the menu
        Logger.clear()

        # Show incorrect input
        if(incorrectInput):
            Logger.text_warn(Config.INVALID_OPTION)

        Logger.text_info(CRUSAGE_MAIN_TEXT)
        for i, option in enumerate(CRUSAGE_MAIN_OPTIONS):
            Logger.text_normal(f"[{i+1}] {option}")

        # Prompt user for input
        i = Prompt.prompt()

        match i:
            case "1":
                CPUandRAM.rpc()
                CPUandRAM.main()
            case "2":
                return
            case _:
                CPUandRAM.main(True)
                return
    
    @staticmethod
    def rpc():
        # Clear screen, ask for delay
        Logger.clear()
        Logger.text_info("Delay in Seconds? (How often the status updates)")
        delay = Prompt.prompt_int()

        Logger.clear()

        try:
            delay = float(delay)
        except ValueError:
            Logger.text_warn("Please enter a valid number!")
            Prompt.enter()
            return

        # Try to make sure the input is > 0
        if delay < 1:
            Logger.text_warn("Please put a number greater than or equal to 1!")
            Prompt.enter()
            return

        # Create object and handle exception when user enters invalid input
        usage = CRUsage(int(delay), int(time()))
        
        # Connect to discord
        match usage.connect():
            case "discordNotFound":
                Logger.text_warn("Discord is not running!")
                Prompt.enter()
                return
            case "fatalErr":
                Logger.text_warn("Fatal Error Occured, Please check logs (under folder data/logs.txt) and report on github. Thanks! :D")
                Logger.text_info("(if on mac, make sure discord is running)")
                Prompt.enter()
                return

        # Then actually start the rpc
        t = Thread(target=usage.start)
        t.start()

        # Wait for user to click enter for stopping
        Logger.text_info("Press Enter to Stop RPC")
        Prompt.enter()
        usage.stop()
        return