
from filmalap import oraperc

for i in range(0,3):
    v = input('Adja meg egy film címét! ')
    ido = int(input('Hány perces a film? '))
    print(f'A(z) {v} című film {oraperc(ido)} hosszú' )