linii = {}
with open('data/exemple.txt', mode='r') as exemplu:
    for index, line in enumerate(exemplu):
       linii[str(index)] = line.rstrip()

print(linii)