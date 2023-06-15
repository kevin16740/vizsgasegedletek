from fuggvenyek import highestPower, searchPlate, totalPrice, lowestConsumption, averageAge, countBrand, highestPower

plate = input('Kérek egy rendszámot! ').upper()
if searchPlate(plate):
    print('Van ilyen rendszám a nyilvántartásban!')
else:
    print('Nincs ilyen rendszám a nyilvántartásban!')

print(f'A flotta összértéke: {totalPrice()} ,-Ft')
print(f'A flotta átlag életkora: {averageAge()}')

brand = input('Afon meg egy márkát: ')
print(f'{countBrand(brand)} db {brand} márkájú autó van a flottában.')

print(f'A legerősebb autó teljesítménye: {highestPower()} LE')
print(f'A legkedvezőbb fogyasztású autó: {lowestConsumption()} L/100Km')