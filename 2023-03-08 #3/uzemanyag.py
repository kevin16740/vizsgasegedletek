from price import Price

euro = 307.7
prices:list[Price]= []
f = open('uzemanyag.txt','r',encoding='utf-8')
for row in f:
    prices.append(Price(row.strip()))
f.close()



print(f'3. feladat: Változások száma: {len(prices)}')



minDiff = prices[0].difference
for item in prices:
    if item.difference < minDiff:
        minDiff = item.difference   
print(minDiff)




count = 0
for item in prices:
    if item.difference == minDiff:
        count += 1
print(f'5. feladat: A legkisebb különbség előfordulása: {count}')



for item in prices:
    if item.leepDay == True:
        print('6. feladat: Volt változás szökőnapon.')
        break
else:
    print('6. feladat: Nem volt változás szökőnapon.')



f = open('euro.txt','w',encoding='utf-8')
for item in prices:
    f.write(f'{item.date};{round(item.petrol / euro,2)};{round(item.diesel / euro,2)}\n')

f.close()