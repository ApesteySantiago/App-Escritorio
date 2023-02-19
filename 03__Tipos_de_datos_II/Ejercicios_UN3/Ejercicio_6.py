"""
Ejercicio 6

A partir del ejercicio 5 cree un programa que vaya agregando en una 
lista las compras realizadas.

"""
lista_compras = []

bandera = True

total = int(0)

while bandera:

    cantidad = int(
        input(
            "Ingrese la cantidad de unidades de la misma FoV (sea 0 para finalizar): "
        )
    )
    if cantidad == 0:
        bandera = False
        break

    precio = int(input("Ingrese el precio de dicha FoV: "))

    lista_compras.append(cantidad)
    lista_compras.append(precio)

    total = total + (precio * cantidad)

# Print pantalla --->

print(" ")

print("-----------Lista de compras-----------")

cont = 0
aux = 1

print(" ")

for i in lista_compras:

    if cont % 2 == 0:
        print(f"Producto {aux}: Cantidad: {i} ", end="----- $ ")
    else:
        print(i)
        aux += 1

    cont += 1

print(" ")
print(f"Total de la compra: --------- $ {total}")
print(" ")
