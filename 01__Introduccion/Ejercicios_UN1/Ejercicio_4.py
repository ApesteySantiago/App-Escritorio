"""
Ejercicio 4

Escriba un programa que solicite el radio de una circunferencia y
permita calcular su área. Presente el resultado en la terminal de editor.

Utilice la siguiente fórmula: A = π * r hypot2. A: Area, π:3.1416, r: radio.

"""

nPi = 3.1416
A = 0

r = int(input("Enter the radio of the circumference: "))

A = nPi * pow(r, 2)

print("The area of the circumference of radio", r, " is: {0:.2f} ".format(A))
