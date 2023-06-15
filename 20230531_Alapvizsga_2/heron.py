import math
print('1. feladat: Háromsög kerülete és területe')
print('Kérem a háromszög oldalait')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
s = (a+b+c)/2
print(f'K = {a+b+c}')
T = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'T = {T}')