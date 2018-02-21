operation = input( '''
please type in the mathematical operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

x=int(input('Enter first number: '))
y=int(input('Enter second number: '))

if operation == '+':
    print('{} + {} = '.format(x, y))
    print(x + y)

if operation == '-':
    print('{} - {} = '.format(x , y))
    print(x - y)

if operation == '*':
    print('{} * {} = '.format(x, y))
    print(x * y)
if operation == '/':
    print('{} / {} = '.format(x, y))
    print(x / y)
else:
    print('You have not typeda valid operator, please run the program again.')

