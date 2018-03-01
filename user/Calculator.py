# allows user to choose an operation
operation = input( '''
please type in the mathematical operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
# allows user to input a number to perform an operation on
x=int(input('Enter first number: '))
y=int(input('Enter second number: '))
# if the operation is addition then the program should add x to y
if operation == '+':
    print('{} + {} = '.format(x, y))
    print(x + y)
# if the operation is subtraction then the program should subtract x from y
elif operation == '-':
    print('{} - {} = '.format(x , y))
    print(x - y)
# if the operation is multiplication then the program should multiply x by y
elif operation == '*':
    print('{} * {} = '.format(x, y))
    print(x * y)
# if the operation is division then the program should divide x by y
elif operation == '/':
    print('{} / {} = '.format(x, y))
    print(x / y)
# if an incorrect character is selected as the operation then the program will display the message.
else:
    print('You have not typeda valid operator, please run the program again.')

