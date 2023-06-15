class FogadoOra:
    def __init__(self,row) -> None:
        splitted = row.split(' ')
        self.VezetekNev = splitted[0] 
        self.keresztNev =splitted[1]
        self.idopont = splitted[2]
        self.fogalalasiIdo = splitted[3]
        splitteded = splitted[3].split('-')
        self.foglalasNap = splitteded[0]
        self.fogalasOra = splitteded[1]
        self.nev = splitted[0] + ' ' + splitted[1]