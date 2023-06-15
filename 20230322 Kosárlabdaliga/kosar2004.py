from verseny import Verseny

versenyek:list[Verseny]=[]
f = open('eredmenyek.txt','r',encoding='utf-8')
f.readline()
for row in f:
    versenyek.append(Verseny(row))
f.close()

count = 0
count1 = 0
for i in  versenyek:
    if i.hazaiNev == 'Real Madrid':
        count += 1
    elif i.idegenNev == 'Real Madrid':
        count1 += 1
print(f'3. feladat: Rel Madrid: Hazai: {count}, idegen: {count1}')

def dontetlen():
    for i in versenyek:
        if i.idegenGol == i.hazaiGol:
            return True
        else:
            return False
        
if dontetlen() == False:
    print(f'4. feladat: Volt döntetlen? NEM')
else:
    print(f'4. feladat: Volt döntetlen? IGEN')



for i in versenyek:
    if 'Barcelona' in i.hazaiNev:
        nev = i.hazaiNev
    elif 'Barcelona' in i.idegenNev:
        nev = i.idegenNev
print(f'5. feladat: barcelonai csapat neve: {nev}')

print('6. feladat:')
for i in versenyek:
    if i.idopont == '2004-11-21':
        print(f'\t{i.hazaiNev}-{i.idegenNev} ({i.hazaiGol}:{i.idegenGol})')

    
print('7. feladat:')

stat = {}
for i in versenyek:
    if i.helyszin in stat.keys():
        stat[i.helyszin] += 1
    else:
        stat[i.helyszin] = 1

for key,value in stat.items():
    if value > 20:
        print(f'\t{key}: {value}')