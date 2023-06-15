class Versenyzo:
    def __init__(self,row) -> None:
        splitted = row.split(';')
        self.nev = splitted[0]
        self.rajtszam = int(splitted[1])
        self.kategoria = splitted[2]
        self.idoeredmeny = splitted[3]
        splittedIdo = self.idoeredmeny.split(':')
        self.ora = int(splittedIdo[0])
        self.perc = int(splittedIdo[1])
        self.masodperc = int(splittedIdo[2])
        self.szazalek = int(splitted[4])
        self.teljesites =  self.ora + self.perc / 60 + self.masodperc / 3600