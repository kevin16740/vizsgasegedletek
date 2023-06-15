from epulet import Epulet
epuletek:list[Epulet]=[]
f = open('legmagasabb.txt','r',encoding='utf-8')
f.readline()
for row in f:
    epuletek.append(Epulet(row.strip()))
f.close()

print(f'3.2 feladat: {len(epuletek)} épület található az állományban!')
emeletek = 0
for i in epuletek:
    emeletek += i.emelet
print(f'3.3 feladat: {emeletek} emelet található összesen.')

magassag = epuletek[0]
for i in epuletek:
    if i.magassag >magassag.magassag:
        magassag = i
print('3.4 feladat: A legmagasabb épület adatai')
print(f'\tNév: {magassag.nev}')
print(f'\tVáros: {magassag.varos}')
print(f'\tOrszág: {magassag.orszag}')
print(f'\tMagasság: {magassag.magassag}')
print(f'\tEmeletek száma: {magassag.emelet}')
print(f'\tÉpítés éve: {magassag.epult}')

def olasz(epuletek):
    for i in epuletek:
        if i.orszag == 'Olaszország':
            return 'Van'
    return 'Nincs'

print(f'3.5 feladat: {olasz(epuletek)} olasz épület az adatok között!')