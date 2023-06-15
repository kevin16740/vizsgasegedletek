from data import *

def nevreKeres():
    for result in results:
        n = input('Kérem a keresett nevet: ')
        splittedData = result.split(';')
        if splittedData[0] == n:
            return True
    return False