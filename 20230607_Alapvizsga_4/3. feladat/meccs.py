class Meccs:
    def __init__(self,row) -> None:
        splitted = row.split(';')
        self.ev = int(splitted[0])
        self.het = int(splitted[1])
        self.fordulo = int(splitted[2])
        self.T13p1 = int(splitted[3])
        self.nyeremeny = int(splitted[4])
        self.eredmenyek = splitted[5]
