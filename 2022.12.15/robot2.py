def countLetters(letter, word):
    counter = 0
    for character in word:
        if character == letter:
            counter += 1
    return counter


commandWord = input('Kérem a robot parancsait: ').upper()
eCount = countLetters("E",commandWord)
nCount = countLetters("N",commandWord)
dCount = countLetters("D",commandWord)
kCount = countLetters("K",commandWord)
print(f'E betűk száma: {eCount}')
print(f'N betűk száma: {nCount}')
print(f'D betűk száma: {dCount}')
print(f'K betűk száma: {kCount}')

if nCount > kCount:
    nCount -= kCount
    kCount = 0
else: 
    kCount -= nCount
    nCount = 0

if eCount > dCount:
    eCount -= dCount
    dCount = 0
else: 
    dCount -= eCount
    eCount = 0

print(f'Egy legrövidebb út parancsa: {nCount * "N"}{dCount * "D"}{kCount * "K"}{eCount * "E"}')