from epitmeny import epitmeny

epitmenyek :list[epitmeny] = []
A = 0
B = 0
c = 0


def beolvas():
    f = open('utca.txt', 'r', encoding='utf-8')
    splitted = f.readline().strip(' ').split(';')
    A = int(splitted[0])
    B = int(splitted[1])
    C = int(splitted[2])
    for sor in f:
        e = epitmeny(sor.strip())
        epitmenyek.append(e)
    f.close()

def kereses(adoszam):
    talalt = False
    for et in epitmenyek:
        if et.adoszam == adoszam:
            print(f'{et.utca} {et.hazszam}')
        talalt = True
    if talalt != True:
        print('Nem szerepel az adatállományban.')


def ado(adosav,alapterulet):
    if adosav == 'A':
        A * alapterulet
    elif adosav == 'B':
        ado = B * alapterulet
    elif adosav == 'C':
        ado = C * alapterulet
    if ado < 10000:
        return 0
    else:
        return ado

beolvas()
print('2.     feladat. A mintban {len(epitmenyek)} telek szerepel.')
adoszam = input('3. feladat. Egy tulajdonos adószáma: ')
talalat = kereses(adoszam)
ado('A',500)
print(f"{ado('A',500)}")s