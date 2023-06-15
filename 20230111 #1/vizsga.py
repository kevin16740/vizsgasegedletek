def vizsga(pont):
    if pont >= 48:
        return True
    else:
        return False


nev = input('Add meg a vizsgázó nevét! ')
while nev != '':
    nev = input('Add meg a vizsgázó nevét! ')
    pont = int(input('Add meg a pontszámát! '))
    if vizsga(nev, pont) == True:
        print(f'{nev} vizsgája sikeres.')
    else:
        print(f'{nev} vizsgája sikertelen.')