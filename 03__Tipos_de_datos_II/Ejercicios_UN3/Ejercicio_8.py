"""

Ejercicio 8

A partir del ejercicio 6 cree un programa con 4 funciones:

alta() para dar de alta la nueva compra.

baja() para dar de baja una compra.

consulta() para consultar por todas las compras realizadas hasta el momento.

modificar() para modificar una compra realizada.

"""
# ----------------------------------------------------------------------------------

import os


def alta(lista_compras):

    nombre = str(input("Ingrese el nombre del producto: ")).capitalize()

    cantidad = int(input(f"Ingrese la cantidad de unidades de {nombre}: "))

    precio = int(input(f"Ingrese el precio de {nombre}: "))

    # lista_compras[0] lo utilizo para el total de la operatoria

    lista_compras[0] = lista_compras[0] + (cantidad * precio)
    lista_compras.append(nombre)
    lista_compras.append(cantidad)
    lista_compras.append(precio)


def baja(lista_compras):

    nombre = str(input("Ingrese el producto que desea eliminar: ")).capitalize()

    i = int(lista_compras.index(nombre))

    lista_compras[0] = lista_compras[0] - (
        lista_compras.pop(i + 2) * lista_compras.pop(i + 1)
    )

    print(f"El producto: {lista_compras.pop(i)} fue eliminado.")


def consulta(lista_compras):

    print(" ")
    print("-----------Lista de compras-----------")
    print(" ")

    for i in range(1, len(lista_compras), 3):
        print(
            f"Producto {lista_compras[i]}: Cantidad: {lista_compras[i + 1]} ----- $ {lista_compras[i + 2]}"
        )

    print(" ")
    print(f"Total de la compra: --------- $ {lista_compras[0]}")
    print(" ")


def modificar(lista_compras):

    bandera = True

    while bandera:

        print(" ")
        print(" ------ ¿Que desea modificar? ------")
        print(" Nombre --- [ Modifica el nombre.   ]")
        print(" Cantidad - [ Modifica la cantidad. ]")
        print(" Precio --- [ Modifica el precio.   ]")
        print(" Salir ---- [ Sale de este Menú   ]")
        print(" ")

        mod = str(input(" Ingrese la opción: ")).upper()

        if mod == "NOMBRE" or mod == "CANTIDAD" or mod == "PRECIO" or mod == "SALIR":
            if mod == "NOMBRE":

                os.system("cls")

                nombre = str(
                    input("Ingrese el nombre del producto que desea modificar: ")
                ).capitalize()

                if lista_compras.count(nombre) == 1:

                    lista_compras[lista_compras.index(nombre)] = str(
                        input(f"Ingrese el nuevo nombre para {nombre}: ")
                    ).capitalize()

                else:
                    print(f"El elemento {nombre} no se encuentra en la lista.")

            elif mod == "CANTIDAD":

                os.system("cls")

                nombre = str(
                    input("Ingrese el nombre del producto que desea modificar: ")
                ).capitalize()

                if lista_compras.count(nombre) == 1:

                    lista_compras[0] = lista_compras[0] - (
                        lista_compras[lista_compras.index(nombre) + 1]
                        * lista_compras[lista_compras.index(nombre) + 2]
                    )

                    lista_compras[lista_compras.index(nombre) + 1] = int(
                        input(f"Ingrese la nueva cantidad para {nombre}: ")
                    )

                    lista_compras[0] = lista_compras[0] + (
                        lista_compras[lista_compras.index(nombre) + 1]
                        * lista_compras[lista_compras.index(nombre) + 2]
                    )

                else:
                    print(f"El elemento {nombre} no se encuentra en la lista.")

            elif mod == "PRECIO":

                os.system("cls")

                nombre = str(
                    input("Ingrese el nombre del producto que desea modificar: ")
                ).capitalize()

                if lista_compras.count(nombre) == 1:

                    lista_compras[0] = lista_compras[0] - (
                        lista_compras[lista_compras.index(nombre) + 1]
                        * lista_compras[lista_compras.index(nombre) + 2]
                    )

                    lista_compras[lista_compras.index(nombre) + 2] = int(
                        input(f"Ingrese el nuevo precio para {nombre}: ")
                    )

                    lista_compras[0] = lista_compras[0] + (
                        lista_compras[lista_compras.index(nombre) + 1]
                        * lista_compras[lista_compras.index(nombre) + 2]
                    )

                else:
                    print(f"El elemento {nombre} no se encuentra en la lista.")

            elif mod == "SALIR":

                os.system("cls")
                break

        else:
            print(f"{mod} no esta dentro de las opciones.")


# ----------------------------------------------------------------------------------

lista_compras = []
lista_compras.append(0)

# Orden de lista_compras = [0: subtotal, 1: nombre_producto, 2: cantidad, 3: precio, n....].

bandera = True

while bandera:

    print(" ")
    print("-----------Programa de Compras-------------")
    print("------------------Menú---------------------")
    print(" A - Alta de compra ---- B - Baja de compra")
    print(" C - Consulta compra - M - Modificar compra")
    print(" ------------- S - Salir ------------------")
    print("-------------------------------------------")

    menu = str(input(" Ingrese la opción | ")).upper()

    if menu == "A" or menu == "B" or menu == "C" or menu == "M" or menu == "S":
        if menu == "A":

            os.system("cls")
            alta(lista_compras)

        elif menu == "B":

            os.system("cls")
            baja(lista_compras)

        elif menu == "C":

            os.system("cls")
            consulta(lista_compras)

        elif menu == "M":

            os.system("cls")
            modificar(lista_compras)

        elif menu == "S":
            os.system("cls")
            break
    else:
        print(f"{menu} no esta dentro del Menú.")
