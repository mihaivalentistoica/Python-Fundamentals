import random

# with open('data/random.txt', 'w') as file:
#     for i in range(100):
#         file.write(str(random.randrange(i, 100)) + ' ')
#         if i % 10 == 0 and i != 0:
#             file.write('\n')

with open('data/random.txt') as fisier_numere:
    lista_numere = []
    for linie in fisier_numere:
        numere = linie.split()
        lista_numere += [int(i) for i in numere]

    lista_numere.sort()
    print(lista_numere)
