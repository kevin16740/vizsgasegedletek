def bmi(testTömeg, testMagassag):
    tti = testTömeg/(testMagassag*testMagassag)
    if tti < 16:
        return('súlyos soványság')
    elif tti > 16 and tti < 18.49:
        return('soványság')
    elif tti > 18.5 and tti < 24.99:
        return('normális')
    elif tti > 25 and tti < 29.99:
        return('túlsúlyos')
    elif tti >= 30:
        return('elhízás')

testTömeg = int(input('Kérem a súlyt kilogrammban:  '))
testMagassag = int(input('Kérem a magasságot cm-ben: '))
tii = round(testTömeg/(testMagassag*testMagassag), 2)
print(f'A testtömeg indexe: {tii}')

print(f'A testsúly osztálya: {bmi(testTömeg, testMagassag)}')