from fileHandling import loadData
from search import searchByName, searchByName2, searchUnder

results = loadData()

#print(len(results))
#print(f'Első vizsgázó: {results[0].name}')
#print(f'Első vizsgázó ideje: {results[0].time}')

name = input('Tanuló neve: ')
index = searchByName(results, name)
print(f'{results[index].name} eredménye {result[index].module} modulból: {results[index].result} pont, {result[index].time} idő alatt.')

found = searchByName2(results, name)
print(f'{found.name} eredménye {found.module} modulból: {found.result} pont, {found.time} idő alatt.')

failed = searchUnder(results, 50)
print('Bukottak listája: ')
for item in failed:
    print(f'\t{item.name}')