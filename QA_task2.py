#function calc
def calculate():
    try:
        number_1 = float(input('Please enter the first number: '))
    except ValueError:
        print('You have not typed, please run the program again.')
        calculate()
    try:
        number_2 = float(input('Please enter the second number: '))
    except ValueError:
        print('You have not typed, please run the program again.')
        calculate()
    operation = input('''
        Please type in the math operation you would like to complete:
         + for addition
         - for subtraction
         * for multiplication
        / for division
    ''')
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
    # Добавление функции again() в calculate()
    again()


def again():
   calc_again = input('''
     Do you want to calculate again?
     Please type Y for YES or N for NO.
     ''')


   if calc_again.upper() == 'Y':
    calculate()
   elif calc_again.upper() == 'N':
    print('See you later.')
   else:
    again()
calculate()


#function simple calc
def mycalc():
    switcher = {
        "-": (a - b),
        "+": (a + b),
        '*': (a * b),
        '/': (a / b)
    }
    print(a, operator, b, '=', +switcher[operator])


a = int(input('input a\n'))
b = int(input('input b\n'))
operator = input('input operator +,-,*, /\n')
mycalc()


#function simple calc2
def simplecalc(a, b, c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c =='/':
        return a/b
    else:
       return ('nonetype operator')

a = int(input('input a\n'))
b = int(input('input b\n'))
c = input('input c (operator +,-,*, /)\n')
print(a, c, b, '=', str(simplecalc(a, b, c)))