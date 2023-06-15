from results import Result

def loadData():
    results = []
    f = open('ecdl.csv','r', encoding='utf-8')

    f.readline()
    for row in f:
        splittedData = row.split(';')
        res = Result()
        res.name = splittedData[0]
        res.module = splittedData[1]
        res.time = splittedData[2]
        res.result = int(splittedData[3])
        
        results.append(res)
    f.close()

    return results