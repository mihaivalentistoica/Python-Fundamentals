def getProdByName(lista, nume):
  for prod in lista:
    if prod["name"].lower() == nume.lower():
      return prod
  else:
    print(f"Nu am in magazin: {nume}")
    return None


def generareComanda(listaCumparaturi, produse, user):
  cos = []
  total = 0
  for cumparatura in listaCumparaturi:
    produs = getProdByName(produse, cumparatura)
    if (produs != None):
      cos.append(produs)
      total += produs["pret"]
  return {
    "produse": cos,
    "user": user,
    "pret_total": total
  }

u1 = {
  "first_name": "Emil",
  "last_name": "Cratita",
  "age": 37
}

produse = [
  {
    "name": "Aspirator",
    "descriere": "Cel mai bun aspirator",
    "pret": 150
  },
  {
    "name": "Matura",
    "descriere": "Cel mai bun priete",
    "pret": 50
  },
  {
    "name": "Apa",
    "descriere": "Nu bei mori",
    "pret": 5
  },
  {
    "name": "Telefon",
    "descriere": "Dupa un an iti fac update sa nu mai mearga",
    "pret": 2540
  },
  {
    "name": "Lapte",
    "descriere": "Lapte din alpi",
    "pret": 5.5
  },
  {
    "name": "Banane",
    "descriere": "Culese cu cea mai mare grija",
    "pret": 10.1
  }
]

cumparaturi = ['apa', "aspiraor", "banne", "lapte"]

print(getProdByName(produse, "Aspirator"))

comanda = generareComanda(cumparaturi, produse, u1)

print(comanda)
