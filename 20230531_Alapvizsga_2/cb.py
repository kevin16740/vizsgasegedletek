class CB:
    def __init__(self,row) -> None:
        splitted = row.split(';')
        self.ora = int(splitted[0])
        self.perc = int(splitted[1])
        self.adasDb = int(splitted[2])
        self.nev = splitted[3]
    def idoTartam(self):
        return int(self.ora) + float(self.perc / 60)
    def idoPercben(self):
        return self.perc + self.ora*60