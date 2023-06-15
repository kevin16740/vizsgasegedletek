from functions import *
from functions import telepulesekSzama
from functions import osszesLakos
from functions import legkisebb
from functions import nagyKozseg
from functions import nagyHektar

print(f'Települések száma: {telepulesekSzama()} db')


# Határozza meg és írja ki a képernyőre Szabolcs-Szatmár-Bereg megye lakosságát!


print(f'A megye lakossága: {osszesLakos()} fő')


#Keresse meg és írja ki a képernyőre a legkisebb lakosságú település nevét!

print(f'A legkisebb település: {legkisebb()}')


#Határozza meg és írja ki, hogy nagyközségből hány található a megyében!

print(f'A megyében a nagyközségek száma: {nagyKozseg()} nagyközség')



#Kérjük be egy település nevét és határozzuk meg, hogy melyik térségben van! 

telepules = input('Település neve: ')
terseg = telepulesTersege(telepules)
if terseg == False:
    print('Nincs ilyen nevű település')
else:
    print(f'A megadott {telepules} a {terseg} térségben található')

# Határozzuk meg, hogy a Záhonyi térségben hány db 1500ha feletti település található!
print(f'{nagyHektar()} db 1500ha feletti település található!')

print(f'{legnagyobb()} községben laknak a legtöbben')