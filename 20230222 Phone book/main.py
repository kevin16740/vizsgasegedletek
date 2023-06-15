from User import User

users : list[User] = []

file = open('phone_book.txt','r',encoding='utf-8')
file.readline()
for row in file:
    users.append(User(row.strip()))
file.close()


print(f'2. feladat.: A telefonkönyvben {len(users)} dolgozó szerepel.')

for item in users:  
    if '.hu' == item.email[-3:]:
        print('3. Feladat.: Van magyar e-mail')
        break
else:
    print('3. Feldat.: Nincs magyar e-mail!')

nev = input('4. Feladat.: Adja meg a nevet: ')
for item in users:
    if nev == item.name:
        print(f'E-mail címe: {item.email} \t telefonszáma: {item.phone} \t Osztály: {item.job_title}')
        break
else:
    print('Nincs ilyen dolgozó!')

area = int(input('5. Feladat: Kérek egy körzetszámot: '))

def keres(area):
    for item in users:
        if item.area == area:
            print(f'\tDolgozó neve: {item.name} \tBeosztása: {item.job_title}')
    return False

keres(area)
if keres(area) == False:
    print('\tNincs ilyen körzet!')

stat = {}

for item in users:
    if item.department in stat.keys():
        stat[item.department] += 1
    else:
        stat[item.department] = 1

print(f'6. Feladat.: 30 fő feletti osztályok dolgozói:')
for key,value in stat.items():
    if value > 30:
        print(f'\t {key} : {value} fő')

for key,value in stat.items():
    print(f'{key}')

file = open('managers.txt','w',encoding='utf-8')
for item in users:
    if 'manager' in item.job_title:
        file.write(f'{item.name};{item.email}\n')
file.close()