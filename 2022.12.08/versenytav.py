class Versenytav:

    # rajtszam = ''
    
    # def __init__(self, rajtszam):
    #     self.rajtszam = rajtszam

    # Rajtszám;Kategória;Név;Egyesület;Idő

    def __init__(self, sor):
        adatok = sor.split(';')
        self.rajtszam = adatok[0]
        self.kategoria = adatok[1]
        self.nev = adatok[2]
        self.egyesulet = adatok[3]
        self.ido = adatok[4]
        ido = adatok[4].split(':')
        self.masodpercek = int(ido[0]) * 3600 + int(ido[1]) * 60 + int(ido[2])
   
    def Tav(self) -> str:
        if self.rajtszam[0] == 'M':
            return 'Mini'
        if self.rajtszam[0] == 'R':
            return 'Rövid'
        if self.rajtszam[0] == 'K':
            return 'Közép'
        if self.rajtszam[0] == 'H':
            return 'Hosszú'
        if self.rajtszam[0] == 'P':
            return 'Pedelec'
        return 'Hibás rajtszám';

    def Nem(self):
        if self.kategoria[-1] == 'n':
            return 'Nő'
        if self.kategoria[-1] == 'f':
            return 'Férfi'
        return 'ismeretlen'