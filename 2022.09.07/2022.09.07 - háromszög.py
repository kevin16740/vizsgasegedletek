#k kérjünk be 3 valós számot
# Dötsük el, hogy lehet-e belőle 3szöget szerkeszteni?

from math import sqrt
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and b + c > a and c + a > b:
        print('A háromszög szerkeszthető!')
        s = (a+b+c) / 2
        T = sqrt(s * (s - a) * (s - b) * (s - c))
        print('A háromszög területe:', T)
else:
        print('A háromszög nem szerkeszthető!')
