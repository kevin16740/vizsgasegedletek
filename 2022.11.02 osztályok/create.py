def addResult():
    print('Új adatok megadása: ')
    res = Result()
    res.name = input('Tanuló neve:')
    res.module = input('Module: ')
    res.time = input('Idő: ')
    res.result = int(input('Eredmény: '))
    