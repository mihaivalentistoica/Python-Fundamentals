import random

def scriereFisier():
  with open("data/example.txt", "w+") as f:  # adaug w+ pentru a putea scrie in fisier
    for i in range(random.randint(10, 100)):
      if i % 2 == 0:
        f.write(f"Acesta {'hello' * random.randint(0, i)} este {'Hello' * random.randint(0, i)} randul  nr.\n")
      else:
        f.write(f"Acesta {'hello' * random.randint(0, i)} este {'Hello' * random.randint(0, i)} randul {'Hello' * random.randint(0, i)}  nr.\n")

  with open("data/example.txt") as f:
    counter = 0
    for line in f:
      counter += line.lower().count('hello')

    with open("data/rezultat.txt", 'a') as rez:
      rez.write(f"rezulatul: {counter: >10}\n")

print("Start...")
for i in range(1000):
  scriereFisier()
else:
  print("Done")