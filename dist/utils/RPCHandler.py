import pypresence
import sys

sys.path.insert(1, sys.path[0].replace("menus", ""))
from utils import Logger, Config

# Global
RPC = None

class RPCHandler:

    @staticmethod
    def checkIfRunning() -> bool:     
        global RPC

        if RPC is None:
            return False
        
        return True
    
    @staticmethod
    def stopRPC():
        global RPC

        if not RPCHandler.checkIfRunning():
            return
        
        try:
            Logger.log_info("RPCHandler", "Attempting to close RPC connection")
            RPC.close()
            RPC = None
        except Exception as e:
            Logger.log_err("RPCHandler", f"{e}")

    @staticmethod
    def start(client_id: int) -> any:
        global RPC

        # Stop the previous RPC, if running
        RPCHandler.stopRPC()

        # Attempt to connect RPC
        try:
            Logger.log_info("RPCHandler", "Attempting to connect to Discord RPC")
            RPC = pypresence.Presence(client_id)
            RPC.connect()

        # Handle exception when discord is not running, returns nothing
        except pypresence.DiscordNotFound:
            Logger.log_warn("RPCHandler", "Discord is not running!")
            return "discordNotFound"
        
        # handle any other unknown exception
        except Exception as e:
            Logger.log_err("RPCHandler", f"{e}")
            return "fatalErr"
        
        return RPC