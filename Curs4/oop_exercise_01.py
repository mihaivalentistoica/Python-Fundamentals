class Vehicul:
  def __init__(self, name, pret, tip='berlina', culoare='negru'):
    self.name = name
    self.pret = pret
    self.tip = tip
    self.culoare = culoare

  def descriere(self):
    return f'{self.name} consta {self.pret} de culoare {self.culoare}'

listaVehicule = []

for g in range(3):
  print("Creaza masina")
  nume = input('Numele masinii: ')
  pret = input('Pret: ')
  detaliiSuplim = input('Vreti sa introduceti tipul si culoarea? (da/nu) ')

  while detaliiSuplim.lower() not in ['da', 'nu', 'd', 'n']:
    detaliiSuplim = input('Va rugam sa introduceti da sau nu? (da/nu) ')

  if detaliiSuplim.lower() == 'da' or detaliiSuplim.lower() == 'd':
    tip = input("Tipul vehiculului: ")
    culoare = input("Culoare: ")
    listaVehicule.append(Vehicul(nume, pret, tip, culoare))
  else:
    listaVehicule.append(Vehicul(nume, pret))


for vh in listaVehicule:
  print(vh.descriere())