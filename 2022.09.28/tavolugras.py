from resultsFile import results




def getNames():
    names = []
    for row in results:
       data = row.split(';')
       names.append(data[1])
    return names 

def getCountries():
    countries = []
    for row in results:
        data = row.split(';')
        countries.append(data[2])
    return countries


#Egy embernek adjuk vissaz az összes ugrását!
def getJumps(name):
    for row in results:
        data = row.split(';')
        if data[1] == name:
            return data[3:7]
    return []

# Kérjük be egy versenyző nevét, indult-e a versenyen?

def searchName(name):
    for singLename in getNames():
        if name == singLename:
            return True  
    return False

def bestJump(jumps):
    best = -1
    for jump in jumps:
        if jump != '' and jump != 'x':
            jumpNumber = float(jump.replace(',','.'))
            if jumpNumber > best:
                best = jumpNumber
    return best


inputName = input('Íjra be a résztvevő nevét: ')
if searchName(inputName):
    print('A versenyző indult a versenyen!')
    print(f'A versenyző ugrásai: {getJumps(inputName)}')
    print(f'A legjobb ugrása: {bestJump(getJumps(inputName))}')
else:
    print('A versenyző nem indult a versenyen!')
