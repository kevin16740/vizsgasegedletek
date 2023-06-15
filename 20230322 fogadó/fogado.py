from fogadoOra import FogadoOra

fogadoorak:list[FogadoOra]=[]
f = open('fogado.txt','r',encoding='utf-8')
for row in f:
    fogadoorak.append(FogadoOra(row))
f.close()

print(f'2. feladat: \n\tFoglalások száma: {len(fogadoorak)}')

nev = input('Adjon meg egy nevet: ')
count = 0
for i in fogadoorak:
    if i.nev == nev:
        count += 1

if count > 0:
    print(f'{nev} néven {count} időpontfoglalás van.')
elif count == 0:
    print('A megadott néven nincs időpontfoglalás.')
    
lista = []
idopont = input('Adjon meg egy érvényes időpontot (pl. 17:10): ')
for i in fogadoorak:
    if i.idopont == idopont:
        lista.append(i.nev)
lista.sort()

filename = idopont.replace(':','') + '.txt'
f = open(filename,'w',encoding='utf-8')
for i in lista:
        f.write(f'{i}\n')
        print(i)

f.close()

print('5. feladat:')
max = ''
for i in fogadoorak:
    if max < i.fogalalasiIdo:
        max = i.fogalalasiIdo
print(f'\tTanár neve: {i.nev}\n\tFoglalt időpont:{i.idopont}\n\tFoglalás ideje:{i.fogalalasiIdo}')

