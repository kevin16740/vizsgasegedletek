commandWord = input('Kérem a robot parancsait: ').upper()
eCount = 0
nCount = 0
dCount = 0
kCount = 0


for leater in commandWord:
    if leater == 'E':
        eCount += 1
    elif leater == 'N':
        nCount += 1
    elif leater == 'D':
        dCount += 1
    else:
        kCount += 1



print(f'E betűk száma: {eCount}')
print(f'N betűk száma: {nCount}')
print(f'D betűk száma: {dCount}')
print(f'K betűk száma: {kCount}')

