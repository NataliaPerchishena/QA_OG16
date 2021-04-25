def func(a, b):
    if a < b:
        print('Лузер')
    elif a > b:
        print('Успішно')
        return
    else:
        print('Майже')
    again()
def povtor():
    a = int(input('введіть 1-шу цифру: '))
    b = int(input('введіть 2-гу цифру: '))
    func(a, b)
def again():
    again = input(''' Хочете продовжити? Натисніть Y якщо так або N якщо ні.''')
    if again.upper() == 'Y':
        povtor()
    elif again.upper() == 'N':
        print('Побачимось пізніше.')
    else:
        povtor()
povtor()
