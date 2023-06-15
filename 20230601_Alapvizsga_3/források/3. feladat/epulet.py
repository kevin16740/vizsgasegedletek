class Epulet:
    def __init__(self,row) -> None:
        splitted = row.split(';')
        self.nev = splitted[0]
        self.varos = splitted[1]
        self.orszag = splitted[2]
        self.magassag = float(splitted[3].replace(',','.'))
        self.emelet = int(splitted[4])
        self.epult = int(splitted[5])
    