import random
lista = []
print('2. felasdat: Halmaz-e?')

def halmazE(lista):
    halmaz = []
    for item in lista:
        if item not in halmaz:
                halmaz.append(item)
    if len(lista) == len(halmaz):
         return True
    else:
         return False
        
for i in range(8):
    for j in range(5):
        lista.append(random.randint(0,9))
    if halmazE(lista) == True:
        print(f'{i+1}. {lista} -> Halmaznak tekinthető!')
    else:
        print(f'{i+1}. {lista} -> Halmaznak nem tekinthető!')
