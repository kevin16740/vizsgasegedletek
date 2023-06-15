class Jelolt:
    def __init__(self,row) -> None:
        adat = row.split(' ')
        self.kerulet = int(adat[0])
        self.szavazatokSzama = int(adat[1])
        self.vezetekNev = adat[2]
        self.keresztNev = adat[3]
        self.part = adat[4]
        self.nev = self.vezetekNev + ' ' + self.keresztNev
        