# lottó szám sorsolás
# 5/90, 6/45, 7/35...

from random import randint


lottoSzamok = []

def sorsolas(darab, osszes):
    # for i in range(darab):
    while len(lottoSzamok) < darab:
        kihuzottSzam = randint(1, osszes)
        if kihuzottSzam not in lottoSzamok:
            lottoSzamok.append(kihuzottSzam)

# sorsolas(5, 90)
sorsolas(7, 35)
print(lottoSzamok)