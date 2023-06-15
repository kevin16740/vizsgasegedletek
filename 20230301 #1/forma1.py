from versenyzok import Versernyzok

pilotak : list [Versernyzok] = []

file = open('pilotak.csv','r',encoding='utf-8')
file.readline()
for row in file:
    pilotak.append(Versernyzok(row.strip()))
file.close()



print(f'3. feladat: {len(pilotak)}')

print(f'4. feladat: {pilotak[-1].nev}')

print(f'5. feladat:')    

for item in pilotak:
    if item.szuletesi_datum < '1901.01.01':
        print(f'\t {item.nev} ({item.szuletesi_datum})')
def kicsi():
    rajtSzam = 10000000
    for item in pilotak:
        if item.rajtszam != '':
            if item.rajtszam < rajtSzam:
                rajtSzam = item.rajtszam
                nemzetiseg = item.nemzetiseg
    return nemzetiseg

print(f'6 feladat: {kicsi()}')

stat = {}

for item in pilotak:
    if item.rajtszam  in stat.keys():
        stat[item.rajtszam] += 1
    else:
        stat[item.rajtszam] = 1
    
x = []    
for key,value in stat.items():
    if value >= 2 and key != '':
        x.append(key)
print(''.join(x))