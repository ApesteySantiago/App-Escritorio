"""
Ejercicio 3

Escriba un programa que consulte al usuario por una oración y comente
al usuario cuantas veces aparecen todas las vocales considerando
minúsculas, mayúsculas y acentos.

"""

oracion = str(input("Ingrese la oracion a analizar: "))

conta = int(0)
conte = int(0)
conti = int(0)
conto = int(0)
contu = int(0)

for i in oracion:
    if i == "a" or i == "A" or i == "á" or i == "Á":
        conta += 1
    elif i == "e" or i == "E" or i == "é" or i == "É":
        conte += 1
    elif i == "i" or i == "I" or i == "í" or i == "Í":
        conti += 1
    elif i == "o" or i == "O" or i == "ó" or i == "Ó":
        conto += 1
    elif i == "u" or i == "U" or i == "ú" or i == "Ú":
        contu += 1

print(
    f"Veces que aparecio la vocal: a: {conta}; e: {conte}; i: {conti}; o: {conto}; u: {contu}."
)
