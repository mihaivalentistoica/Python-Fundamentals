'''
1. Creati clasa Animal cu 2 atribute private(mangled): nume si varsta. La initiere se dau valori default.
Sa se creeze getteri si setteri pentru ambele campuri.
Creati cel putin 2 obiecte si testati proprietatile create.
'''


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


pisica = Animal()  # cream cele 2 obiecte pisca si animal
caine = Animal()

pisica.nume = 'Pisica'
pisica.set_varsta(0.1)

caine.nume = 'Caine'
caine.set_varsta(3)

print(f'Animalul {pisica.nume} are o varsta de {pisica.get_varsta()}')
print(f'Animalul {caine.nume} are o varsta de {caine.get_varsta()}')

'''
2. Creati o clasa caine cu 2 atribute statice publice si 2 atribute de instanta protejate.
Faceti modificarea variabilelor din exteriorul clasei pentru 2 instante.
'''

'''
3. Creati o clasa Animal cu 1 atribut public nume si 1 atribut privat varsta.
Creati getteri si setteri pentru variabila privata.
Sa se verifice in cadrul setter-ului daca valoarea transmisa este pozitiva.
Daca valoarea nu este corecta, se afiseaza un mesaj corespunzator si nu se efectueaza atribuirea.
Sa se creeze 1 obiect(instanta) de tip animal si inca unul ce este o copie a primului( prin referinta).
Sa se modifice campurile celui de-al doilea obiect si sa se verifice modificarile aparute in cadrul ambelor obiecte create.
Sa se repete procedeul cu o alta copie a obiectului, de aceeasta data utilizandu-se 'deepcopy'.
'''


class Animal:
    def __init__(self):
        self.__nume = None
        self.__varsta = None
