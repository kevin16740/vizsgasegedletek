from versenyzo import Versenyzo
versenyzok:list[Versenyzo] = []

f = open('ub2017egyeni.txt','r',encoding='utf-8')
f.readline()
for row in f:
    versenyzok.append(Versenyzo(row.strip()))
f.close()



print(f'3. feladat: Egyéni indulók: {len(versenyzok)} fő')



count = 0
for i in versenyzok:
    if i.kategoria == 'Noi':
        if i.tavSzazalek == 100:
            count += 1
print(f'4. feladat: Célba érkező női sportolók: {count} fő')



nev = input('5. feladat? Kérem a sportoló nevét: ')
for i in versenyzok:
    if nev == i.versenyzo:
        print('Indult egyéniben a sportoló? Igen')
    else:
        print('Indult egyéniben a soprtoló? Nem')
        break
    if nev == i.versenyzo and i.tavSzazalek == 100:
        print('Teljesítette a teljes távot? Igen')
    elif nev == i.versenyzo and i.tavSzazalek != 100:
        print('Teljesítette a teljes távot? Nem')






count = 0
idomeres = 0
for i in versenyzok:
    if i.tavSzazalek == 100 and i.kategoria == 'Ferfi':
        count += 1
        idomeres += i.idoOraban()
print(f'7. feladat: Átlagos idő: {idomeres / count} óra')



print('8. feladat: Verseny győztesei:')
min = 100000000000000000000
rajt = 0
nev = ''
ido = ''
for i in versenyzok:
    if i.kategoria == 'Noi' and i.tavSzazalek == 100 and i.idoOraban() < min:
        nev = i.versenyzo
        rajt = i.rajtszam
        min = i.idoOraban()
        ido = i.versenyIdo
print(f'Női: {nev} ({rajt}) - {ido}')
min = 1000000000000000000
nev = ''
rajt = 0
ido = ''
for i in versenyzok:
    if i.kategoria == 'Ferfi' and i.tavSzazalek == 100 and i.idoOraban() < min:
        nev = i.versenyzo
        rajt = i.rajtszam
        min = i.idoOraban()
        ido = i.versenyIdo
print(f'Férfiak: {nev} ({rajt}) - {ido}')
print()