"""
Ejercicio 2

Escriba un programa que consulte al usuario por una oración y comente
al usuario cuantas veces aparece la letra "a"

"""

oracion = str(input("Ingrese una oracion a analizar: "))

cont = int(0)

for i in oracion:
    if i == "a":
        cont += 1

print(
    f"La cantidad de veces que aparecio la letra: A en la oracion fue de {cont} veces."
)
