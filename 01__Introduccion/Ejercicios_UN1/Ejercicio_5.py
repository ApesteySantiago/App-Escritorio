"""

Ejercicio 5

Escriba un programa que solicite un valor entero por pantalla y presente
en la terminal del editor el valor incrementado un 10%.

"""

result = 0

num = int(input("Enter a number for increment whit 10%: "))

result = num + (num * 0.1)

print("The value increment of the number ", num, " is: {0:.1f} ".format(result))
