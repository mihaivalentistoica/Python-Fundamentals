alphabet = []
# print(f'array: {alphabet}, length: {len(alphabet)}')
alphabet.append('a')
alphabet.append('b')
alphabet.append('f')
alphabet.append('e')
# print(f'array: {alphabet}, length: {len(alphabet)}')

# print(f"""
# -3: {alphabet[-3]}
# -2: {alphabet[-2]}
# -1: {alphabet[-1]}
# 0: {alphabet[0]}
# 1: {alphabet[1]}
# 2: {alphabet[2]}
# """)
alphabet.extend(['j', 'k', 'l'])
# print(alphabet)

alphabet.sort()
# print("Sorted: ", alphabet)
alphabet.remove('a')
# print("removed", alphabet)

# print("Slice: ", alphabet[2:5])

users = ["User1", "Admin", "UserChris", "Admin", "User2", "Admin"]
# print(users.index("Admin"))
users.remove("Admin")
# print(users)


dictionar = {}
# print(f"Am initializat dictionarul:  {len(dictionar)}")
dictionar["yes"] = "oui"
dictionar['dog'] = 'chien'
dictionar['cat'] = 'chat'
# print(f"Am initializat dictionarul:  {len(dictionar)}")

dog_fr = dictionar['dog']
# print(f"Caine in fraceza: {dog_fr}")

# dictionar.update({""})

dictionar2 = {1: 'one', 2:'two', 3: 'three'}
# print(f"Lungimea dictioanrului 2: {len(dictionar2)}")
dictionar2[4] = 'four'
# print(f"Valuare lui 2: {dictionar2[2]}")
# print(f"Valuarea unui field undefined: {dictionar2[10]}")
# print(f"get() function: {dictionar2.get(10)}")
# print(f"get() cu default unknown: {dictionar2.get(10,'unknown')}")
# print(f"get(3, 'unknown'): {dictionar2.get(3, 'unknown')}")
# print(f"functia items(): {dictionar2.items()}")
# print(f"keys(): {dictionar2.keys()}; values: {dictionar2.values()}")

dictionar2.pop(1)
# print(f"dictionar dupa pop(2): {dictionar2}")
dictionar2.popitem()
# print(f"Dictionarul dupa pop items: {dictionar2}")

dictionar2.setdefault(2,'two')
# print(f"Dictionar dupa set default {dictionar2}")
dictionar2.setdefault(3, "new-three")
# print(f"Dictionar default cu 3: {dictionar2}")
dictionar0 = {0: 'zero'}
dictionar2.update(dictionar0)
# print("Dictionar 0: ", dictionar2)

dictionar2.clear()
# print(f"Dictionar curat: {dictionar2}")

dictionar2 = dict.fromkeys(["x", "y", "z"], False)
# print(f"Dictionar2 fromkeys {dictionar2}")

# print(list(dictionar2.values()))

# Touple

reteta = ('boil water', "insert egg", 'wait 5min', 'wait 5min', 'eat')
# print(f"Al treilea pas din retea: {reteta[2]}")
# print(f"Ultimii 2 pasi: {reteta[2:]}")
# print(f"Count wait 5min", {reteta.count('wait 5min')})

# print("Este pe prima pozitie", reteta.index('boil water'))
i = reteta.index('boil water')
if reteta.index('boil water') == 0:
  print("Este primul")



# Set
fish = {'cod', 'salmon', 'carp'}
bird = {'stork', 'magpie'}
animals = {"cod", "stork"}
small_pond = {"carp"}

print(f"este in fish? : {'salmon' in fish}, este in bird? {'salmon' in bird}, este in animals?, {'salmon' in animals}, este in small? {'salmon' in small_pond}")
print(f"Nu au elemente comune? {fish.isdisjoint(bird)}")
print(f"nu au elemente comune {fish.isdisjoint(animals)}")
print(f"subset {small_pond.issubset(fish)}")
