from math import sqrt

def masodfokuGyokei(a, b, c):
    if b*b < 4*a*c:
        raise ValueError('Nincs megoldás a valós számok halmazán!')
    x1 = -b + sqrt(b*b - 4*a*c)/(2*a)
    x2 = -b - sqrt(b*b - 4*a*c)/(2*a)
    return x1, x2

print('Másodfokú egyenlet megoldása')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

try:
    print(f'Az egyenlet gyökei: {masodfokuGyokei(a,b,c)}')
except ValueError as error:
    print(error)