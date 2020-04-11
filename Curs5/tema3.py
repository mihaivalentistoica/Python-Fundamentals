"""
3. Creati un fisier "fisier1.txt". Scrieti 5 linii in fisier care sa contina cate un nume si un nr de telefon (stringuri!).
Citisi fisierul "fisier1.txt" si memorati intr-un dictionar fiecare nume(cheia) si numarul de telefon aferent(valoarea).
Adaugati la sfarsitul fisierului dictionarul creat.
"""
with open('data/carte_telefon.txt', 'a') as carte_telefon:
   carte_telefon.write('nume1 017561')
   carte_telefon.write('nume2 523511')
   carte_telefon.write('nume3 23511')
   carte_telefon.write('nume4 053252')
   carte_telefon.write('nume5 01543')
   carte_telefon.write('nume6 01532')
   carte_telefon.write('nume6 01432')

# with open('data/cautareCuvinte.txt') as fisier_numer: