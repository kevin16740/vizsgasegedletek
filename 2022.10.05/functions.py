from data import results

def countCompetitors():
    return len(results)

def typeStringToNumber(type):
    #'Talaj' -> 4
    #'Lólengés' -> 5
    if type == 'Talaj':
        return 4 
    elif type == 'Lólengés':
        return 5
    elif type == 'Gyűrű':
        return 6
    elif type == 'Nyújtó':
        return 7
    elif type == 'Korlát':
        return 8
    elif type == 'Ugrás':
        return 9
    return False



#maximumkiválasztás
def winner(competitionNumber):
    typeNumber = typeStringToNumber(competitionNumber)
    maxPoint = 0
    WinnerName = ''
    for result in results:
        resultlist = result.split(';')
        Point = float(resultlist[typeNumber].replace(',','.'))
        if Point > maxPoint:
            maxPoint = Point
            WinnerName = resultlist[1]
    return WinnerName

#rajtszám bekérés, majd írja ki a képernyőre az adott versenyző gyűrűn elért eredményét!

def ringResult(startNumber):
    for result in results:
        resultlist = result.split(';')
        if resultlist[0] == startNumber:
            return resultlist[6]
    return False

def countLessThenPomelHorse(limit):
    count = 0
    for result in results:
        resultlist = result.split(';')
        if limit > float(resultlist[5].replace(',','.')):
            count += 1
    return count
    


def Regions():
    regionList = []
    for result in results:
        resultList = result.split(';')
        if resultList[3] not in regionList:
            regionList.append(resultList[3]) 
        regionList.sort()
    return regionList

def printCountCompetitorsOfCountries():
    countries = []
    for result in results:
        resultList = result.split(';')
        if resultList[2] not in countries:
            countries.append(resultList[2]) 
    for country in countries:
        count = 0
        for result in results:
            resultList = result.split(';')
            if resultList[2] == country:
                count += 1
        print(f'{country}: {count} fő')

