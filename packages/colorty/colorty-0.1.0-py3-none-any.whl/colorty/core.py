# Core functionalities like setting colors
class Clt:
    RESET = '\033[39m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    LIGHTBLACK_EX = '\033[90m'
    LIGHTRED_EX = '\033[91m'
    LIGHTGREEN_EX = '\033[92m'
    LIGHTYELLOW_EX = '\033[93m'
    LIGHTBLUE_EX = '\033[94m'
    LIGHTMAGENTA_EX = '\033[95m'
    LIGHTCYAN_EX = '\033[96m'
    LIGHTWHITE_EX = '\033[97m'

class Style:
    RESET_ALL = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BRIGHT = "\033[1m"
    DIM = "\033[2m"
    NORMAL = "\033[22m"
    
    
def set_color(color):
    """
    Set the terminal text color.
    """
    try:
        print(f"\033[{color}m", end="")
    except Exception as e:
        print(f"Error setting color: {e}")

def reset_color():
    """
    Reset the terminal text color to default.
    """
    try:
        print("\033[0m", end="")
    except Exception as e:
        print(f"Error resetting color: {e}")