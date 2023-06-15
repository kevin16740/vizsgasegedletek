#Olvasson be egy dátumot és függény(ek) segítségével döntse el, hogy a dátum helyes-e


def szokoev(ev):
    if ev % 4 != 0:
        return False
    if ev % 100 == 0 and ev % 400 != 0:
        return False
    return True


def datumEllenorzes(datum):
    splitted = datum.split('.')
    if len(splitted) != 3:
        return False
    ev = int(splitted[0])
    honap = int(splitted[1])
    nap = int(splitted[2])
    
    honapok = [31,28,31,30,31,30,31,31,30,31,30,31]
    if honap > 12 or honap < 1:
        return False
    if szokoev(ev):
        if honap == 2 and nap > 30:
            return False
    elif nap > honapok[honap-1]:
        return False
    if ev > 2023:
        return False
    return True
datum = input('Kérem a dátumot (éééé.hh.nn): ')

if datumEllenorzes(datum) == True:
    print('A dátum megfelelő')
else:
    print('A dátum nem megfelelő')