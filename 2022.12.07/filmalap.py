import math


def oraperc(ido): #Egészítse ki a függvénydefiníciót paraméterrel!
    ora = math.floor(ido / 60)
    perc = ido - ora * 60
    return  str(ora) + ' óra ' + str(perc) + ' perc' 