# def legregebbi():
#     szamok = 0
#     for result in GreatesHits80s:
#         szamok = result.split(';')
#         if int(szamok[4]) < best:
#             best = int(szamok[4])
#     return best

# def legHosszabbSzam():
#     szamok = 0
#     for result in GreatesHits80s:
#         szamok = result.split(';')
#         if int(szamok[3]) > ido:
#             ido = int(szamok[3])
#             ido = ido.split(';')
#     return ido
from data import *
from data import GreatesHits80s


def idotartam(row: str):
    splittedData = row.split(';')
    d = splittedData[3]  #pl 3:34
    timeData = d.split(':')
    minute = int(timeData[0])
    seconds = int(timeData[1])
    return minute * 60 + seconds

def megjelenes(row):
    splittedData = row.split(':')
    return int(splittedData[4])

def categorie(row):
    splittedData =  row.split(';')
    return splittedData[5]

def performer(row):
    splittedData =  row.split(';')
    return splittedData[1]
