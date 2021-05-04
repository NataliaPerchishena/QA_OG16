from random import randint

def rendom_list():
    Min = int(input('Please enter the Min: '))
    Max = int(input('Please enter the Max: '))
    K = int(input('Please enter the quantity: '))
    return [randint(Min, Max) for i in range(K)]

b1 = rendom_list()
print(b1)
b2 = rendom_list()
print(b2)
f = list((set(b1) ^ set(b2)))
print(f)




# памятка по сравнению і подобное (для себя)
#print(list(set(b1+b2)))
#print(list(((set(b1) | set(b2)) - set(b1) & set(b2))))

#a = [i for i in range(10)]
#print(a)
#b = [i for i in range(5)]
#print(b)
#print(set(a).difference(b))
#print(set(a).intersection(b))
#print(set(a) - set(b))
#print(set(a) & set(b))



