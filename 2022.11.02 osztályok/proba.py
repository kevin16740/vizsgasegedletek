from results import Result

results = []

res1 = Result() #példányosítás = result osztályból létrehozok egy osztálypéldányt
res1.name = 'Kovács Béla'
res1.module = 'Excel'
res1.time = '41:41'
res1.result = 30

results.append(res1)


res2 = Result() 
res2.name = 'Takács Béni'
res2.module = 'PPT'
res2.time = '41:42'
res2.result = 40

results.append(res2)


for item in results:
    print(item.name, '-', item.time, '-', item.module, '-', item.result)
