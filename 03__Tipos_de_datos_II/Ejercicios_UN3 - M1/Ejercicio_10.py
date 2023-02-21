"""

Ejercicio 10

Escriba un programa que guarde en una variable una contraseña y
consulte al usuario por la contraseña hasta que esta sea correcta.
El programa debe informar al ususario si la contraseña fue o no correcta

"""

contra = "Riquelme1."

contraseña = str(input("Ingrese su contraseña: "))

while contraseña != contra:

    contraseña = str(input("Contraseña Incorrecta, vuelva a intentarlo: "))

print("Acceso concedido. Contraseña Correcta.")
