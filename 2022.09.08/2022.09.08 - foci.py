#4 csapatos focitorna
#kérjük be a csapatok nevét

from random import randint


csapatok = []

for i in range(4):
    nev = input(f'{i + 1} csapat neve: ')
    csapatok.append(nev)

for i in range(4):
    for j in range(i + 1, 4):
        gol1 = randint(0,6)
        gol2 = randint(0,6)
        print(f'{csapatok[i]} - {csapatok[j]}: {gol1} - {gol2}')