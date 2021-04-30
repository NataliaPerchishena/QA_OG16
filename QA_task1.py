a = int(input('input a\n'))
print(a*2, a, a)



#eval = eval(input('Введіть математичний вираз:\n'))
#print(eval)

#def calc():
#    while True:
 #       req = input("введите выражение: ")
  #      if req == "":
  #          break
   #     print(req + "=" + str(eval(req)))


#calc()

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

#calc
 a = int(input('input a\n'))
 b = int(input('input b\n'))
 operator = input('input operator +,-,*, /\n')
 switcher = {
   "-": (a - b),
   "+": (a + b),
   '*': (a * b),
   '/': (a / b)
 }
 print(a, operator, b, '=', +switcher[operator])
mycalc()






calc_again = input(''' Do you want to calculate again? Y for YES or N for NO.''')
if calc_again.upper() == 'Y':
    mycalc()
elif calc_again.upper() == 'N':
    print('See you later.')
else:
    mycalc()
