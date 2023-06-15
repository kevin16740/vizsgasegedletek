class Feltalalo:
    def __init__(self, sor) -> None:
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.szuletes = int(adatok[1])
        if adatok[2] == "0":
            self.halal = 0
        else:
            self.halal = int(adatok[2])
        self.talalmany = adatok[3]