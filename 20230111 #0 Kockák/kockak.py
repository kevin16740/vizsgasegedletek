import random

n = int(input('Hány alkalommal legyen feldobás? '))
pdb = 0
adb = 0
for i in range(n):
    dobas = random.randint(1,6)
    dobas2 = random.randint(1,6)
    dobas3 = random.randint(1,6)
    if (dobas + dobas2 + dobas3) < 10:
        nyertes = 'Anni'
        adb += 1
    elif (dobas + dobas2 + dobas3) > 10:
        nyertes = 'Panni'
        pdb += 1
    print(dobas, '+', dobas2, '+', dobas3, 'Nyert:', nyertes)
print(f'A játék során {adb} alkalommal Anni, {pdb} alkalommal Panni nyert.')
