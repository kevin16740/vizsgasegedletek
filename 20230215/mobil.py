
def szamEll(szam:str):
    szam = szam.replace(' ','')
    szam = szam.replace('-','')
    if szam[0] == '+':
        szam = szam.replace('+','')
    if szam[0:4] == '0036':
        szam = szam.replace('0036','06')
    if szam[0:2] != '06' or szam[0:2] != '00': 
        return False
    if szam[2:4] != '20' and szam[2:4] != '30' and szam[2:4] != 70 and szam[2:4] != 50 and szam[2:4] != 31:
        return False
    if len(szam) != 11:
        return False
    return True

szam = input('Adja meg a telefonszámot! ')

if szamEll(szam) == True:
    print('Helyes!')
else:
    print('Helytelen!')