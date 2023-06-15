from eloadas import Eloadas
from math import floor
eloadasok:list[Eloadas]=[]

f = open('eloadasok.txt','r',encoding='utf-8')
for row in f:
    eloadasok.append(Eloadas(row))
f.close()

stat = {}

for item in eloadasok:
    if item.nap in stat.keys():
        stat[item.nap] += item.hossz
    else:
        stat[item.nap] = item.hossz
nap = 0
for key,value in stat.items():
    nap += 1
    print(f'{nap} nap: {floor(value/60)} óra {value%60} perc')

max = 0
for i in eloadasok:
    if i.nap == 6:
        if i.hossz > max:
            max = i.hossz
            nev = i.nev
            hossz = i.hossz
print(f'Név: {nev}  \nidő: {hossz} perc')

for item in eloadasok:
    if item.nap in stat.keys():
        stat[item.nap] += item.hossz + 20
    else:
        stat[item.nap] = item.hossz + 20

for key,value in stat.items():
    print(f'November {key}.: {8 + int((value-20)/60)} óra {(value-20)%60} perc')

count = 0
nev = input('Adja meg az előadó nevét! ')
for i in eloadasok:
    if nev == i.nev:
        count += 1
if count > 0:
    print(count)
else:
    print('Nincs ilyen')

count = 0
for i in eloadasok:
    if 'mikrofon' in i.eszkoz :
        count += 1
print(count)