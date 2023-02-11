"""
Ejercicio 5

Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5),
pero tratando de utilizar una función, de forma que la operación 
se realice dentro de la misma.

Presente el resultado en la terminal del editor.

"""

# Ejer 3
def perimetro(radio):

    nPi = 3.1416

    return 2 * nPi * radio


# Ejer 4
def area(radio):

    nPi = 3.1416

    return nPi * pow(radio, 2)


# Ejer 5
def incremento(num):

    return num + (num * 0.1)


radio = int(input("Ingrese el Radio de la circunferencia: "))

num = radio

print(
    f"El perimetro de {radio} es {perimetro(radio):.2f}; Su área es: {area(radio):.2f};",
    f"Y por último el valor incrementado en 10% es: {incremento(num):.2f}",
)
