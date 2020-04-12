cuvinte = "Acesta este un string de minim 10 care"
mijloc = int(len(cuvinte) / 2)
print(len(cuvinte))
if len(cuvinte) % 2 == 0:
    substring = cuvinte[(mijloc - 2):(mijloc + 2)]
    print(substring)
else:
    substring = cuvinte[mijloc - 2:mijloc + 3]
    print(substring)

lista_nume = ['Ana', 'Maria', 'Eleonida']
nume_complet = ' '.join(lista_nume)
print(nume_complet.find('Maria'))