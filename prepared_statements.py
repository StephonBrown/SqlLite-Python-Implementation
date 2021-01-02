from enum import Enum, auto

class PreparedStatements(Enum):
    PREPARE_SUCCESS = auto()
    PREPARE_UNRECOGNIZED_STATEMENT = auto()
    PREPARE_SYNTAX_ERROR = auto()
