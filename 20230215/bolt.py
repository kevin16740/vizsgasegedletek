def bolt(rezsi, ber, forgalom, atlagoshaszon):
   marad = forgalom*atlagoshaszon/100
   marad -= ber
   marad -= rezsi
   return marad

rezsi = int(input('Adja meg a havi rezsit! '))
ber = int(input('Adja meg a bérköltséget! '))
forgalom = int(input('Adjam meg a forgalmat! '))
atlagoshaszon = int(input('Adja meg mennyi százalék az átlagos haszon! '))


print(marad, 'Ft,- marad')

if marad <= 0:
    print('Zárja be a boltot!')
else:
    print('Tartson nyitva!')