from statement_type import StatementType
from statement import Statement
import sys
import re
from meta_commands import MetaCommands
from prepared_statements import PreparedStatements

def main():
    while(True):
        line = input("db > ")
        if(line[0] == "."):
            command_value = do_meta_command(line)
            if(command_value == MetaCommands.META_COMMAND_SUCCESS):
                continue
            elif(command_value == MetaCommands.META_COMMAND_UNRECOGNIZED_COMMAND):
                print("Unrecognized command {0} .\n".format(line)) 
                continue
            elif(command_value == MetaCommands.META_COMMAND_EXIT):
                print("~Goodbye")
                sys.exit()

        statement = Statement()
        statement_value = prepare_statement(line, statement)

        if(statement_value == PreparedStatements.PREPARE_SUCCESS):
            break
        elif(statement_value == PreparedStatements.PREPARE_UNRECOGNIZED_STATEMENT):
            print("Unrecognized keyword at start of {0} .\n".format(line)) 
            continue   

    execute_statement(statement)
    print("Executed")
  
def do_meta_command(arg):
    if(arg == ".exit"):
        return MetaCommands.META_COMMAND_EXIT
    else:
        return MetaCommands.META_COMMAND_UNRECOGNIZED_COMMAND

def prepare_statement(arg:str, statement:Statement):
    arg.upper()
    if(arg.startswith("INSERT")):
        regex = re.compile("^INSERT$\s^\+?\d+$\s^\w+$\s^\w+$")
        statement.type = StatementType.STATEMENT_INSERT
        if(not regex.match(arg)):
            return PreparedStatements.PREPARE_SYNTAX_ERROR
        splitStatement = arg.split(" ")
        statement.row_to_insert.id = int(splitStatement[1])
        statement.row_to_insert.username = splitStatement[2]
        statement.row_to_insert.email = splitStatement[3]
        return PreparedStatements.PREPARE_SUCCESS
    if(arg.startswith("select")):
        regex = re.compile("^SELECT$\s^\+?\d+$\s^\w+$\s^\w+$")
        statement.type = StatementType.STATEMENT_SELECT
        if(not regex.match(arg)):
            return PreparedStatements.PREPARE_SYNTAX_ERROR
        splitStatement = arg.split(" ")
        statement.row_to_insert.id = int(splitStatement[1])
        statement.row_to_insert.username = splitStatement[2]
        statement.row_to_insert.email = splitStatement[3]
        return PreparedStatements.PREPARE_SUCCESS

    return PreparedStatements.PREPARE_UNRECOGNIZED_STATEMENT

def execute_statement(statement:Statement):
    if(statement.type == StatementType.STATEMENT_INSERT):
        print("This is where we would do an insert")
    elif(statement.type == StatementType.STATEMENT_SELECT):
        print("This is where we would do a select.")


if __name__ == '__main__':
    main()
