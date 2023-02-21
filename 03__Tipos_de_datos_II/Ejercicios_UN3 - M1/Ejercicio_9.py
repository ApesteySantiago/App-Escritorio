"""

Ejercicio 9

A partir del ejercicio 7 cree un programa con 4 funciones:

alta() para dar de alta la nueva compra.

baja() para dar de baja una compra.

consulta() para consultar por todas las compras realizadas hasta el momento.

modificar() para modificar una compra realizada.

"""

import os

# ----------------------------------------------------------------------------------


def alta(dicc_compras, total):

    nombre = str(input("Ingrese el nombre del producto: ")).capitalize()
    cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
    precio = int(input(f"Ingrese el precio de {nombre}: "))

    dicc_compras.update({nombre: [cantidad, precio]})
    total = total + (cantidad * precio)

    # Tambien puede usarse "global total" pero debe ser inizilizada al principio del programa
    return total


def baja(dicc_compras, total):

    lista_aux = []

    nombre = str(input("Ingrese el nombre del producto a eliminar: ")).capitalize()

    lista_aux = dicc_compras.pop(nombre)
    # Respetar [cantidad, precio].
    total = total - (lista_aux[0] * lista_aux[1])

    print(" ")
    print(f"Se a eliminado con éxito el producto: {nombre}.")


def consulta(dicc_compras, total):

    print(" ")
    print("-----------Lista de compras-----------")
    print(" ")

    for keys, values in dicc_compras.items():

        list_aux = []
        list_aux = values

        print(f"Producto {keys}: Cantidad {list_aux[0]} ----- $ {list_aux[1]}")

    print(" ")
    print(f"Total de la compra: --------- $ {total}")
    print(" ")


def modificar(dicc_compras, total):

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

                for key in dicc_compras.keys():
                    if key == nombre:
                        bandera = True
                    else:
                        print(
                            f"El elemento {nombre} no se encuentra en el diccionario."
                        )
                        bandera = False
                if bandera:
                    nuevo_nombre = str(input("Ingrese el nuevo nombre: "))
                    dicc_compras[nuevo_nombre] = dicc_compras.pop(nombre)
                else:
                    print("No se hicieron cambios.")

            elif mod == "CANTIDAD":

                os.system("cls")

                lista_aux = []

                nombre = str(
                    input("Ingrese el nombre del producto que desea modificar: ")
                ).capitalize()

                for key, value in dicc_compras.items():
                    if key == nombre:
                        lista_aux = value
                        bandera = True
                    else:
                        print(
                            f"El elemento {nombre} no se encuentra en el diccionario."
                        )
                        bandera = False

                if bandera:

                    total = total - (lista_aux[0] * lista_aux[1])

                    nueva_lista = []

                    lista_aux.pop(0)

                    lista_aux.insert(
                        0,
                        int(
                            input(
                                f"Ingrese el nuevo valor de la cantidad de {nombre}: "
                            )
                        ),
                    )

                    nueva_lista = lista_aux[0], lista_aux[1]

                    dicc_compras[nombre] = nueva_lista

                    total = total + (lista_aux[0] * lista_aux[1])

                else:
                    print("No se hicieron cambios.")

                return total

            elif mod == "PRECIO":

                os.system("cls")

                lista_aux = []

                nombre = str(
                    input("Ingrese el nombre del producto que desea modificar: ")
                ).capitalize()

                for key, value in dicc_compras.items():
                    if key == nombre:
                        lista_aux = value
                        bandera = True
                    else:
                        print(
                            f"El elemento {nombre} no se encuentra en el diccionario."
                        )
                        bandera = False

                if bandera:

                    total = total - (lista_aux[0] * lista_aux[1])

                    nueva_lista = []

                    lista_aux.pop(1)

                    lista_aux.append(
                        int(input(f"Ingrese el nuevo valor del precio de {nombre}: "))
                    )
                    # ERROR
                    nueva_lista = lista_aux[0], lista_aux[1]

                    dicc_compras[nombre] = nueva_lista

                    total = total + (lista_aux[0] * lista_aux[1])

                else:
                    print("No se hicieron cambios.")

                return total

            elif mod == "SALIR":

                os.system("cls")
                break

        else:
            print(f"{mod} no esta dentro de las opciones.")


# ----------------------------------------------------------------------------------

dicc_compras = {}

total = int(0)

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
            total = alta(dicc_compras, total)

        elif menu == "B":

            os.system("cls")
            total = baja(dicc_compras, total)

        elif menu == "C":

            os.system("cls")
            consulta(dicc_compras, total)

        elif menu == "M":

            os.system("cls")
            total = modificar(dicc_compras, total)

        elif menu == "S":
            os.system("cls")
            break
    else:
        print(f"{menu} no esta dentro del Menú.")
