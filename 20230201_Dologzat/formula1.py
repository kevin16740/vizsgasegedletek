def length(circuit): # Egészítse ki a függvényt a hiányzó formális paraméterrel!
    circuits = {}
    circuits['HUN'] = 4.381
    circuits['BEL'] = 7.004
    circuits['ITA'] = 5.793
    circuits['MON'] = 3.337
    lengthOfCircuit = circuits[circuit]
    return lengthOfCircuit


def sebesseg(idokor, lengthOfCircuit):
    splitted = idokor.split(':') 
    masodperc = (int(splitted[0]) * 60) + (int(splitted[2]) / 1000 + int(splitted[1]))
    atlagSebesseg = (lengthOfCircuit / (masodperc / 3600))
    return atlagSebesseg

circuit = input('Válassza ki a pályát (HUN/BEL/MON/ITA): ')
versenyzo = 0
for i in range(3):
    versenyzo += 1
    nev = input(f'A(z) {versenyzo} versenyző: \n\tNeve: ')
    idokor = input('\tideje (pp:mm:eee): ')
    print(f'{nev} versenyző átlagsebessége: {round(sebesseg(idokor,length(circuit)), 2)} km/h')