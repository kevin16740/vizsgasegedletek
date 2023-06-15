from meccs import Meccs

meccsek:list[Meccs]=[]

f = open('toto.txt','r',encoding='utf-8')
f.readline()
for row in f:
    meccsek.append(Meccs(row.strip()))
f.close()

print(f'3.2 feladat: Fogadási fordulók száma: {len(meccsek)}')


db = 0
for i in meccsek:
    db += i.T13p1
print(f'3.3 feladat: telitalálatos szerelvények száma: {db} db')

for i in meccsek:
    if 'X' in i.eredmenyek:
        print(f'3.4 feladat: Volt döntetlen mentes forduló!')
        break
else:
    print(f'3.4 feladat: Nem volt döntetlen mentes forduló!')