import sys
import time
import psutil
from pypresence import PipeClosed

sys.path.insert(1, sys.path[0].replace("menus", ""))
from utils import *

class CRUsage:
    def __init__(self, delay: int):
        self.delay = delay
        self.rpc = None

    def connect(self) -> any:
        self.rpc = RPCHandler.start(Config.CRUSAGE_CLIENT_ID)

        return self.rpc

    def start(self):
        while True:
            # Check if stopped, if not, continue to update
            if self.rpc is None:
                break

            # Determine whether cpu usage is low, medium, or high
            cpuUsage = self.getCPUUsage()
            if cpuUsage <= 33:
                img = "lowcpu"
            elif cpuUsage <= 66:
                img = "mediumcpu"
            else:
                img = "highcpu"

            # Get ram usage
            ramUsage = self.getRamUsage()

            try:
                self.rpc.update(state=f"RAM: {ramUsage}", details=f"CPU: {cpuUsage}%", large_image=img, large_text="CPU Levels")
            except PipeClosed:
                Logger.log_warn("CRUsage", "Pipe Closed, attempting to reconnect...")
                pass
            except Exception as err:
                Logger.log_err("CRUsage", f"{err}")
                Logger.text_warn("An error has occured, please check the logs (/data/logs.txt) for more information")
                break

            time.sleep(abs(self.delay))

        RPCHandler.stopRPC()

    def getCPUUsage(self):
        return psutil.cpu_percent()
    
    def getRamUsage(self):
        total = psutil.virtual_memory().total / (1024 ** 3)
        used = round(psutil.virtual_memory().total / (1024 ** 3), 2) * round((psutil.virtual_memory().percent / 100), 2)
        return f"{used}/{total} MB"


    def stop(self):
        self.rpc = None