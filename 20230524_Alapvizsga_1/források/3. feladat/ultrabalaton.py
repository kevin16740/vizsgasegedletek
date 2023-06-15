from versenyzo import *

versenyzok:list[Versenyzo]=[]
f = open('ub2017egyeni.txt','r', encoding='utf-8')
f.readline()
for row in f:
    versenyzok.append(Versenyzo(row.strip()))
f.close()

print('1 feladat:')
print(f'A versenyen indulók száma: {len(versenyzok)}')

print('2. feladat:')
count = 0
for i in versenyzok:
    if i.kategoria == 'Noi' and i.szazalek == 100:
        count += 1
print(f'Célba érkező női sportolók: {count} fő')

leghosszabb = ''
rajtszam = 0
eredmeny = ""
for i in versenyzok:
    if len(i.nev) > len(leghosszabb):
        leghosszabb = i.nev
        rajtszam = i.rajtszam
        eredmeny = i.idoeredmeny
print('4. feladat: A leghosszabb nevű futó:')
print(f'\tNév: {leghosszabb}')
print(f'\tRajtszám: {rajtszam}')
print(f'\tEredmény: {eredmeny}')

ora = 0
for i in versenyzok:
    if i.szazalek == 100 and i.kategoria == 'Ferfi':
        ora += i.teljesites
count = 0
for i in versenyzok:
    if i.kategoria == 'Ferfi' and i.szazalek == 100:
        count += 1
print(f'3.5 Férfi sportolók átlagos ideje: {ora / count} óra')