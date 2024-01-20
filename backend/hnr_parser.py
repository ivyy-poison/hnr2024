from instructions import instruction_optype_table, get_line_operand_count, get_line_operator, get_line_operands

def parse(code : str) -> list[tuple[int]]:
    def convert_operands_to_int(operand) -> int:
        try:
            return int(operand)
        except ValueError:
            raise InvalidOperandError
    
    codelist = (list(ln.split()) for ln in code.split('\\n') if len(ln.replace(' ', '')))
    parsed_code = []
    try:
        for instruction in codelist:
            operator_id = instruction_optype_table[get_line_operand_count(instruction)].index(get_line_operator(instruction).upper())
            operands = map(convert_operands_to_int, get_line_operands(instruction))
            parsed_code.append((operator_id, *operands))
        return parsed_code
    except InvalidOperandError:
        raise InvalidOperandError(len(parsed_code))
    except ValueError:
        raise InvalidOperatorError(len(parsed_code))

class InvalidOperatorError(Exception):
    def __init__(self, line_number : int = None):
        self.line_number = line_number

class InvalidOperandError(ValueError):
    def __init__(self, line_number : int):
        self.line_number = line_number
