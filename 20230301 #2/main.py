from versenyzok import Versenyzo

versenyzok :list[Versenyzo]=[] 

file = open('snooker.txt','r',encoding='utf-8')
file.readline()
for row in file:
    versenyzok.append(Versenyzo(row.strip()))
file.close()

print(f'3. feladat A világranglistán {len(versenyzok)} versenyző szerepel')


def atlagBevetel():
    bevetel = 0
    for i in versenyzok:
        bevetel += i.nyeremeny
    atlag = bevetel / len(versenyzok)
    return round(atlag,1)
print(f'4. feladat A versenyzők átlagosan {atlagBevetel()} fontot keresték')


bevetel = 0
maxIndex = 0
for index,item in enumerate(versenyzok):
    if item.orszag == 'Kína':
        if bevetel < item.nyeremeny:
            bevetel = item.nyeremeny
            maxIndex = index

print(f'5. feladat A legjobb kereső kínai versenyző:')
print(f'\tHelyezés: {versenyzok[maxIndex].helyezes}')
print(f'\tNév: {versenyzok[maxIndex].nev}')
print(f'\tOrszág: {versenyzok[maxIndex].orszag}')
print(f'\tNyeremény összege: {versenyzok[maxIndex].nyeremeny} Ft')

norveg = 0
for i in versenyzok:
    if i.orszag == 'Norvégia':
        norveg += 1
if norveg != 0:
    print('6. feladat: A versenyzők között van norvég versenyző.')
else:
    print('6. feladat: A versenyzők között nincs norvég versenyző.')
   
stat = {}
for i in versenyzok:
    if i.orszag in stat.keys():
        stat[i.orszag] += 1
    else:
        stat[i.orszag] = 1

print('7. feladat: Statisztika')
x = []
for key,value in stat.items():
    if value > 4:
        print(f'\t{key}-{value} fő')
