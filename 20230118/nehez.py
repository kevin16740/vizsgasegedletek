from allat import Állatfaj

allatok = []

for i in range(3):
    fajnév = input('Add meg egy állatfaj nevét! ')
    tömeg = int(input('Hány kg a tömege egy példánynak? ')) 
    ujallat = Állatfaj(fajnév,tömeg)
    allatok.append(ujallat)

legnehezebb = allatok[0]

for allat in allatok:
    if allat.tömeg > legnehezebb.tömeg:
        legnehezebb = allat

f = open('legnehezebb.txt', 'w', encoding='utf-8')
f.write(f'A(z) {legnehezebb.fajnév} tömege {legnehezebb.tömeg} kg')
f.close()

for allat in allatok:
    print(f'A(z) {allat.fajnév} töemege {allat.tömeg} kg.')