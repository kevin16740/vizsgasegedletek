def ritkit(szo):
    ujszo = ''
    for item in szo:
        ujszo += item + ' '
    return ujszo

szo = input('Kérem a szót: ')

print(f'{ritkit(szo)}''')