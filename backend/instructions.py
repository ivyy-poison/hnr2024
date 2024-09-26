def print_value(data, index):
    data.print_to_screen(data.read(index))

def print_string(data, index):
    int_value = int(data.read(index))
    string_array = []
    while int_value:
        string_array.append(chr(int_value % 128))
        int_value //= 128
    string_array.reverse()
    data.print_to_screen(''.join(string_array))

def read_value(data, index):
    try:
        data.write(index, int(data.get_user_input()))
    except ValueError:
        raise InvalidInputFormatError()

def read_string(data, index):
    string = data.get_user_input()
    num = 0
    for char in string:
        num *= 128
        num += ord(char)
    data.write(index, num)

def set_value(data, index, value):
    data.write(index, value)

def not_index(data, set_index, setter_index):
    data.write(set_index, 0 if data.read(setter_index) else 1)

def add_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) + data.read(setter1_index))

def subtract_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) - data.read(setter1_index))

def multiply_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) * data.read(setter1_index))

def divide_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) // data.read(setter1_index))

def modulo_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, data.read(setter0_index) % data.read(setter1_index))

def and_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, 1 if data.read(setter0_index) and data.read(setter1_index) else 0)

def or_indices(data, set_index, setter0_index, setter1_index):
    data.write(set_index, 1 if data.read(setter0_index) or data.read(setter1_index) else 0)

def branch_equal(data, setter0_index, setter1_index, line_number):
    if data.read(setter0_index) == data.read(setter1_index):
        data.set_pc_register(line_number)

def branch_not_equal(data, setter0_index, setter1_index, line_number):
    if data.read(setter0_index) != data.read(setter1_index):
        data.set_pc_register(line_number)

def branch_less_than(data, setter0_index, setter1_index, line_number):
    if data.read(setter0_index) < data.read(setter1_index):
        data.set_pc_register(line_number)

def branch_less_equal(data, setter0_index, setter1_index, line_number):
    if data.read(setter0_index) <= data.read(setter1_index):
        data.set_pc_register(line_number)

def branch_greater_than(data, setter0_index, setter1_index, line_number):
    if data.read(setter0_index) > data.read(setter1_index):
        data.set_pc_register(line_number)

def branch_greater_equal(data, setter0_index, setter1_index, line_number):
    if data.read(setter0_index) >= data.read(setter1_index):
        data.set_pc_register(line_number)

def get_instruction_optype(instruction):
    return instruction[0]

def get_instruction_function(instruction):
    return instruction[1]

def get_line_operator(line : list[int]):
    return line[0]

def get_line_operands(line : list[int]):
    return line[1:]

def get_line_operand_count(line : list[int]):
    return len(get_line_operands(line))

instruction_table = {
                    1: [
                            ('PRINT_VALUE', print_value), ('PRINT_STRING', print_string),
                            ('READ_VALUE', read_value), ('READ_STRING', read_string)
                        ],
                    2: [
                            ('SET', set_value), ('NOT', not_index)
                        ],
                    3: [
                            ('ADD', add_indices), ('SUB', subtract_indices),
                            ('MULT', multiply_indices), ('DIV', divide_indices), ('MOD', modulo_indices),
                            ('AND', and_indices), ('OR', or_indices), ('BEQ', branch_equal), ('BNE', branch_not_equal),
                            ('BLT', branch_less_than), ('BLE', branch_less_equal), ('BGT', branch_greater_than), ('BGE', branch_greater_equal)
                        ]
                }

instruction_optype_table = {k: list(map(lambda pr: get_instruction_optype(pr), v)) for (k, v) in instruction_table.items()}

instruction_name_table = {j for i in instruction_table.values() for j, k in i}

instruction_table_count = [0] * 4
for i in range(1, 4):
    instruction_table_count[i] = instruction_table_count[i - 1] + len(instruction_table[i])

def getMusicChar(op_idx_conversion_table : dict[list[int]], num_args : int, operator_id : int) -> chr:
    return chr(65 + instruction_table_count[num_args - 1] + op_idx_conversion_table[num_args][operator_id])

class InvalidInputFormatError(Exception):
    pass
