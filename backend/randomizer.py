import random
import datetime 
from parser import instructions

today = datetime.date.today()
today_year = today.year
today_month = today.month
today_day = today.day
print(instructions)
random.seed(today_day*2 + today_month + today_year)

#dict1 = {1: [1, 2, 3, 4, 5], 2: [1, 2, 3, 4, 5, 6], 3: [1, 2, 3, 4, 5, 6, 7]}
#print(dict1)
for i in range(1, 4):
    if today_day != 20 and today_day != 21:
        #random.shuffle(dict1[i])
        random.shuffle(instructions[i])
#print(instructions)
#print(dict1)