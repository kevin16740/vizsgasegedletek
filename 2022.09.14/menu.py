from distutils.command.install_egg_info import safe_name
from re import S
from this import d


def foMenu():
    valasz = ''
    while valasz != 'A' and valasz != 'B' and valasz != 'C'and valasz != 'D'and valasz != 'E' and valasz != 'X' :
        print('X - Kilépés')
        print('A - Téglatest')
        print('b - Gömb')
        print('C - Gúla')
        print('D - Kúp')
        print('E - Kocka')

        # valasz = input('Választás: ')
        valasz = input('Választás: ').upper()
    return valasz

def felszinVagyTerfogat():
    valasz = ''
    while valasz != 'A' and valasz != 'B':
        print('\nMit szeretne kiszámolni? ')
        print('\tA - Felszín')
        print('\tV- Térfogat')

        valasz = input('Választás: ').upper()
    return valasz

def teglatestfelszinVagyTerfogat():
    valasz = ''
    while valasz != 'A' and valasz != 'V':
        print('\n Mit választana: ')
        print('\tA - téglatest felszíne')
        print('\tV - téglatest térfogata')

        valasz = input('Választása: ').upper()
def gömbFelszinVagyTerfogat():
    valasz = ''
    while valasz != 'A' and valasz != 'B':
        print('\n Mit szeretne kiszámolni?')
        print('\tA - Gömb felszíne')
        print('\tB - Gömb térfogata')

        valasz = input('Választás: ').upper()

def gulaFelszinVagyTerfogat():
    valasz = ''
    while valasz != 'A' and valasz != 'B':
        print('\n Mit szeretne kiszámolni?')
        print('\tA - Gúla felszíne')
        print('\tB - Gúla térfogata')

        valasz = input('Választás: ').upper()