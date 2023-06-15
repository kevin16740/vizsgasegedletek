def capitalize(mondat: str):
    splitted = mondat.split(' ')
    ujmondat = ''
    for item in splitted:
        ujmondat += item.capitalize() + ' '
    return ujmondat


mondat = input('Kérem a mondatot: ')
print(capitalize(mondat))