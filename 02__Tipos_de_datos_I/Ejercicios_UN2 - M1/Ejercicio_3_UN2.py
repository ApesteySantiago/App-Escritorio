"""
Ejercicio 3

Tome dos valores por consola, y guarde en una lista:

[primer_valor, segundo_valor, la_suma_de_los_valores]

Presente el resultado en la terminal del editor.

"""

lista_suma = [5, 6, 0]

lista_suma[2] = sum(lista_suma[0:2])

print(f"La sumatoria de {lista_suma[0]} + {lista_suma[1]} = {lista_suma[2]}")
