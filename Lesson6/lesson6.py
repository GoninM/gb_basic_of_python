import random

bigger = '>'
smaller = '<'
equal = '='

MinNumber = 1
MaxNumber = 100

while True:
    number = random.randint(MinNumber, MaxNumber)
    print(number)
    answer = input()

    if(answer == equal):
        break
    elif(answer == bigger):
        MaxNumber = number
    elif(answer == smaller):
        MinNumber = number


print("Victory")