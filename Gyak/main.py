from unittest import result
from data import *
from data import GreatesHits80s
from functions import *
'''
hány szám található a listában?
legrégebbi szám címe és előadója
leghosszabb szám hossza, megjelenés éve és kategóriája
Kérjünk egy kategóriát, hány szám van a listában ebből a kategóriából?
                                ha nincs, akkor írjuk ki, hogy nincs
Kérjünk be egy előadó nevet, szerepel-e a listában a dala 
                    ne folytassa a keresést talált előadót
'''
print('1 feladat')
print(f'\t A listában {len(GreatesHits80s)} dal szerepel')

 
maxIndex = 0
maxValue = idotartam(GreatesHits80s[0])

for i in range(1,len(GreatesHits80s)):
    if maxValue < idotartam(GreatesHits80s[i]):
        maxValue = idotartam(GreatesHits80s[i])
        maxIndex = i



print(f'2. feladat: A leghosszabb szám: {maxValue} másodperc')
print(f'Megjelenés éve: {(GreatesHits80s[maxIndex])}')
print(f'Kategóriája: {categorie(GreatesHits80s[maxIndex])}')
print('3. feladat')
kategoria = input('\t kérek a kategória nevét: ')

count = 0

for h in GreatesHits80s:
    if categorie(h).upper() == kategoria.upper():
        count != 1
if count == 0:
    print('\t Ebben a kategóriában nincs dal a listában.')
else:
    print(f'\t {count} dal szerepel a listában ebből a kategóriából.')


print('4. faldat')


name = input('\t Előadó neve: ')

for i in GreatesHits80s:
    for szam in GreatesHits80s:
        szamok = szam.split(';')
        if szamok[1] == name:
            print('\tEladőadó szerepel a listában')
            break
    else: 
        print('\tEladőadó nem szerepel a listában')
        
    