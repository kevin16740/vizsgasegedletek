from versenyzo import Versenyzo

versenyzok: list[Versenyzo] = []


file = open('helsinki.txt','r',encoding='utf-8')

for row in file:
    row = row.strip()
    v = Versenyzo(row)
    versenyzok.append(v)

file.close()

print(f'3. feldat: \n\tPontszerző helyezések száma: {len(versenyzok)}')

print(f'4. feladat:')

stat = {}


for i in versenyzok:
    if i.helyezes in stat.keys():
        stat[i.helyezes] += 1
    else:
        stat[i.helyezes] = 1

print(f'\tArany: {stat[1]}')
print(f'\tEzüst: {stat[2]}')
print(f'\tBronz: {stat[3]}')
print(f'Összesen: {stat[1] + stat[2] + stat[3]}')

totalPoints = 0

for item in versenyzok:
    totalPoints += item.olympicPoints
print(f'5. feladat: \nolimpiai pontok száma: {totalPoints}')

uszas = 0
torna = 0
for i in versenyzok:
    if i.helyezes <= 3 and i.sportTag == 'torna':
        torna += 1
    elif i.helyezes <= 3 and i.sportTag =='úszás':
        uszas += 1
if uszas > torna:
    print('6. feladat: Úszásban szereztek több érmet.')
elif torna > uszas:
    print('6. feladat: tornában szereztek több érmet.')
else:
    print('6. feladat: Egyenlő volt az érmek száma.')

file = open('helsinki2.txt', 'w', encoding='utf-8')
for item in versenyzok:
    if item.sportTag == 'kajakkenu':
        file.write(f'{item.helyezes} {item.olympicPoints} {item.olympicPoints} kajak-kenu {item.versenySzam}\n')
    else:
        file.write(f'{item.helyezes} {item.olympicPoints} {item.olympicPoints} {item.sportTag} {item.versenySzam}\n')
file.close()

maxValue = versenyzok[0].sportoloSzam
maxItem = versenyzok[0]
for i in versenyzok:
    if i.sportoloSzam > maxItem:
        maxItem = i
        maxValue = i.sportoloSzam

print('8. feladat:')
print(f'Helyezés: {maxItem}')
print(f'Sportág: {i.sportTag}')
print(f'Sportolók száma: {i.sportoloSzam}')