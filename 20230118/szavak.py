szo1 = input('Adj meg egy szót! ')
szo2 = input('Adj meg egy szót! ')

if len(szo1) > len(szo2):
    print(f'A hosszabb szó: {szo1}')
elif len(szo1) == len(szo2):
    print(f'A két szó egyforma hosszú.')

else:
    print(f'A hosszabb szó: {szo2}')

