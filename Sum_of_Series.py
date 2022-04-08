import math 

number = int(input("Please Enter any Positive Number  : "))
total = 0

total = math.pow((number * (number + 1)) /2, 2)

for i in range(1, number + 1):
    if(i != number):
        print("%d^3 + " %i, end = ' ')
    else:
        print("{0}^3 = {1}".format(i, total))