"""

Ejercicio 1 

Tome el ejercicio de cálculo de números pares e impares de la unidad 2 
y agréguele un bucle al código de forma de simplificarlo. 

"""

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

list = [a, b, c]

for i in list:
    if i % 2 == 0:
        print(f"El valor {i} es Par.")
    else:
        print(f"El valor {i} es Impar.")
