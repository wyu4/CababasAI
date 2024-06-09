## String colors (printing)
class TColors():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m' # orange on some systems
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m' # called to return to standard terminal text color

    B_SUCCESS = GREEN
    B_WARNING = RED
    B_RECEIVE = BLUE
    B_SEND = BRIGHT_MAGENTA
    B_MESSAGE_CONTENT = WHITE
    B_USER = CYAN
    B_FINISH_REASON = LIGHT_GRAY