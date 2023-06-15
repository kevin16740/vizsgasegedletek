from data import *
from dunctions import nevreKeres

def name():
    for result in results:
       splittedData = result.split(';')
    return splittedData[0]


def module(row: str):
    splittedData = str.split(';')
    return splittedData[1]

def mdoule():
    for result in results:
       splittedData = result.split(';')
    return splittedData[1]

def minutes(row: str):
    splittedData = str.splitted(';')
    time = splittedData[2].split(':')
    return float(time[0]) + float(time[1]) / 60

print(f'Az állományban {len(results)} vizsgázó van!')

db = 0 

for result in results:
    splittedData = result.split(';')
    if float(splittedData[3]) >= 75:
        db += 1
print(f'{db} vizsgázó tett sikeres vizsgát!')
# perc = 0
# for result in results:
#     splittedData = result.split(';')
#     if splittedData[1] == 'Word':
#         perc += minutes(row)
    
# print(f'A Wordból vizsgázok átlagosan {perc}-t dolgoztak')

# minValue = percent(results[0])
# minIndex = 0
# for i in range(1,len(results)):
#     if minValue > percent(results[i]):
#         minValue = percent(results[i])
#         minIndex = i
# print(f'a legrosszab eredményt {name(results[minIndex])} érte el {minValue}%')

versenyzo = input('Nevet: ')
versenyzo = nevreKeres(versenyzo)
if nevreKeres():
    print('Volt ilyen nevű verseníző!')
else:
    print('Nincs ilyen versenyző!')