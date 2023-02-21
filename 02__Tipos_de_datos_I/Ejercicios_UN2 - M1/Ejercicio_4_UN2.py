"""
Ejercicio 4

Realice un programa que consulte la edad y en caso de que el valor
ingresado supere la fecha de jubilación, presente en la terminal
el mensaje "Ya está en edad de jubilarse." en caso contrario que 
presente "Aún está en edad de trabajar.".

"""

edad = int(input("Ingrese su edad: "))

if edad >= 65:
    print("Ya está en edad de jubilarse.")

else:
    print("Aún está en edad de trabajar.")
