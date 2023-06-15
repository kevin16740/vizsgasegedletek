def benneVanE(sazm):
    elso = 1
    masodik = 1
    while kovetkezo <= szam:
        kovetkezo = elso + masodik
        elso = masodik
        masodik = kovetkezo
        if kovetkezo == szam:
            return True
    return False
szam = int(input('Adja meg egy számot: '))

if benneVanE(szam) == True:
    print('A szám benne van a ísorozatban')
else:
    print('Nincs benne a sorozatban')