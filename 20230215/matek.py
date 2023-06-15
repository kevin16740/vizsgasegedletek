def keres(muvelet, muveletiJel):
    for index,item in enumerate(muvelet):
        if item == muveletiJel:
            return index
    return False

def muveletek(muvelet):
    eredmeny = 0
    muvelet = muvelet.replace(' ','')
    muveletijelHelye = keres(muvelet,"+")
    if muveletijelHelye != False:
        x = float(muvelet[0:muveletijelHelye])
        y = float(muvelet[muveletijelHelye+1:])
        eredmeny = x+y
        return eredmeny
    muveletijelHelye = keres(muvelet,"-")
    if muveletijelHelye != False:
        x = float(muvelet[0:muveletijelHelye])
        y = float(muvelet[muveletijelHelye+1:])
        eredmeny = x-y
        return eredmeny
    muveletijelHelye = keres(muvelet,"*")
    if muveletijelHelye != False:
        x = float(muvelet[0:muveletijelHelye])
        y = float(muvelet[muveletijelHelye+1:])
        eredmeny = x*y
        return eredmeny
    muveletijelHelye = keres(muvelet,"/")
    if muveletijelHelye != False:
        x = float(muvelet[0:muveletijelHelye])
        y = float(muvelet[muveletijelHelye+1:])
        eredmeny = x/y
        return eredmeny


muvelet = input('Adja meg a műveletet: ')
print(f'{muvelet} = {muveletek(muvelet)}')    
