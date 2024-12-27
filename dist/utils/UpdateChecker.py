import requests

from . import Logger


class UpdateChecker:
    @staticmethod
    def checkForUpdates() -> str:
        # Get the latest version from the github repo
        try:
            response = requests.get("https://api.github.com/repos/deR0R0/discordRPC/releases/latest")
            response = response.json()

        except requests.exceptions.RequestException:
            Logger.log_err("UpdateChecker", "Failed to check for updates, please check your internet connection.")
            return "error while checking for updates"
        
        # :O
        return response["tag_name"]