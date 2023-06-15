from autok import autok
def searchPlate(plate):
    for car in autok:
        splittedData = car.split(';')
        if splittedData[0] == plate:
            return True
    return False

def totalPrice():
    sum = 0
    for car in autok:
        totalprice = car.split(';')
        sum += int(totalprice[4])
    return sum

def averageAge():
    sum = 0
    for car in autok:
        averageage = car.split(';')
        sum += int(averageage[2])
    return 2022 - sum / 58

def countBrand(brand):
    count = 0
    for car in autok:
        splittedData = car.split(';')
        if splittedData[1].upper() == brand.upper():
            count += 1
    return count

def highestPower():
    best = 0
    for car in autok: 
        splittedData = car.split(';')
        power = int(splittedData[6])
        if power > best:
            best = power
    return best

def lowestConsumption():
    lower = 200
    for car in autok: 
        splittedData = car.split(';')
        Esz = float(splittedData[8])
        if Esz < lower:
            lower = Esz
    return lower