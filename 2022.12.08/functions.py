
from versenytav import Versenytav

versenytavok = []

def beolvas(fajlnev: str):
    f = open(fajlnev,'r',encoding='utf-8')
    f.readline()
    for row in f:
        vt = Versenytav(row)
        versenytavok.append(vt)
    f.close()



def celbaerkezokAranya() -> float :
    return (1 - len(versenytavok) / 691) * 100



def Versenyzokszama(tav, nem):
    darab = 0
    for vt in versenytavok:
        if tav == vt.Tav() and nem == vt.Nem():
            darab += 1
    return darab




def VoltTobbMint(masodpercek):
    for vt in versenytavok:
        if masodpercek < vt.masodpercek:
            return True
    return False



def Gyoztes(tav, kategoria):
    min = 99999999
    versenyzo = ''
    for vt in versenytavok:
        if tav == vt.Tav() and kategoria == vt.kategoria and vt.masodpercek < min:
            min = vt.masodpercek
    return gyoztes