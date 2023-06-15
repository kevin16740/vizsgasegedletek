from functions import *

print(f'3.Feladat: A listában {varosokSzama()} város található!')
print(f'4. Feldatat: Legalább 10 milliós városok száma: {megfeleltVaros()}.')
legnepesebbVaros()
print(f'6. Feladat:1{kinaiVarosok()} Legnagyobb kínai város össznépessége: {kinaiVarosokLakossaga()}')

terseg = input('7. Feladat: kérem az ország nevét: ').upper()
szereploterseg = orszagSzerepel(terseg)
if szereploterseg == False:
    print(f'\t{terseg}i város nem szerepel a listában! ')
else: 
    print(f'\t{terseg}i város szerepel a listában!')