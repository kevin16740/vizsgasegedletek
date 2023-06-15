from menu import *

names = []

def load():
    file = open('people.csv','r', encoding= 'utf-8')
    
    for row in file:
        names.append(row.strip())

    file.close()

def listAll():
    for name in names:
        print(name, end=' ')
    print()
def search(name):
    results = []
    if name.upper() in names.upper():
        results.append(name)
    return results

def searchWithIndex(name):
    results = []
    for index in range(len(names)):
        if name.upper() in names[index].upper():
            results.append(index)
    return results


def new(name, reginev):
    names.remove(reginev)
    names.append(name)
    f = open('people.csv','a',encoding='utf-8')
    f.write(name + '\n')
    f.close()
def delete(name):
    if name in names:
        names.remove(name)
    f = open('people.csv','a',encoding='utf-8')
    writeNamesToFile()
    f.close()
def writeNamesToFile():
    file = open('people.csv','w',encoding = 'utf-8')
    for name in names:
        file.write(name + '\n')
def update(nev, newName):
    names.remove(nev)
    names.append(newName)
    writeNamesToFile()

def updateByIndex(index, newName):
    names.pop(index)
    names.append(newName)
    writeNamesToFile()