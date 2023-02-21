"""
Ejercicio 5

Suponga que tiene una verdulería y carga la cantidad y el precio de lo
comprado por un cliente. Realice un programa que tome de a uno la
cantidad y el precio comprado por el cliente y al finalizar la compra
retorne el monto total gastado.

"""

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

    total = total + (precio * cantidad)

print(f"El monto total a pagar es de: $ {total}.")
