def kamatosKamat(osszeg,honapokszama,evesKamat,):
    evszam =  honapokszama/12
    eredmeny = osszeg * ((100+evesKamat) / 100)** evszam
    return eredmeny



osszeg = float(input('Adja meg a felvenni kívánt összeget! '))
honapokszama = int(input('Adja meg a hitelidőt! '))
evesKamat = float(input('Adja meg a THM-t! '))
print(round(kamatosKamat(osszeg,honapokszama,evesKamat), 1))