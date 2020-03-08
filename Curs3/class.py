class Masina:
  nume: None
  tip: None
  culoare: None
  pret: None

  def __init__(self, nume, pret, tip="berlina", culoare="alba"):
    self.nume = nume
    self.tip = nume
    self.tip = tip
    self.culoare = culoare
    self.pret = pret

  def descriere(self):
    return f"Am o masina {self.nume}, {self.tip} care are culoarea {self.culoare} la un pret extraordinar de {self.pret}"

class Animal:
  __nume = ""
  __varsta = 0
  __rasa = ""

  def __init__(self, nume, rasa):
    self.__nume = nume.capitalize()
    self.__rasa = rasa.capitalize()

  def setVarsta(self, age):
    if(age > 0):
      self.__varsta = age
    else:
      print("Varsta trebuie sa fie mai mare ca 0")

  def getVarsta(self):
    return self.__varsta

  def getNme(self):
    return  self.__nume

  def getRasa(self):
    return self.__rasa


# masinaMea = Masina("Cielo", 1500, "berlina", "albastra")

# print(masinaMea.descriere())

listaMasini = []

# for i in range(0, 3):
#   print("Bine ati venit la generatorul de masini!")
#   nume = input("Numele: ")
#   pret = input("Pretul: ")
#
#   confirm = input("Vrei sa introduci tipul si culoarea masinii? (Da / Nu) ")
#
#   if confirm.lower() == 'da':
#     tip = input("Tipul: ")
#     culoare = input("Culoare: ")
#     listaMasini.append(Masina(nume, pret, tip, culoare))
#   else:
#     listaMasini.append(Masina(nume, pret))
#
# for masina in listaMasini:
#   print(masina.descriere())

# bobita = Animal()
#
# print(bobita._nume)
#
# bobita._nume = "Nume schimbat"
# print(bobita._nume)

# bobita = Animal("bobita", "maidanez")
# bobita.setVarsta(6)
# print(bobita.getNme(), bobita.getRasa(), bobita.getVarsta())

class User:
  name = ""
  __password = ""

  def __init__(self, name):
    self.name = name.capitalize()

  def setPassword(self, password):
    lungime = len(password)
    if lungime < 6:
      password = password + "#" * (6-lungime)

    self.__password = password

  @property
  def password(self):
    return self.__password[0] + '*' * (len(self.__password) - 2) + self.__password[-1]

  # @property
  # def name(self):
  #   return self.name + '$$$'

  @password.deleter
  def password(self):
    print("Sterg parola")
    del self.__password

nelu = User("nelu")
nelu.setPassword("parolamea123")
print(nelu.name, nelu.password)
del(nelu.password)
# print(nelu.password)