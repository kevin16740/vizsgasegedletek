class Versernyzok:
    def __init__(self,row) -> None:
        splitted = row.split(';')
        self.nev = splitted[0]
        self.szuletesi_datum = splitted[1]
        self.nemzetiseg = splitted[2]
        self.rajtszam = splitted[3]        
        if self.rajtszam != '':
            self.rajtszam = int(splitted[3])