from enum import Enum, auto

class MetaCommands(Enum):
    META_COMMAND_SUCCESS = auto()
    META_COMMAND_UNRECOGNIZED_COMMAND = auto()
    META_COMMAND_EXIT = auto()