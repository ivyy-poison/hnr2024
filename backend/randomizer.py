import random
import datetime 
from parser import instructions

today = datetime.date.today()
today_year = today.year
today_month = today.month
today_day = today.day
print(today_day)
random.seed(today_day*2 + today_month + today_year)
for i in range(1, 4):
    random.shuffle(instructions[i])
#print(instructions)