nev = input('Adja meg a diák nevét! ')
tantargy = 0
jeyek = []
def atlagSzamitasok(tantargyJegyek):
    osszeg = 0
    jegyAtlag = 0
    for item in tantargyJegyek:
        osszeg += int(item)
        jegyAtlag =  (osszeg / len(tantargyJegyek))
    return jegyAtlag

def jegy():
    erdemjegy = 0
    if atlagSzamitasok(tantargyJegyek) < 1.5:
        erdemjegy = 1
    elif atlagSzamitasok(tantargyJegyek) > 1.49 and atlagSzamitasok(tantargyJegyek) < 2.5:
        erdemjegy = 2
    elif atlagSzamitasok(tantargyJegyek) > 2.49 and atlagSzamitasok(tantargyJegyek) < 3.5:
        erdemjegy = 3
    elif atlagSzamitasok(tantargyJegyek) > 3.49 and atlagSzamitasok(tantargyJegyek) < 4.5:
        erdemjegy = 4
    elif atlagSzamitasok(tantargyJegyek) > 4.49:
        erdemjegy = 5
    jeyek.append(erdemjegy)
    return erdemjegy
def jegyKiir(erdemjegy):
    if erdemjegy == 1:
        print('Elégtelen')
    elif erdemjegy == 2:
        print('Elégséges')
    elif erdemjegy == 3:
        print('Közepes')
    elif erdemjegy == 4:
        print('Jó')
    elif erdemjegy == 5:
        print('Jeles')

def evvegijegy(jeyek):
    osszeg = 0
    for i in jeyek:
        osszeg += i
        jegyesjegy = osszeg / 5
    return jegyesjegy    
eevvegi = evvegijegy(jeyek)
def osztondij(evvegi):
    if evvegi < 2.99 and evvegi > 2:
        return 8000
    elif evvegi < 3.99 and evvegi > 3:
        return 25000
    elif evvegi < 4.49 and evvegi > 4:
        return 42000
    elif evvegi > 4.49:
        return 59000

for i in range(5):
    tantargy += 1
    tantargyNev = input(f'{tantargy}. tantárgy neve: ')
    tantargyJegyek = input(f'\t{tantargyNev} jegyek: ')
    print(f'Év végi jegy {jegy()}  ')
print(f'{nev} év végi átlaga: {evvegijegy(jeyek)}')
print(f'{nev} öszöntöndíja: {osztondij(evvegi)} Ft,-')

