class Eloadas:
    def __init__(self,row) -> None:
        splitted =row.strip().split('\t')
        self.nev = splitted[0]
        self.honap = int(splitted[1])
        self.nap = int(splitted[2])
        self.sorszam = int(splitted[3])
        self.hossz = int(splitted[4])
        self.cim = splitted[5]
        self.eszkoz = splitted[6]