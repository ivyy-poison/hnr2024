import sys
import json
from random import randint

from datetime import datetime
from randomizer import randomize

from mem_manager import MemoryManager, NoUserInputError, LocNoDataError, InvalidLineError
from hnr_parser import parse, InvalidOperatorError, InvalidOperandError, InvalidNumOperandsError
from instructions import get_line_operands, get_line_operator, InvalidInputFormatError, getMusicChar

DATE_FORMAT = "%m/%d/%Y"
MAX_EXECUTABLE_LINES = 100000
FILE_ID_UPPER = 1000000000

def execute(date_string : str, code : str, user_input : str):
    date_obj = datetime.strptime(date_string, DATE_FORMAT).date()
    op_idx_conversion_table, instruction_table = randomize(date_obj)
    memory = MemoryManager(user_input)

    parsed_code = parse(code)

    code_len = len(parsed_code)
    executed_lines_of_code = 0
    music_string = ""
    try:
        while 0 <= memory.read_pc_register() < code_len and executed_lines_of_code < MAX_EXECUTABLE_LINES:
            line = parsed_code[memory.read_pc_register()]
            memory.increment_pc_register()
            operator_id = get_line_operator(line)
            num_args = len(get_line_operands(line))
            operation = instruction_table[num_args][operator_id]
            music_string += getMusicChar(op_idx_conversion_table, num_args, operator_id)
            operation(memory, *get_line_operands(line))
            executed_lines_of_code += 1

        if memory.read_pc_register() < 0:
            raise InvalidLineError()
        
        if executed_lines_of_code >= MAX_EXECUTABLE_LINES:
            raise CodeRuntimeExceedException()
        
        print(generate_json_file(0, music_string, memory.get_outputs()))
    
    except InvalidOperatorError as e:
        print(generate_json_file(1, "", e.line_number))
    except InvalidOperandError as e:
        print(generate_json_file(2, "", e.line_number))
    except InvalidNumOperandsError as e:
        print(generate_json_file(3, "", e.line_number))
    except InvalidInputFormatError:
        print(generate_json_file(4, music_string, memory.get_outputs()))
    except ZeroDivisionError:
        print(generate_json_file(5, music_string, memory.get_outputs()))
    except CodeRuntimeExceedException:
        print(generate_json_file(6, music_string, memory.get_outputs()))
    except LocNoDataError:
        print(generate_json_file(7, music_string, memory.get_outputs()))
    except NoUserInputError:
        print(generate_json_file(8, music_string, memory.get_outputs()))
    except InvalidLineError:
        print(generate_json_file(9, music_string, memory.get_outputs()))
    

def generate_json_file(status_code : int, music_string : int, output):
    json_dict = {"Status code": status_code,
                 }
    if status_code == 1 or status_code == 2:
        json_dict["Line error"] = output
    else:
        json_dict["Code sound"] = music_string
        json_dict["Output"] = output

    file_name = f"backend/outputs/{randint(1, FILE_ID_UPPER)}.json"
    with open(file_name, "w") as f:
        json.dump(json_dict, f)
    return file_name

class CodeRuntimeExceedException(Exception):
    def __init__(self):
        super().__init__("Code has exceeded maximum runtime")

class InsufficientCmdArgumentsException(Exception):
    def __init__(self):
        super().__init__("Script requires filename and date")

# execute("01/21/2024", "SET 1 2\nPRINT_VALUE 1", "")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise InsufficientCmdArgumentsException

    date_string = sys.argv[0]
    code = sys.argv[1]
    user_input = sys.argv[2]
    execute(date_string, code, user_input)
