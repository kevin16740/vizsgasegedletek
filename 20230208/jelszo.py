import random
import string
def jelszo(szamokDb,specialisDb,kisBetu,nagyBetu):
    keszJelszo = ''
    for i in range(szamokDb):
        keszJelszo += str(random.randint(1,9))
    specialisKarakter ="@&#><{};>*äđĐ\|Ä][÷×¤ß$Ł-.,"
    letters = string.ascii_lowercase
    for i in range(kisbetu):
        hossz = len(letters)
        index = random.randint(0, hossz -1)
    keszJelszo += letters[index]
    letters = string.ascii_uppercase
    for i in range(nagybetu):
        hossz = len(letters)
        index = random.randint(0, hossz -1)
    keszJelszo += letters[index]    
    i = lisz(keszJelszo)
    random.shuffle(keszJelszo)
    result = ''.join(i)
    return result

szamokdb = int(input('Adja meg hogy db szám legyen a jelszóban? '))
specialis = int(input('Hány speciális karakter legyen?: '))
kisbetu= int(input('Hány db kisbetű?'))
nagybetu = int(input('Hány db nagybetű? '))

print(f'A generált jelszó: {jelszo(szamokdb, specialis, kisbetu, nagybetu,)}')