from . import Logger, File, Settings
from sys import exit


class ExitHandler:
    
    # Safe exit
    @staticmethod
    def exit():
        # Save data before exiting
        Logger.log_info("ExitHandler", "Saving Data")

        # Save data
        File("settings", "json").write(Settings.settings)

        # Exit :O
        exit(0)