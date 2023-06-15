meterSzeles = int(input('Hány méter széles a terület?: '))
meterHosszu = int(input('Hány méter hosszú a terület?: '))

terulet = meterSzeles * meterHosszu
teruletSzogol = terulet * 0.2780364289
munkadij = int(5000 + ((teruletSzogol / 100) * 7))
print(f'A felszántandó tertület: \n\tMérete: (m2) : {terulet} \n\tMérete (négyszögöl): {teruletSzogol} \n\tMunkadíj: {munkadij}Ft.')