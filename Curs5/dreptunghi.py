import math


class Dreptunghi:
    def __init__(self, lungime, latime):
        if lungime <= 0:
            print('Lungimea trebuie sa fie mai mare decat 0')
            self.lungime = 1
        else:
            self.lungime = lungime

        if latime <= 0:
            print('Latimea trebuie sa fie mai mare ca 0')
            self.latime = 1
        else:
            self.latime = latime

    def calculeazaAria(self):
        return self.lungime * self.latime

    def calculeazaPerimetru(self):
        return self.lungime * 2 + self.latime * 2

    def calculeazaLungimeaDiagonalei(self):
        return math.sqrt(self.lungime ** 2 + self.latime ** 2)


dreptunghi_1 = Dreptunghi(3, 2)
print(dreptunghi_1.calculeazaAria())
print(dreptunghi_1.calculeazaPerimetru())
print(dreptunghi_1.calculeazaLungimeaDiagonalei())