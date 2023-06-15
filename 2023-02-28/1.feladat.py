import random
nev1 = input('Adja meg az egyik barát nevét! ')
nev2 = input('Adja meg a másik parát nevét! ')
dobas1 = 0
dobas2 = 0
dobas3 = 0
dobas4 = 0
kor = 0
while dobas1 != 6 and dobas2 != 6 or dobas3 != 6 and dobas4 != 6:
    kor += 1
    dobas1 = random.randint(1,6)
    dobas2 = random.randint(1,6)
    dobas3 = random.randint(1,6)
    dobas4 = random.randint(1,6)
    print(f'{kor} kör:')
    print(f'\t{nev1} dobása: {dobas1} + {dobas2}')
    print(f'\t{nev2} dobása: {dobas3} + {dobas4}')
if dobas1 == 6 and dobas2 == 6:
    print(f'A játékot {nev1} kezdi')
elif  dobas3 == 6 and dobas4 == 6:
    print(f'A játékot {nev2} kezdi')