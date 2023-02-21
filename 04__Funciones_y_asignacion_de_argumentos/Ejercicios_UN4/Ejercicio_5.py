"""

Ejercicio 5

Cree un programa que utilizando una función solicite la edad de la
persona e imprima todos los años que la persona a cumplido segun el
siguiente formato de ejemplo:

1,2,3,4,5
Y
5,4,3,2,1

"""
aux = 0

edad = int(input("Ingrese su edad: "))


def primer_ejemplo(edad):
    global aux
    if aux == edad:
        print(aux)
        return 0
    else:
        print(aux, end=", ")
        aux += 1
        return primer_ejemplo(edad)


primer_ejemplo(edad)


print(" ")


def segundo_ejemplo(edad):
    print(edad, end=", ")
    if edad == 0:
        return 0
    else:
        return segundo_ejemplo(edad - 1)


segundo_ejemplo(edad)
