
from allat import Allatfaj
allatok = []
for i in range(3):
    fajnev = input('Adja meg egy állatfaj nevét! ')
    tomeg = int(input('Hány kilogramm a tömege egy példánynak? '))
    ujAllat = Allatfaj(fajnev, tomeg)
    allatok.append(ujAllat)
    legnehezebb = 0
    for i in range(1,3):
        if allatok[i].tomeg > allatok[legnehezebb].tomeg:
            legnehezebb = i
file = open('legnehezebb.txt', 'w', encoding='utf-8')
file.write(allatok[legnehezebb].fajnev)
file.close()
