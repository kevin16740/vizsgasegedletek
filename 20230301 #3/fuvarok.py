class Fuvar:
    def __init__(self,row) -> None:
        splitted = row.split(';') #taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja
        self.taxi_id = int(splitted[0])
        self.indulas = splitted[1]
        self.idotartam = splitted[2]
        self.tavolsag = float(splitted[3].replace(',','.'))
        self.viteldij = float(splitted[4].replace(',','.'))
        self.borravalo = float(splitted[5].replace(',','.'))
        self.fizetes_modja = splitted[6]