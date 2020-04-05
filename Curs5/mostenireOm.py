from datetime import datetime
from random import randint


class Om:
    def __init__(self, nume, data_nastere, inaltime):
        self.nume = nume.title()
        self.__data_nastere = data_nastere
        self._inaltime = inaltime

    @property
    def inlatime(self):
        return self._inaltime

    @inlatime.setter
    def inaltime(self, inaltime):
        self._inaltime = inaltime

    def merge(self):
        print(f'{self.nume} merge!')

    def vorbeste(self):
        print(f'{self.nume} vorbeste')

    def getDataNastere(self):
        return self.__data_nastere

    def setDataNastere(self, data_nastere):
        if data_nastere != None:
            self.__data_nastere = data_nastere


class Profesor(Om):
    def __init__(self, nume, data_nastere, inaltime):
        super().__init__(nume, data_nastere, inaltime)
        self.list_elevi = []
        self.__grad = None

    def scoateLaTabla(self):
        nr_elevi = len(self.list_elevi)
        if nr_elevi == 0:
            print('Nu are ce elevi sa scoata la tabla')
            return None
        else:
            elev_ascultat = self.list_elevi[randint(0, nr_elevi - 1)]
            elev_ascultat.note = randint(1, 10)
            return elev_ascultat

    @property
    def grad(self):
        return self.__grad

    @grad.setter
    def grad(self, grad):
        self.__grad = grad


class Elev(Om):
    def __init__(self, nume, data_nastere, inaltime):
        super().__init__(nume, data_nastere, inaltime)
        self.__note = []

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note):
        self.__note.append(note)


ion = Om('ion popescu', datetime(1980, 12, 3), 175)
ion.vorbeste()
ion.merge()
ion.inaltime = 231
ion.setDataNastere(datetime(1989, 2, 3))
print(ion.getDataNastere())
print(ion.inaltime)

militarul = Profesor

elev1 = Elev('elev 1', datetime(2000, 2, 12), 185)
elev2 = Elev('elev 2', datetime(2000, 3, 12), 145)
elev3 = Elev('elev 3', datetime(2000, 12, 12), 175)

profesor1 = Profesor('Prof', datetime(1980, 4, 21), 200)
profesor1.list_elevi = [elev1, elev2, elev3]

# print(profesor1.scoateLaTabla().note)
profesor1.scoateLaTabla()
profesor1.scoateLaTabla()
profesor1.scoateLaTabla()

for elev in profesor1.list_elevi:
    print(elev.note)