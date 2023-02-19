"""
Ejercicio 7

A partir del ejercicio 5 cree un programa que vaya agregando en un
diccionario las compras realizadas.

"""

dicc_compras = {}

bandera = True

total = int(0)

while bandera:

    producto = str(input("Ingrese el nombre del producto (sea fin para finalizar): "))
    if producto.upper() == "FIN":
        bandera = False
        break

    cantidad = int(input(f"Ingrese la cantidad de {producto.capitalize()}: "))
    precio = int(input(f"Ingrese el precio de {producto.capitalize()}: "))

    dicc_compras.update({producto: cantidad, "precio": precio})

    total = total + (precio * cantidad)

print(" ")

print("-----------Lista de compras-----------")

cont = 0
aux = 1

print(" ")

for i, j in dicc_compras.items():

    if cont % 2 == 0:
        print(f"Producto: {i.capitalize()} ---- Cantidad: {j} ", end="----- $ ")
    else:
        print(j)
        aux += 1

    cont += 1

print(" ")
print(f"Total de la compra: --------- $ {total}")
print(" ")
