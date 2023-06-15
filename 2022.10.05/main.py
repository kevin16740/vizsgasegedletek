from functions import *

print(f'A versenyen {countCompetitors()} versenyző indult.')
paraLellBarsWinner = winner('Korlát')
print(f'Kroláton a győztes: {paraLellBarsWinner}')
jumpWinner = winner('Ugrás')
print (f'Ugrásban győztes: {jumpWinner}')


startNumber = (input('Írja a versenyző rajtszámát:'))
ringResultes = ringResult(startNumber)
if ringResult == False:
    print('Nincs ilyen számű versenyző')
else:
    print(f'A versenyző gyűrűn elért eredménye: {ringResultes}')

print(f'Lólengésben kiesett {countLessThenPomelHorse(14.5)} fő')


print('Földrészek amelyeken versenyzők indultak: ')
print(Regions())

printCountCompetitorsOfCountries()