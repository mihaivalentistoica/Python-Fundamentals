def print_rectangle(wall_size, caracter="#"):
  lungime = wall_size
  while wall_size > 0:
    print(caracter * lungime)
    wall_size -= 1


def max_of_three(a, b, c):
  max = a
  if b > max:
    max = b
  if c > max:
    max = c
  return max





# functii cu parametrii optonali
def salutare(name="World"):
  print(f"Hello, {name}")



salutare("Mihai")

print(max_of_three(10, 45, 2))

print_rectangle(5, "#")
