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
        if varsta_in < 0:
            print('Varsta animalului trebuie sa fie mai mare sau egala cu 0')
        else:
            self.__varsta = varsta_in


class Caine(Animal):
    def __init__(self):
        super().__init__()

    def latra(self):
        print(f'{self.nume} ham ham')


caine = Caine()
caine.nume = 'Azor'
caine.set_varsta(5)

print(caine.nume)
print(caine.get_varsta())
caine.latra()

cumpar = [
    {
        'nume': 'banana',
        'pret': 12,
        'descriere': 'dasfaf gdf'
    }
]

print(cumpar[0]['pret'])

# pisica = Animal()
# caine = Animal()
#
# pisica.nume = 'Pisica'
# pisica.set_varsta(-2)
#
# caine.nume = 'Caine'
# caine.set_varsta(5)
#
# print(f'animal {pisica.nume} are o varsta de {pisica.get_varsta()}')
# print(f'animal {caine.nume} are o varsta de {caine.get_varsta()}')

'''
Sa se creeze o clasa utilizator care sa contina nume, email, adresa
Sa se creze o clasa de produse care sa contina nume, pret, descriere cu ajutorul careia sa se
genereze o lista 4 produse
Creati o lista de cumparaturi de la tastatura delimitata de virgule si cautati in lista de produse.
Daca exista cel putin un produs sa se genereze o comanda dupa ce a fost itrebat utilizatorul 
'''