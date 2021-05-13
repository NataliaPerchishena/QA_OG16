def sumnumber(a):
    sum = 0
    while a != 0:
        sum = sum + a%10
        a = (a-a%10)/10
    return sum


a = abs(int(input('введіть чило: ')))
b = sumnumber(a)
print(int(b))