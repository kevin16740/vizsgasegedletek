felhasznaloNev = input('Adja meg felhasználónevét! ')
jelszo = input('Adja meg jelszavát! ')
jelsz = 'Szivecske99'
felhaszn= 'bori99'
while felhasznaloNev == felhaszn or jelszo == jelsz:
    print('Sikertelen bejelentkezés!')
    felhasznaloNev = input('Adja meg felhasználónevét! ')
    jelszo = input('Adja meg jelszavát! ')
print('Sikeres bejelentkezés!')