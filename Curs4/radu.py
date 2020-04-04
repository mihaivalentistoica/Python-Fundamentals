class Animal:
    def __init__(self):
        self.__nume = None
        self.__varsta = None

    @property
    def nume(self):
        return self.__nume



    @nume.setter
    def nume(self, nume_in):
        self.__nume = nume_in


    def get_varsta(self):
        return self.__varsta


    def set_varsta(self, varsta_in):
        self.__varsta = varsta_in


pisica = Animal()
caine = Animal()

pisica.nume = 'Pisica'
pisica.set_varsta(0.1)

caine.nume = 'Caine'
caine.set_varsta('')

print(f'animal {pisica.nume} are o varsta de {pisica.get_varsta()}')
print(f'animal {caine.nume} are o varsta de {caine.get_varsta()}')
