
from functions import beolvas, celbaerkezokAranya, Versenyzokszama, VoltTobbMint, Gyoztes

beolvas('bukkm2019.txt')

print(f'Versenytávot nem teljesítők: {celbaerkezokAranya():.3}%')

print(f'Rövid távon indult nők száma: {Versenyzokszama("Rövid","Nő")}')

print(f'Mini távon indult nők száma: {Versenyzokszama("Mini","Férfi")}')
if VoltTobbMint(6*60*60):
    print('Volt ilyen versenyző')
else:
    print('Volt ilyen versenyző')

print(f'Rövid távon indult felnőtt férfi nyertes:')
print(f'\t Rajtszám: {gyoztes.rajtszam}')
print(f'\t Név: {gyoztes.nev}')
print(f'\t Egyesület: {gyoztes.egyesulet}')
print(f'\t Idő: {gyoztes.ido}')