import random
import math
szamok = []


for i in range(10):
    szamok.append(random.randint(10,99))

def ez_prím(szam):
    for i in range(2,szam-1):
        if szam % i == 0:
            return False
    return True
            

print(szamok)
for i in szamok:
    if ez_prím(i) == True:
        print('Van prímszám a listában!')
        break
else:
    print('Nincs prímszám a listában!')