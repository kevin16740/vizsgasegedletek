
def szokoev(evszam):
    if evszam % 400 == 0:
        return True
    if evszam % 4 == 0 and evszam % 100 != 0:
        return True
    return False
szokoevek = []
evszam1 =int(input('Kérem az egyik gépszámot: ')) 
evszam2 = int(input('Kérem a másik évszámot: '))

for ev in range(evszam1, evszam2+1):
    if szokoev(ev):
        szokoevek.append(ev)
if len(szokoevek) == 0:
   print('Nincs szökőév a megadott tartományban!')
else:
    print(f'Szökőévek: ', end='')
    for ev in szokoevek:
        if ev == szokoevek[-1]:
            print(ev, end='')
        else:
            print(ev, end='; ')