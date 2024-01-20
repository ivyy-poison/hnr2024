import random
from datetime import date
from instructions import instructions

DEMO_DATE = date(2024, 1, 21)

def randomize(today : date):

#dict1 = {1: [1, 2, 3, 4, 5], 2: [1, 2, 3, 4, 5, 6], 3: [1, 2, 3, 4, 5, 6, 7]}
#print(dict1)

    output_dict = {}
    for k, _ in instructions.items():
        output_dict[k] = list(map(lambda inst_pair: inst_pair[1], instructions[k]))
    #print(output_dict)

    if not today == DEMO_DATE:
        random.seed(generate_date_seed(today))
        for _, v in output_dict.items():
            random.shuffle(v)
    return output_dict

def generate_date_seed(dateVal : date):
    return dateVal.day *2 + dateVal.month + dateVal.year

def test_randomizer():
    print(randomize(date(2024, 1, 20)))


#print(output_dict)
#print(instructions)
#print(dict1)