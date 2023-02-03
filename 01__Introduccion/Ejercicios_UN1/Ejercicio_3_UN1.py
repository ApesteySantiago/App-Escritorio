"""
Ejercicio 3

Escriba un programa que solicite el radio de una circunferencia y 
permita calcular el perímetro.
Presen el resultado en la terminal del editor.

Utilice la siguiente fórmula: (L = 2 * π * r), 
donde L: Longitud del perimetro, π: 3.1416 y r: radio.

"""

nPi = 3.1416
L = 0

r = int(input("Enter the radio of the circumference: "))

L = 2 * nPi * r

print("The perimeter of the radio", r, " is: {0:.4f}".format(L))

# "{0:.nf}".format(variable) utilizado para delimitar los decimales de un flotante
