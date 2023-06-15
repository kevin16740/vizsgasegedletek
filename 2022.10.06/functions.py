from data import telepulesek

def telepulesekSzama():
    return len(telepulesek)


#összegzés
def osszesLakos():
    lakossag = 0
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        lakossag += int(telepulesAdatok[4])
    return lakossag


#minimum kiválasztás
def legkisebb():
    elso = telepulesek[0].split(';')
    minMeret = int(elso[3])
    minNev = elso[0]
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        if minMeret > int(telepulesAdatok[3]):
            minMeret = int(telepulesAdatok[3])
            minNev = telepulesAdatok[0]

    return minNev

def nagyKozseg():
    kozseg = 0
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        if telepulesAdatok[1] == 'nagyközség':
            kozseg += 1
    return kozseg

def telepulesTersege(keresettTelepules):
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        if telepulesAdatok[0] == keresettTelepules:
            return telepulesAdatok[2]
    return False

def nagyHektar():
    hektar = 0
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        if telepulesAdatok[2] == 'Záhonyi'  and int(telepulesAdatok[3]) > 1500:
            hektar += 1
    return hektar

# Melyik községben laknak a legtöbben?
def legnagyobb():
    maxLakos = 0
    maxNev = ''
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        if maxLakos < int(telepulesAdatok[4]) and telepulesAdatok[1] == 'község':
            maxLakos = int(telepulesAdatok[4])
            maxNev = telepulesAdatok[0]

    return maxNev
