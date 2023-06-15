class Utas:
    def __init__(self,row) -> None:
        splitted = row.split(';')
        self.tipus = splitted[0]
        self.ev = int(splitted[1])
        self.utas = splitted[2]
        self.szemelyzet = splitted[3]
        self. utazosebesseg = int(splitted[4])
        self.tomeg = int(splitted[5])
        self.fesztav = float(splitted[6].replace(',','.'))
        if '-' in self.utas:    
            utasok = self.utas.split('-')
            self.utasSzam = int(utasok[1])
        else:
            self.utasSzam = int(self.utas)
        
        if '-' in self.szemelyzet:    
            szemelyzet = self.szemelyzet.split('-')
            self.szemSzam = int(szemelyzet[1])
        else:
            self.szemSzam = int(self.szemelyzet)