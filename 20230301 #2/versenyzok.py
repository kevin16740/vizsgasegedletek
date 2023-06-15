class Versenyzo:
    def __init__(self,row) -> None:
        splitted = row.split(';') 
        self.helyezes = splitted[0]
        self.nev = splitted[1]
        self.orszag = splitted[2]
        self.nyeremeny = int(splitted[3])