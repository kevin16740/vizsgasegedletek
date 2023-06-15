def tokeletesSzam(szam):
    osszeg = 0
    for i in range(1,szam):
        if szam % i == 0:
            osszeg += i
    if osszeg == szam:
        return True
    return False


print('2. feladat: Tökéletes számok:')
print('Kérek két természetes számot:')
tol = int(input('tól = '))
ig = int(input('ig = '))

tokeletes_lista = []
print(f'Tökéletes számok {tol} és az {ig} között:')
for i in range(tol,ig+1):
    if tokeletesSzam(i):
        tokeletes_lista.append(i)


if len(tokeletes_lista) == 0:
    print('A megadott tartomáynban nincs tökéletes szám!')
else:
    print(*tokeletes_lista, sep=';')