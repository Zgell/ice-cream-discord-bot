from enum import Enum, auto

class Users(Enum):
    '''
    Gives a number of different types for different users of the bot.
    Intended for use to allow certain commands to be restricted to certain groups.
    '''
    BLACKLISTED     = auto()  # Not allowed to use any bot commands
    DEFAULT_USER    = auto()  # Can use the default set of bot commands
    CONTENT_CREATOR = auto()  # Can use default + a couple of others (?)
    MODERATOR       = auto()  # Can use default + mod tools
    ADMINISTRATOR   = auto()  # Can use everything minus dev tools
    DEVELOPER       = auto()  # The highest tier, unlocks all commands + debug stuff
