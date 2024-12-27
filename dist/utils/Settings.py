# Program Path (usually where the script is executed)
program_path = ""

# Data
settings = {}

# Stop the threads
stop_thread = False



# Setter Functions
def set_program_path(path):
    global program_path
    program_path = path
    return

def set_stop_thread(value: bool):
    global stop_thread
    stop_thread = value
    return