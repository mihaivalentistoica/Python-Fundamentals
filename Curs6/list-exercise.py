lista_numere = [1, 2, 3]

print(len(lista_numere))

lista_numere.append(2)

print(lista_numere)

print(lista_numere.count(2))

alta_lista = [3, 4, 5]
lista_numere.extend(alta_lista)
lista_numere.append(alta_lista)
print('alta lista: ', alta_lista)
print(lista_numere)

print(lista_numere.index(3))

print(lista_numere.insert(2, 10))
print(lista_numere)

print(lista_numere[-1])
print(lista_numere.pop(4))
print(lista_numere)

lista_numere.remove([3, 4, 5])
print(lista_numere)

lista_numere.reverse()
print(lista_numere[::-1])
print(lista_numere)

lista_numere.sort()
print(lista_numere)

del lista_numere[-2]

# lista_numere.clear()
print(lista_numere)