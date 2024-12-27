import json
from os import mkdir
from . import Settings

class File:
    def __init__(self, file_path, file_type):
        self.name = file_path
        self.type = file_type

    def read(self):
        try:
            with open(rf"{Settings.program_path}/data/{self.name}.{self.type}", "r") as file:
                match self.type:
                    case "json":
                        return json.load(file)
                    case _:
                        return file.read()
        except:
            match self.type:
                case "json":
                    self.write({})
                case _:
                    self.write("")

            return self.read()
                
    def write(self, data):
        try:
            with open(rf"{Settings.program_path}/data/{self.name}.{self.type}", "w") as file:
                match self.type:
                    case "json":
                        json.dump(data, file, indent=4)
                    case _:
                        file.write(data)
        except FileNotFoundError:
            mkdir(rf"{Settings.program_path}/data")
            self.write(data)