from feltalalo import Feltalalo
feltalalokListaja = []
file = open('feltalalok.txt','r',encoding='utf-8')
for sor in file:
    f = Feltalalo(sor)
    feltalalokListaja.append(f)

file.close()   

print(f'2.feladat: A fajlban {len(feltalalokListaja)} tudós adata szerepel')
print(f'3. feladat: feltalálók-találmányok ')
for felt in feltalalokListaja:
    print(f'{felt.nev}->{felt.talalmany}')

kor = int(input('Kor megadása: '))

f = open('kiiras.txt','w',encoding = 'utf-8')
for felt in feltalalokListaja:
    if felt.halal - felt.szuletes > kor:
        print(felt.nev)
        f.write(felt.nev + '\n')

f.close()