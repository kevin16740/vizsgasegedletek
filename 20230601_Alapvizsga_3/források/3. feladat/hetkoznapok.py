napok = ['hetfő','kedd','szerda','csütörtök','péntek']

def maganhangzo(nap):
    betuk = 'aáeéiíoóöőuúüű'
    darab = 0
    for i in nap:
        if i in betuk:
            darab += 1
    return darab

max = napok[0]
for i in napok:
    if maganhangzo(max) < maganhangzo(i):
        max = i




print(f'A legtöbb magánhangzó a {max}-ben van')