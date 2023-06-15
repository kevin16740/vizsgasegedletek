def menu():
    option = -1
    while option <0 or option > 5:
        print('--------------------------')
        print('0 - Kiépés')
        print('1 - Listázás')
        print('2 - Keresés')
        print('3 - Új')
        print('4 - Törlés')
        print('5 - Módosítás')
        print('--------------------------')
        option = int(input('Válasszon a fentiek közül: '))
    return option