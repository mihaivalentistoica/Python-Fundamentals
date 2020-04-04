from copy import deepcopy

class Animal:
    def __init__(self, nume_in):
        self.nume = nume_in
        self.__varsta = None

    @property
    def varsta(self):
        return self.__varsta

    @varsta.setter
    def varsta(self, varsta_in):
        if varsta_in < 0:
            print('Nu putem sa avem varsta negativa')
        else:
            self.__varsta = varsta_in


azorel = Animal('Azorel')
azorel.varsta = 3

grivei = deepcopy(azorel)

print('Grivei nume: ', grivei.nume)
azorel.nume = 'Alt Azorel'
print('Grivei nume: ', grivei.nume)

