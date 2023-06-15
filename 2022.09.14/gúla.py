def gulaTerfogat(aOldal, magassag):
    return aOldal * aOldal * magassag / 3
def gulaFelszin(aOldal, magassag):
    cOldal = pow(aOldal/2, 2) * pow(magassag, 2)
    palast = (cOldal * aOldal) / 2
    return palast * 4