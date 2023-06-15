
from mondatok_alap import névelő, jelző
print('Adjon meg három főnevet!')
szam = 1
for i in range(3):
    szó = input(f'{szam} főnév : ')
    szam += 1
    névelő(szó)
    print(f'{névelő(szó)} {szó} {jelző()}')