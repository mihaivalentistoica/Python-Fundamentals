class Caine:
    are_coada = True
    picioare = 4

    def __init__(self, nume_in, varsta_in):
        self._nume = nume_in
        self._varsta = varsta_in

    @property
    def nume(self):
        return self._nume

    @nume.setter
    def nume(self, nume_in):
        self._nume = nume_in


grivei = Caine('Grivei', 4)
print(grivei.nume)
# print()
print('Picioare: ', Caine.picioare)
print('Are coada: ', Caine.are_coada)

grivei.picioare = 3
grivei.are_coada = False
grivei.nume = 'Grivei 2'

print('Picioare grivei: ', grivei.picioare)
print('Are coada grivei: ', grivei.are_coada)
print('Picioare: ', Caine.picioare)
print('Are coada: ', Caine.are_coada)
print("Nume schimbat: ", grivei.nume)
