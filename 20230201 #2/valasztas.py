from jelolt import Jelolt

jeloltek: list[Jelolt] = []

def keres(nev):
    for item in jeloltek:
        if item.nev == nev:
            return item
    return False
file = open('szavazatok.txt', 'r', encoding='utf-8')
for item in file:
    jeloltek.append(Jelolt(item.strip()))
file.close()

print(f'2.feladat: A választáson {len(jeloltek)} képsviselőjelölt indult.')

nev = input('Írja be a keresett képviselőjelölt nevét: ')
talalat = keres(nev)
if talalat == False:
    print('Ilyen nevű képviselőjelölt nem szerepel.')
else:
    print(f'3.feladat: Képviselő neve: {nev} \n\tA jelölt a {talalat.kerulet}-s számú körzetben indult\t\nA kapott szavazatok száma: {talalat.szavazatokSzama}')

osszesSzavazat = 0
for item in jeloltek:
    osszesSzavazat += item.szavazatokSzama

print(f'4.faladat: A választáson {osszesSzavazat} szavazó a jogosultak {osszesSzavazat / 12345 * 100}%-a vett részt.')


maxErtek = 0
maxElem = ''
for item in jeloltek:
    if item.kerulet == 1 and maxErtek < item.szavazatokSzama:
        maxErtek = item.szavazatokSzama
        maxElem = item


if maxElem.part == '':
    print(f'5+1.faladat: A legtöbb szavazat: \t\n{maxElem.nev} : {maxElem.szavazatokSzama}')
else:
    print(f'5+1.faladat: A legtöbb szavazat: \t\n{maxElem.nev} : {maxElem.szavazatokSzama}')


stat = {}
for item in jeloltek:
    if item.part in stat:
        stat[item.part] += item.szazvazatokSzama
    else:
        stat[item.part] = item.szavazatokSzama

print('6.Feldat:')

for key, value in stat.items():
    if key == '.':
        print(f'\tfüggetlen: {value} szavazatok.')
    else:
        print(f'\t{key}: {value} szavazatok.')


file = open('TISZ.csv','w',encoding='utf-8')




file.write('Körzet:Név:Szavazatok száma\n')
for item in jeloltek:
    if item.part == 'TISZ':
        file.write(f'{item.kerulet};{item.nev};{item.szavazatokSzama}')

file.close()