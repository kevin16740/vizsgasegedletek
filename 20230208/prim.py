def prim(szam):
    for i in range(2, szam):
        if szam % i == 0:
            return False
    return True
def legnagyobbPrim(szam):
    for i in range(szam,1, -1):
        if prim(i) == True:
            return i

szam = int(input('Szám: '))
print(legnagyobbPrim(szam))