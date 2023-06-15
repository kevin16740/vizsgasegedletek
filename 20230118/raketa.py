kezdo = int(input('Hány órás visszaszámlálást tervezünk? '))
print(f'Visszaszámlálás: {kezdo}')
nem = 0
marad = kezdo
if kezdo > 1:
    for i in range(kezdo):
        v = input('Fel kell függeszteni a visszaszámlálást (i/n)? ')
        if v == 'n':
            marad -= 1
            print(f'Visszaszámlálás {marad}')

        elif v == 'i':
            marad -= 1
            print(f'Visszaszámlálás {marad}')
            nem += 1
print(f'A rakéta a visszaszámlálást követően ennyi idővel indult: {kezdo + nem}')