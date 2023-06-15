import random
print('Milyen műveletet szeretne gyakorolni?')
print('1. Összeadás')
print('2. Kivonás')
print('3. Szorzás')
valasz = int(input('Választás (1-3): '))
ok = 0
db = 0
d = 0
while ok != 5:
    db += 1
    a = random.randint(1,10)
    b = random.randint(1,10)
    if valasz == 1:
        print(a + b)
        d = a + b
    elif valasz == 2:
        print(a - b)
        d = a - b
    elif valasz == 3:
        print(a * b)
        d = a * b
    c = int(input('Adja meg a választ: '))
    if d == c:
        ok += 1
        print('Helyes!')
    else:
        print(f'Hibás!')

print(f'Gratulálunk! \n Sikerült 5 helyes műveletet elvégezni a {db} próbálkoásból!')      