#felelő sorsoló alkalmazás
#Véletlenszerűen válasszunk ki egy nevet a listából
#Kérdezzük meg, legyen-e újabb felelő, 
#aki már felelt, az ne legyen újra
from random import randint


nevsor = [
    'Ackermann Roland',
    'Blümmel Zétény',
    'Csizmazia Máté',
    'Deli Ádám',
    'Fábry Kevin',
    'Harczi Gergő',
    'Hegedüs Márk',
    'Holper Júlia',
    'Káldi Martin',
    'Károlyi Kevin',
    'Király Ágoston',
    'Kiss Bálint Simon',
    'Kocsis Bálint',
    'Kovács Máté Miklós',
    'Vámosi Attila',
    'Váradi Dávid'
]

def sorsol():
    return randint(0,len(nevsor) - 1 )


tovabb = 'i'
while len(nevsor) != 0 and  tovabb == 'i':
    felelo = nevsor[sorsol()]
    print(f'A mai felelő: {felelo}')
    nevsor.remove(felelo)
    tovabb = input('Legyen újabb felelő? (i/n)')
    