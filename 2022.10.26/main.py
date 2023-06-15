from menu import menu 
from functions import * 
from functions import updateByIndex
load()

choice = -1
while choice != 0:
    choice = menu()
    if choice == 1:
        listAll()
    elif choice == 2:
        name = input('Kérem a keresett nevet: ')
        result = search(name)
        if len(result) == 0:
           print('Nincs ilyen ember')
        else:
            for item in result:
                print(f'\t{item}')
    elif choice == 3:
        reginev = input('Kérem a nevet: ')
        name = input('Kérem a nevet: ')
        new(name, reginev)
    elif choice == 4:
        name = input('Kérem a törlendő nevet: ')
        delete(name)
    # elif choice == 5:
    #     nev = input('Kérem a régi nevet: ')
    #     if len(search(nev)) == 0:
    #         print('Nincs ilyen ember!')
    #     elif len(search(nev)) > 1:
    #         print('Túl sok találat van!')
    #     else:
    #         newName = input('Kérem az új nevet: ')
    #     update(nev, newName)
    elif choice == 5:
        nev = input('Kérem a régi nevet: ')
        results = searchWithIndex(nev)
        if len(results) == 0:
            print('Nincs találat!')
        else:
            for index in results:
                print(f'\tMelyik {index} - {names[index]} ')
            userIndex = input('Adja meg a választott ember sorszámát: ')
            if userIndex not in results:
                print('Nincs ilyen sorszám!')
            else: 
                newName = input('Kérem az új nevet: ')
                updateByIndex(index, newName)




        '''
        TODO: azonos nevű embereket lekell kezelni!
        
        '''

