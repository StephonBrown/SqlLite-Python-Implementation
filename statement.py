from row import Row
from statement_type import StatementType

class Statement:
    
    type:StatementType
    row_to_insert: Row
    def __init__(self) -> None:
        super().__init__()