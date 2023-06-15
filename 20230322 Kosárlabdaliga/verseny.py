class Verseny:
    def __init__(self,row) -> None:
        splitted = row.strip().split(';')
        self.hazaiNev = splitted[0]
        self.idegenNev = splitted[1]
        self.hazaiGol = int(splitted[2])
        self.idegenGol = int(splitted[3])
        self.helyszin = splitted[4]
        self.idopont = splitted[5]