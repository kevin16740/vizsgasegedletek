from utas import Utas

gepek:list[Utas] = []
f = open('utasszallitok.txt','r',encoding='utf-8')
f.readline()
for row in f:
    gepek.append(Utas(row.strip()))
f.close()

print(f'4.Feladat: {len(gepek)} gép van')

count = 0
for i in gepek:
    if 'Boeing' in i.tipus:
        count += 1
print(f'5.Feladat: {count}-t gyártot')

max = gepek[0]
for i in gepek:
    if i.utasSzam > max.utasSzam:
        max = i

print('6. Feladat: A legtöbb utast szállító repülőgéptípus:')
print(f'\tTípus: {max.tipus}\n\tElső felszállás: {max.ev}\n\tUtasok száma: {max.utas}\n\tSzemélyzet: {max.szemelyzet}\n\tUtazósebesség {max.utazosebesseg}')

f = open('utasszallitok.new.txt','w',encoding='utf-8')
f.write('típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv\n')
for i in gepek:
    f.write(f'{i.tipus};{i.ev};{i.utasSzam};{i.szemSzam};{i.utazosebesseg};{round(i.tomeg/1000)};{round(i.fesztav*3.2808)}\n')
f.close()

stat = {}
for i in gepek:
    if i.ev in stat.keys():
        stat[i.ev] += 1
    else:
        stat[i.ev] = 1
print('Statisztika')
for key,value in stat.items():
    print(f'{key}: {value} db')