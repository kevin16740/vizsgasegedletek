print('1. feladat: a háromszög szerkehszthetősége \nKérem a háromszög oldalait!')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('A háromszög megszerkeszthető!')
elif (a + b) < c or (a + c) < b or (b + c) < a:
    print('A háromszög nem szerkeszthető a megadott adatokkal!')