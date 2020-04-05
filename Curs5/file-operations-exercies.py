# with open('data/exercise.txt', 'r') as exercise:
#     cuvant = input('Cuvantul cautat: ')
#     count = 0
#     for linie in exercise:
#         linie_lower = linie.lower()
#         # count += linie.lower().count(cuvant.lower())
#         cuvinte = linie_lower.split()
#         print(cuvinte)
#     print("Cuvantul a fost gasit de ", count, ' ori')
#
#     with open('data/cautareCuvinte.txt', mode='a') as result:
#         result.write(f'Cuvantul a fost gasit de {count} ori \n')

# exercise = open('data/exercise.txt')
# cuvant = input('Cauta cuvat: ')
# count = 0

with open('data/exercise.txt') as fisier:
    counter_cuvinte = {}
    caractere = [',', '.', '?', '!']

    for line in fisier:
        linei_lower = line.lower()
        for chr in caractere:
            linei_lower = linei_lower.replace(chr, '')

        cuvinte = linei_lower.split()
        for cuvant in cuvinte:
            if cuvant in counter_cuvinte.keys():
                counter_cuvinte[cuvant] += 1
            else:
                counter_cuvinte[cuvant] = 1

    with open('data/cautareCuvinte.txt', 'w') as rezultat:
        for key, count in counter_cuvinte.items():
            rezultat.write(f'"{key}" apare de {count} \n')