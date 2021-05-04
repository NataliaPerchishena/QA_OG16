from random import randint
def rendom_list():
    Min = int(input('Please enter the Min: '))
    Max = int(input('Please enter the Max: '))
    K = int(input('Please enter the quantity: '))
    lst = [randint(Min, Max) for i in range(K)]
    print(lst)
    again()

def again():
   again = input('''
     Do you want to calculate again?
     Please type Y for YES or N for NO.
     ''')


   if again.upper() == 'Y':
    rendom_list()
   elif again.upper() == 'N':
    print('See you later.')

rendom_list()

#list = [1,2,3,4,5,6,7,8,9]
#print("Выбор случайного числа из списка - ", random.choice(list))

