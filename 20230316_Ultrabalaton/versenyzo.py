class Versenyzo:
    def __init__(self,row) -> None:
        splitted = row.split(';')
        #Versenyzo;Rajtszam;Kategoria;Versenyido;TavSzazalek
        self.versenyzo = splitted[0]
        self.rajtszam = int(splitted[1])
        self.kategoria = splitted[2]
        self.versenyIdo = splitted[3]
        splitted1 = self.versenyIdo.split(':')
        self.ora = int(splitted1[0])
        self.perc = int(splitted1[1])
        self.masodperc = int(splitted1[2])
        self.tavSzazalek = int(splitted[4])
    
    def idoOraban(self):
        return self.ora + self.perc/60 + self.masodperc/3600
                
