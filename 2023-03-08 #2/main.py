from versenyzo import Player

players:list[Player]= []
f = open('fob2016.txt','r',encoding='utf-8')
for i in f:
    players.append(Player(i))
f.close()



print(f'3. feladat: versenyzők száma: {len(players)}')



no = 0
for i in players:
    if i.category == 'Noi':
        no += 1
print(f'4. feladat: Női versenyzők aránya: {round((no/len(players) * 100),2)}%')



winnerWomen = ''
winnerWomenPoints = -1
for item in players:
    if item.totalPoints() > winnerWomenPoints:
        winnerWomenPoints = item.totalPoints()
        winnerWomen = item
print('6. feladat: A bajnok női versenyző')
print(f'\tNév: {winnerWomen.name}')
print(f'\tEgyesület: {winnerWomen.club}')
print(f'\tÖsszpont: {winnerWomen.totalPoints()}')



f = open('összpontFF.txt','w',encoding='utf-8')
for item in players:
    if item.category == 'Felnott ferfi':
        f.write(f'{item.name};{item.totalPoints()}\n')
f.close()



print('8. Feladat: Egyesület statisztika:')
stat= {}
for item in players:
    if item.club in stat.keys():
        stat[item.club] += 1
    else:
        stat[item.club] = 1

for key,value in stat.items():
    if value > 2 and key != 'n.a.':
        print(f'\t{key}: {value}fő')