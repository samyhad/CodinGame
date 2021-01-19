import sys
import math

l = int(input())
h = int(input())
t = input()
rows = []

for i in range(h):
    row = input()
    rows.append(row)

letras=[]

for index_digito in range(len(t)):
    digito = t[index_digito].upper()

    if not (ord(digito) >= 65 and ord(digito) <= 90):
        digito = '['

    min = (ord(digito) - 65) * l
    max = (ord(digito) - 65 + 1) * l

    letra = []

    for col in range(h):
        letra.append(rows[col][min:max])

    if not letras:  # List is empty
            letras = letra
    else:
        for col in range(h):
            letras[col] = letras[col] + letra[col]

for col in range(h):
    print(letras[col][:])


