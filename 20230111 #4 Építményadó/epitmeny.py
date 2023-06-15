class epitmeny:
    def __init__(self, sor: str) -> None:
       #"90561 Aradi 10 c 168"
        splitted = sor.split(' ')
        self.adoszam = splitted[0]
        self.utca = splitted[1]
        self.hazszam = splitted[2]
        self.tipus = splitted[3]
        self.alapterulet = int(splitted[4])