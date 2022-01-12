import time as t
import os
t.sleep(5)
x= "Enter a valid option!"
os.system ("clear")
print ("""Lekzcal is a python programme for performing simple math operation""")
t.sleep(8)
os.system("clear")
t.sleep(4)
def loop():
	os.system ("clear")
	os.system (" figlet Lekzcal")
	t.sleep(6)
	print("""
	Tool Name:Lekzcal
	Creator:Lêkzï
	Contact me on whatsapp:+2347064822519
	Team:Greyhaxors 
	""")
	print("""Special thanks to Spider Anongrey hat for his support""")
loop()
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')
