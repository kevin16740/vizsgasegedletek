from Legnepesebb import results

def varosokSzama():
    return len(results)

def megfeleltVaros():
    megfeleltVarosok = 0
    for result in results:
        splittedData = result.split(';')
        if int(splittedData[2]) >= 10000000:
            megfeleltVarosok += 1
    return megfeleltVarosok

def legnepesebbVaros():
    lvarosNev = ''
    LvarosOrszag = ''
    LvarosSzam = 0
    for result in results:
        splittedData = result.split(';')
        if int(splittedData[2]) > LvarosSzam:
            LvarosSzam = int(splittedData[2])
            lvarosNev = splittedData[0]
            LvarosOrszag = splittedData[1]
    print(f'5. Feladat: A legnépesebb város: \n Neve: {lvarosNev} \n Ország: {LvarosOrszag} \n Lakosság: {LvarosSzam} fő')

def kinaiVarosokLakossaga():
    megfeleltVarosokLakossag = 0
    for result in results:
        splittedData = result.split(';')
        if splittedData[1] == 'Kína':
            megfeleltVarosokLakossag += int(splittedData[2])
    return megfeleltVarosokLakossag

def kinaiVarosok():
    max = 0
    for result in results:
        splittedData = result.split(';')
        if splittedData[1] == 'Kína' and int(splittedData[2]) > max:
            max = int(splittedData[2])
            kesz = len(splittedData[0])
    return kesz

def orszagSzerepel(terseg):
    for result in results:
        splittedData = result.split(';')
        if terseg == splittedData[1].upper():
            return True
    return False
