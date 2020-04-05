'''
Creati o clasa Student cu 3 atribute private, respectiv numar_matricol(int), note(lista), este_integralist(boolean).
Sa se creeze getteri si setteri pentru toate atributele. Creati 3 obiecte de tip Student si verificati functionalitatea
getterilor si a setterilor.
'''

class Student:
    def __init__(self):
        self.__numar_matricol = None
        self.__note = []
        self.__este_integralist = None

    @property
    def numar_matricol(self):
        return self.__numar_matricol

    @numar_matricol.setter
    def numar_matricol(self, numar_matricol):
        if type(numar_matricol) == int and numar_matricol > 0:
            self.__numar_matricol = numar_matricol
        else:
            print('Numarul matricol trebuie sa fie de tip int si mai mare ca 0')

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note):
        if type(note) == list and len(note) > 0:
            note_valide = True
            for nota in note:
                if type(nota) != int or nota <= 0 or nota > 10:
                    note_valide = False
                else:
                    self.__note.append(nota)
            if note_valide != True:
                print('O parte din notele introduse sau toate nu sunt valide')

    @property
    def este_integralist(self):
        return self.__este_integralist

    def set_este_integralist(self):
        nr_note = len(self.__note)
        if nr_note > 0:
            media = sum(self.__note) / nr_note
            if media >= 5:
                self.__este_integralist = True
            else:
                self.__este_integralist = False
        else:
            print('Nu are note pentru a calcula daca este integralist!')


student1 = Student()
student2 = Student()
student3 = Student()

print("Student 1...")
student1.numar_matricol = 1
student1.note = [2, 5, 6, 40]
student1.set_este_integralist()
print(student1.numar_matricol, student1.note, student1.este_integralist)

print("Student 3...")
student2.numar_matricol = 'fasf'
student2.note = ['abc', 23, -23, 5]
student2.set_este_integralist()
print(student2.numar_matricol, student2.note, student2.este_integralist)

print("Student 3...")
student3.numar_matricol = 2321
student3.note = [32, 43, 43, 10]
student3.set_este_integralist()
print(student3.numar_matricol, student3.note, student3.este_integralist)
