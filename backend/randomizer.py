import random
import datetime 
from instructions import instructions

def randomize(today):   
    today_year = today.year
    today_month = today.month
    today_day = today.day
    #print(instructions)
    random.seed(today_day*2 + today_month + today_year)

#dict1 = {1: [1, 2, 3, 4, 5], 2: [1, 2, 3, 4, 5, 6], 3: [1, 2, 3, 4, 5, 6, 7]}
#print(dict1)

    output_dict = {1: [], 2: [], 3: []}
    for i in range(1, 4):
        for j in instructions[i]:
            output_dict[i].append(j[1])
    #print(output_dict)

    for i in range(1, 4):
        if today_day != 21:
            #random.shuffle(dict1[i])
            random.shuffle(output_dict[i])
    return output_dict

print(randomize(datetime.date.today()))


#print(output_dict)
#print(instructions)
#print(dict1)