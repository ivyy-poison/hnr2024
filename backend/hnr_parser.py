from instructions import instruction_optype_table, instruction_name_table, get_line_operand_count, get_line_operator, get_line_operands

def parse(code : str) -> list[tuple[int]]:
    def convert_operands_to_int(operand) -> int:
        try:
            return int(operand)
        except ValueError:
            raise InvalidOperandError
    
    codelist = (list(ln.split()) for ln in code.split('\n') if len(ln.replace(' ', '')))
    parsed_code = []
    for instruction in codelist:
        try:
            operator_id = instruction_optype_table[get_line_operand_count(instruction)].index(get_line_operator(instruction).upper())
        except (ValueError, KeyError):
            if get_line_operator(instruction).upper() in instruction_name_table:
                raise InvalidNumOperandsError(len(parsed_code))
            raise InvalidOperatorError(len(parsed_code))
        try:
            operands = map(convert_operands_to_int, get_line_operands(instruction))
        except InvalidOperandError:
            raise InvalidOperandError(len(parsed_code))
        parsed_code.append((operator_id, *operands))
    return parsed_code

class InvalidOperatorError(Exception):
    def __init__(self, line_number : int = None):
        self.line_number = line_number

class InvalidOperandError(ValueError):
    def __init__(self, line_number : int):
        self.line_number = line_number

class InvalidNumOperandsError(ValueError):
    def __init__(self, line_number : int):
        self.line_number = line_number
