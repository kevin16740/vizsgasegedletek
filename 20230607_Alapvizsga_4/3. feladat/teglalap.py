print('1- feladat: Téglalap kerülete és területe')
for i in range(10):
    print('Adja meg a téglalap oldalait!')
    try:
        a = float(input('a= '))
        b = float(input('b= '))

        print(f'T = {a*b}')
        print(f'K = {2*(a+b)}')
    except:
        print('Nem megfelelő adat!')