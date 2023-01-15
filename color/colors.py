'''
color/colors.py

This provides the Colors class, which is used for terminal formatting.
It uses ANSI escape sequences to color/format the terminal.
Mostly used on the server-side to make the interface more readable.
'''

class Colors:
    RESET = '\u001b[0m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    BLUE = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'
    GRAY = '\u001b[37m'
    LIGHT_RED = '\u001b[31;1m'
    LIGHT_GREEN = '\u001b[32;1m'
    LIGHT_YELLOW = '\u001b[33;1m'
    LIGHT_BLUE = '\u001b[34;1m'
    LIGHT_MAGENTA = '\u001b[35;1m'
    LIGHT_CYAN = '\u001b[36;1m'
