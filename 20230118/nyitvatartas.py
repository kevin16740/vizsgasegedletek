ido = float(input('Hány óra van most?'))

if ido >= 8 and ido < 16:
    print('A bolt nyitva van.')
    print(f'Ennyi órád van még odaérni {16-8}')
elif ido <=8 and ido < 16 or ido != 8 and ido > 16 or ido == 8 and ido > 16:
    print('A bolt zárva van.')