import random

bigger = '>'
smaller = '<'
equal = '='

MinNumber = 1
MaxNumber = 100

answer = None
while answer != equal:
    number = random.randint(MinNumber, MaxNumber)
    print(number)
    answer = input()

    if(answer == bigger):
        MaxNumber = number - 1
    elif(answer == smaller):
        MinNumber = number + 1


print("Victory")