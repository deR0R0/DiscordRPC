from . import Config
class Prompt:

    # Prompt for an option
    @staticmethod
    def prompt() -> str:
        return input(f"{Config.PROMPT_COLOR}{Config.PROMPT_TEXT_OPTION}")
    
    # Prompt for an integer
    @staticmethod
    def prompt_int() -> str:
        return input(f"{Config.PROMPT_COLOR}{Config.PROMPT_TEXT_INT}")
    
    # Prompt for text
    @staticmethod
    def prompt_text() -> str:
        return input(f"{Config.PROMPT_COLOR}{Config.PROMPT_TEXT_TEXT}")
    
    # Enter
    @staticmethod
    def enter():
        input(f"{Config.PROMPT_COLOR}[ENTER]")
        return