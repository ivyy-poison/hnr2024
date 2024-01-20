import random
from datetime import date
from instructions import instruction_table, instruction_optype_table, get_instruction_optype, get_instruction_function

DEMO_DATE = date(2024, 1, 21)

def randomize(today : date):

#dict1 = {1: [1, 2, 3, 4, 5], 2: [1, 2, 3, 4, 5, 6], 3: [1, 2, 3, 4, 5, 6, 7]}
#print(dict1)

    output_dict = {}
    for k, _ in instruction_table.items():
        output_dict[k] = list(instruction_table[k].copy())
    #print(output_dict)

    if not today == DEMO_DATE:
        random.seed(generate_date_seed(today))
        for _, v in output_dict.items():
            random.shuffle(v)
    opcode_table = {k: list(map(lambda pr: get_instruction_optype(pr), v)) for (k, v) in output_dict.items()}
    opfunc_table = {k: list(map(lambda pr: get_instruction_function(pr), v)) for (k, v) in output_dict.items()}
    idx_conversion_table = {k: list(map(lambda op: instruction_optype_table[k].index(op), v)) for (k, v) in opcode_table.items()}
    return idx_conversion_table, opfunc_table

def generate_date_seed(dateVal : date):
    return dateVal.day *2 + dateVal.month + dateVal.year

def test_randomizer():
    print(randomize(date(2024, 1, 20)))


#print(output_dict)
#print(instructions)
#print(dict1)