import sys
from datetime import datetime
from randomizer import randomize

from mem_manager import MemoryManager
from hnr_parser import parse
from instructions import get_line_operands, get_line_operator

class CodeRuntimeExceedException(Exception):
    def __init__(self):
        super().__init__("Code has exceeded maximum runtime")

DATE_FORMAT = "%m/%d/%Y"
MAX_EXECUTABLE_LINES = 100000

filename = sys.argv[1]
date_string = sys.argv[2]

date_obj = datetime.strptime(date_string, DATE_FORMAT).date()
instruction_table = randomize(date_obj)
memory = MemoryManager()

parsed_code = parse(filename)
code_len = len(parsed_code)

executed_lines_of_code = 0

while 0 <= memory.read_pc_register() < code_len and executed_lines_of_code < MAX_EXECUTABLE_LINES:
    line = parsed_code[memory.read_pc_register()]
    memory.increment_pc_register()
    operation = instruction_table[len(get_line_operands(line))][get_line_operator(line)]
    operation(memory, *get_line_operands(line))
    executed_lines_of_code += 1

if executed_lines_of_code >= MAX_EXECUTABLE_LINES:
    raise CodeRuntimeExceedException()
