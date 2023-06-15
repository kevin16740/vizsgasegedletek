from math import floor
from random import randint
ZARAS = 16 * 60 * 60 #eddig van nyitva a bolt 
MAX_PENZTAR = 5
MAX_VEVO_SZAM = 5
vevok = [] # mennyi ideje van a vevő a boltban 
penztarak = [] # hány vásárló van a pénztárakban

def allapotKiir(ido):
    pontosIdo = ido + 6 * 3600
    # round() - matek szabályok szerint kerekít (3,5-től felfele, alatta lefele)
    # floor() - mindig lefelé kerekít (3.7) -> 3
    #ceil() - mindig felfelé kerekít (3.1) -> 4
    ora = floor(pontosIdo / 3600)
    perc = floor((pontosIdo - ora * 3600) / 60)
    masodPerc = pontosIdo - ora * 3600 - perc * 60 
    print(f'Idő: {ora} óra {perc} perc {masodPerc} másodperc')
    print(f'Vevők száma: {len(vevok)}')
    print(f'Vevők: {vevok}')
    print(f'Pénztárak: {penztarak}')

def ujVevo(ido):
    if ido > ZARAS:
        print('Bezárt a bolt, nem mehet be új vevő.')
        return
    if len(vevok) >= MAX_VEVO_SZAM:
        print('Tele van a bolt')
        return 
    if  randint(0,1) == 0: #érkezik új vevő
            vevok.append(0)



def vevvokIdejeNovel():
    for i in range(len(vevok)):
        vevok[i] += 15


#def fizetes():
 #   for i in range(len(penztarak)):
  #      if penztarakIdeje[i] <= 15: #20% valószínűséggel szolgál ki vevőt
   #        if randint(0,99) < 20:
    #            pass            




def penztarNyit():
    # ha nincs egy olyan pénztár sem, ahol 3-nál kevesebben állnak, akkor nyisson ki 
    if len(penztarak) == MAX_PENZTAR:
        return
    for item in penztarak:
        if item < 3:
            return
    penztarak.append(0)

def penztarbolKimegy():
        #minél többen vnnak a pénztárban, annál nagyobb valószínűséggel megy ki onnan vki
    for i in range(len(penztarak)):
        if penztarak[i] > 5: # biztosan kimegy
            penztarak[i] -= 1            
        elif penztarak[i] > 4:
            if (randint(0,99) > 20):
                penztarak[i] -= 1
        elif penztarak[i] > 3:
            if (randint(0,99) > 40):
                penztarak[i] -= 1
        elif penztarak[i] > 2:
            if (randint(0,99) > 60):
                penztarak[i] -= 1
        elif penztarak[i] > 1:
            if (randint(0,99) > 70):
                penztarak[i] -= 1
        else:
            if (randint(0,99) > 80):
                penztarak[i] -= 1


def penztarBezar():
    for i in range(len(penztarak)-1, -1 , -1):
        if penztarak[i] == -1:
            del(penztarak[i])

def vevoPenztarbaMegy():
    for i in range(len(vevok)):
        if vevok[i] < 30:
            pass
        elif vevok[i] < 60: #20% valsz. meg a pénztárba
            if randint (0,99) < 20:
                # nyitott pénztárak közül random beáll az egyikbe
                penztarak[randint(0,len(penztarak) -  1)] += 1
            # del(vevok[i])
            vevok[i] = -1 #pénztárba megy
        elif vevok[i] < 120:
            if randint(0,99) < 40: # 40%
                penztarak[randint(0,len(penztarak) -  1)] += 1
            vevok[i] = -1
        elif vevok[i] < 180:
            if randint(0,99) < 60: # 60%
                penztarak[randint(0,len(penztarak) -  1)] += 1
            vevok[i] = -1
        elif vevok[i] < 240: # 80%
            if randint(0,99) < 80:
                penztarak[randint(0,len(penztarak) -  1)] += 1
            vevok[i] = -1
        else: #Midenképp menjen nyitáskor a pénztárhoz
                penztarak[randint(0,len(penztarak) -  1)] += 1
                vevok[i] = -1
    # a pénztárba menteket törölni kell
    ujvevok = []
    for item in vevok:
        if item != -1:
            ujvevok.append(item)
    # vevok = ujvevok
    vevok.clear()
    for item in ujvevok:
        vevok.append(item)

def main():
    ido = 0
    penztarak.append(0) # egy pénztár nyitásakor kinyit 
    while ido < ZARAS or len(vevok) > 0:
        
        ujVevo(ido)
        allapotKiir(ido)
        vevvokIdejeNovel()
        vevoPenztarbaMegy()
        penztarbolKimegy()
        penztarBezar()
        ido += 15
        input()
    print('Bezárt a bolt, nincs benne több vevő.')
main()



