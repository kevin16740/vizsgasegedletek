from fileinput import close


varosok = []


f = open('varosok.csv','r',encoding='utf8')

print(f.readline())
for row in f:
    varosok.append(row.strip())
f.close()

print(varosok)
print(f'A városok száma: {len(varosok)}')


ujVaros = 'Msikolc;Magyarország;211123\n'
f = open('varosok.csv','a', encoding='utf8')
f.write(ujVaros)
f.close()

#Hozzon létre egy orszagok.csv nevű fájlt, benne az összes országgal(minden ország 1-szer)


f = open('orszagok.csv','w',encoding='utf8')
# w - orásra nyitja meg a fájlt, ami benn van azt kitörli
# ha nem létezik a fájl, akkor létrehozza
for sor in varosok:
    adatok = sor.split(';')
    f.write(adatok[1]+'\n')
f.close()


orszagok = []
for sor in varosok:
    adatok = sor.split(';')
    if adatok[1] not in orszagok:
        orszagok.append(adatok[1])
orszagok.sort()
print(orszagok)

f = open('orszagok.csv','w',encoding='utf8')
for orszag in orszagok:
    f.write(orszag+'\n')
f.close()


# f = open('orszagok.csv','w',encoding='utf8')
# f.writelines(orszagok)
# f.close()