"""
Ejercicio 4

Escriba un programa que solicite la edad de la persona e imprima
todos los años que la persona ha cumplido.

"""
import datetime

years = int(input("Ingrese su edad: "))

for i in range(years + 1):
    print(f"Cumplio años en: {datetime.datetime.today().year - i}")
