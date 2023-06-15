from hiresek_alap import Celeb
celebek = []


def mentesFileba():
    fajl = open('celebek.txt','w', encoding='utf-8')
    for c in celebek:
        fajl.write(f'{c.nemzetiseg()} {c.name} egy híres {c.job}\n')
    fajl.close

for i in range(3):
    celeb = Celeb()
    celeb.name = input('Add meg egy híres nő nevét! ')
    celeb.job = input('Add meg a foglalkozását! ')
    celeb.nationality = input('Add meg a nemzetiségét! (a/n)! ')
    celebek.append(celeb)

for c in celebek:
    print(f'{c.nemzetiseg()} {c.name} egy híres {c.job} ')
mentesFileba()
