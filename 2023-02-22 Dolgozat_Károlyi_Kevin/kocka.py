import random
anniNyeres = 0
panniNyeres = 0
n = int(input('Hány alkalommal legyen feldobás? '))
for i in range(n):
    kocka1 = random.randint(1,6)
    kocka2 = random.randint(1,6)
    kocka3 = random.randint(1,6)
    dobas = kocka1 + kocka2 + kocka3
    nyertes = ''

    if dobas < 10:
        anniNyeres += 1
        nyertes = 'Anni'
    else:
        panniNyeres += 1
        nyertes = 'Panni'
    print(f'Dobás: {kocka1} + {kocka2} + {kocka3} = {dobas}\tNyert: {nyertes}')
print(f'A játék során {anniNyeres} alkalommal Anni, {panniNyeres} alkalommal Panni nyert.')