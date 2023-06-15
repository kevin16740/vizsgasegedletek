from kocka import terfogat
from kocka import felszin
from tegla import teglaFelszin
from tegla import teglaTerfogat
from gömb import gombTerfogat, gombFelszin
from gúla import gulaTerfogat, gulaFelszin
from menu import felszinVagyTerfogat, foMenu, teglatestfelszinVagyTerfogat, gömbFelszinVagyTerfogat, gulaFelszinVagyTerfogat

valasz = foMenu()
if valasz == 'A':
    print('Téglatest felszín/térfogat számítás')
    aaOldal = int(input('A oldal: '))
    bbOldal = int(input('B oldal: '))
    ccOldal = int(input('B oldal: '))
    if teglatestfelszinVagyTerfogat() == 'A':
        print(f'A téglatest felszíne = {teglaFelszin(aaOldal, bbOldal)}')
    else: 
        print(f'A téglatest térfogata = {teglaTerfogat(aaOldal, bbOldal, ccOldal)}')
elif valasz == 'B':
    print('Gömb felszín/térfogat számítás')
    sugar = int(input('sugár: '))
    if gömbFelszinVagyTerfogat() == 'A':
        print(f'A gömb felszíne = {gombFelszin(sugar)}')
    else: 
        print(f'A gömb térfogata = {gombTerfogat(sugar)}')
elif valasz == 'C':
    print('Gúla felszín/térfogat számítás')
    aOldal = int(input('A gúla alapjának oldala: '))
    magassag = int(input('A gúla magassága: '))
    if gulaFelszinVagyTerfogat():
        print(f'A gúla felszíne: {gulaFelszin(magassag, aOldal)}')
    else:
        print(f'A gúla térfogata: {gulaTerfogat(magassag, aOldal)}')
elif valasz == 'D':
    print('Kúp felszín/térfogat számítás')
elif valasz == 'E':
    print('Kocka felszín/térfogat számítás')
    aOldal = int(input('A oldal: '))
    if felszinVagyTerfogat() == 'A':
        print(f'A kocka felszíne = {felszin(aOldal)}')
    else: 
        print(f'A kocka felszíne = {terfogat(aOldal)}')