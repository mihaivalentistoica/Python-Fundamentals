"""
2. Creati o clasa Profesor cu 3 atribute private: materie(string), numar_studenti(int) si facultate(string).
Constructorul nu are niciun parametru, atributele se declara(in constructor) None. Creati getteri si setteri pentru
toate atributele. Sa se suprascrie metoda __str__ si ca sa returneze o descriere a obiectului, utilizand toate
atributele.Creati 2 instante ale clasei Profesor, setati toate atributele si afisati str(Profesor).

"""


class Profesor:
    def __init__(self):
        self.__materie = None
        self.__numar_studenti = None
        self.__facultate = None

    @property
    def materie(self):
        return self.__materie

    @materie.setter
    def materie(self, materie):
        if type(materie) == str:
            self.__materie = materie.lower()
        else:
            print('Materia trebuie sa fie un sir de caractere')

    @property
    def numar_studenti(self):
        return self.__numar_studenti

    @numar_studenti.setter
    def numar_studenti(self, numar_studenti):
        if type(numar_studenti) == int and numar_studenti > 0:
            self.__numar_studenti = numar_studenti
        else:
            print('Numarul de studenti trebuie sa fie de tip intreg si mai mare ca 0')

    @property
    def facultate(self):
        return self.__facultate

    @facultate.setter
    def facultate(self, facultate):
        if type(facultate) == str:
            self.__facultate = facultate.title()
        else:
            print("Facultatea introdusa trebuie sa fie de tip caractere")

    def __str__(self):
        return f'In cadrul facultatii {self.__facultate} profesorul de {self.__materie} are {self.__numar_studenti} studenti'

caragiale = Profesor()
caragiale.facultate = 'Litere'
caragiale.numar_studenti = 250
caragiale.materie = 'Arte'
print(caragiale.__str__())
