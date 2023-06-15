from fuvarok import Fuvar

fuvarok :list[Fuvar] = []

file= open('fuvar.csv','r',encoding='utf-8')
file.readline()
for row in file:
    fuvarok.append(Fuvar(row.strip()))
file.close()

print(f'3. feladat: {len(fuvarok)} fuvar')

fuvarSzam = 0
bevetel = 0

for i in fuvarok:
    if i.taxi_id == 6185:
        fuvarSzam += 1
        bevetel += (i.viteldij + i.borravalo)

print(f'4. feladat: {fuvarSzam} fuvar alatt: {round(bevetel,2)}$')

stat={}

for item in fuvarok:
    if item.fizetes_modja  in stat.keys():
        stat[item.fizetes_modja] += 1
    else:
        stat[item.fizetes_modja] = 1

print('5. feladat:')
x = []
for key,value in stat.items():
    print(f'\t{key}: {value} fuvar')