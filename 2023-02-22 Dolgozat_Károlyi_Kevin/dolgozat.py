maxPontszam = int(input('Mennyi a dolgozat maximális pontszáma: '))
tanSzam = 0
for i in range(3):
    tanSzam += 1
    print(f'A (z) {tanSzam}. tanuló:')
    nev = input('\tNeve: ')
    Pontszam = int(input('\tPontszáma: '))
    print(f'\t{nev} osztályzata: {osztalyzas(Pontszam,maxPontszam)}')

osztalyzat = ''
def osztalyzas(Pontszam,maxPontszam):
    if Pontszam / maxPontszam * 100 < 39.9:
        osztalyzat = 'elégtelen (1)'
    if Pontszam / maxPontszam * 100 > 40 and Pontszam / maxPontszam * 100 < 54.9:
        osztalyzat = 'elégséges (2)'
    if Pontszam / maxPontszam * 100 > 55 and Pontszam / maxPontszam * 100 < 69.9:
        osztalyzat = 'közepes (3)'
    if Pontszam / maxPontszam * 100 > 70 and Pontszam / maxPontszam * 100 < 84.9:
        osztalyzat = 'jó (4)'
    if Pontszam / maxPontszam * 100 > 85 and Pontszam / maxPontszam * 100 <= 100:
        osztalyzat = 'jeles (5)'    