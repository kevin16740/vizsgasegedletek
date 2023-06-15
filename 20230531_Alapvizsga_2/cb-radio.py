from cb import CB
bejegyzesek:list[CB]=[]
f = open('cb.txt','r',encoding='utf-8')
f.readline()
for row in f:
    bejegyzesek.append(CB(row.strip()))
f.close()

sanyiDb = 0
for i in bejegyzesek:
    if i.nev == 'Sanyi':
        sanyiDb += 1





print('3. feladat: CB-Rádió')
print(f'3.2 feladar: Bejegyzések száma: {len(bejegyzesek)} db')
print(f'3.1 feladat: Sanyihoz tartozó bejegyzések :{sanyiDb} db')
print('3.3 feladat: A legtöbb adás: ')

legtobb = bejegyzesek[0]
for i in bejegyzesek:
        if i.adasDb > legtobb.adasDb:
             legtobb = i

for i in bejegyzesek:
        if i.adasDb == legtobb.adasDb:
            print(f'\tIdő: {i.ora}:{i.perc} Darab: {i.adasDb} Név: {i.nev}')

f = open('cb2.txt','w',encoding='utf-8')
f.write('Kezdes,Nev,AdasDb\n')
for i in bejegyzesek:     
     f.write(f'{i.idoPercben()};{i.nev};{i.adasDb}\n')
f.close()

stat={}
for i in bejegyzesek:
    if i.nev in stat.keys():
        stat[i.nev] += 1
    else:
         stat[i.nev] = 1
for key,value in stat.items():
    print(f'\t{key} : {value} db')