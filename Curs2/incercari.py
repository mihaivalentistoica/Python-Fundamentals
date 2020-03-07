import sys
import math

# print('cow' in ['cow', 'fox'])
# print('{name} - {alt} _ {cinci}'.format(name='abc', alt='def', cinci=6))
name = 'Stoica Mihai'
age = 25

# print(f'|{name:^10}|{age:^10}|')
# print(name.split(' '))
# print(name.count('a'))
# taie = slice(5,9)
# print(name[::-1]) # revers string

palindrom = 'ana'
este = palindrom == palindrom[::-1]
# print(este)

animals = {"caine", "pisica", "cal"}
# print(animals)


# User input

# print("Bine ai venit la python");
# nume = input("Va rugam sa introduceti numele: ");

# print(f"Numele este {nuime}")

# x = int(input("Baza: "))
# y = int(input("Exponent: "))
d = {}

# d["-"] = x - y
# d["+"] = x + y
# d["*"] = x * y
#
# if y != 0:
#   d["/"] = x / y
# else:
#   d["/"] = math.inf
#   print("Y trebuie sa fie diferit de 0")
# z = x ** y
# print(f"{x} la puterea {y} este: {z}")
# print(d)

# print(sys.argv)

sum = 0
for nr in range(2020, 3031, 2):
  sum += nr

print(sum)