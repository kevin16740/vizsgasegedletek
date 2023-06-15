from random import randint


def tippBeker():
    #1,2,x,X
    tipp= ''
    while tipp != '1' and tipp != '2' and tipp != 'X': 
        tipp = input('Kérem a tippet (1,2,x):  ').upper()
    return tipp 
tippek = []
hazai = []
vendeg = []
def osszesTippBeker():
    for i  in range(14):
       tippek.append(tippBeker())

def eredmenyGeneral():
    for i in range(14):
        hazai.append(randint(0,9))        
        vendeg.append(randint(0,9))

def golokbolEredmeny(hazaiGol,vendegGol):
        if hazaiGol > vendegGol:
            return '1'
        elif hazaiGol < vendegGol:
            return '2'
        elif hazaiGol == vendegGol:    
            return 'x'

def talaltE(tipp, hazaGol, vendegGol):
    return tipp == golokbolEredmeny(hazaGol,vendegGol)

def talalalatokSzama():
    talalatDarab = 0
    for i in range(14):
        if talaltE(tippek[i],hazai[i], vendeg[i]):
            talalatDarab += 1

            return talalatDarab
def kiir():
    for i in range(14):
        print(f'{tippek[i]}\t{hazai[i]}-{vendeg[i]}\t{golokbolEredmeny(hazai[i],vendeg[i])}')

def main():
    osszesTippBeker()
    eredmenyGeneral()
    print('Tipp\tGólkülönbség\tEredmény')
    kiir()
    print(f'Végeredmény: {talalalatokSzama()} darab találat.')
    
main()