#1
number = int(input('enter number: '))
print(number + 2)

#2
number2 = int(input('enter number: '))

while( not(number2>0) or not(number2 < 10) ):
    print('wrong number, enter number 0...10')
    number2 = input()

print(number2**2)

#3

first_name = input('Enter your first name: ')
last_name = input('Enter your last_name: ')
age = int(input('How old are you: '))
ves = int(input('ves?: '))

if(age < 30 and (ves > 50 and ves < 120)):
    print('good')
elif((age > 30 and age < 40) and (ves < 50 or ves > 120)):
    print(':(')
elif(age > 40 and (ves < 50 or ves > 120)):
    print('need doctor')
else:
    print('fff')

