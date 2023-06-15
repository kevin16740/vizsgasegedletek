data = []
def readFile():
    
    file = open('torna.csv','r',encoding='utf-8')

    elsosor = file.readline()
    
    for row in file: #beolvassa soronként a file tartalmát
        # print(row)
        data.append(row.strip())
    
    file.close()



def getContinents():
    contintnents = []
    for row in data:
        splitted = row.split(';')
        if splitted[3] not in contintnents:
            contintnents.append(splitted[3])
    return contintnents

def writeContinentsToFile(continents):
    file = open('continents.txt','w',encoding='utf-8')
    
    
    for continent in continents:
        file.write(f'{continent} + \n')       

    
    file.close()

def writeCompetitorsFromCountryToFile(countryCode):
    file = open(countryCode + '.txt','w',encoding='utf-8')
    for row in data:
        splitted = row.split(';')
        if splitted[2].upper() == countryCode.upper():
            file.write(splitted[1] + '\n')
    
    file.close()

def versenyzokPontszam():
    osszpontszam = 0
    file = open(osszpontszam + '.txt','w',encoding='utf-8')
    for row in data:
        splitted = row.split(';')
        osszpontszam = float(splitted[4].replace(',','.')) * float(splitted[5].replace(',','.')) + float(splitted[6].replace(',','.'))
    
        file.write(splitted[1] + ';' + str(osszpontszam)+ '\n')
    file.close()