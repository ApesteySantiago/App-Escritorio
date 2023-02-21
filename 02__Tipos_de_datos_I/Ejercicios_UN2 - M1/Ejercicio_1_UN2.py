"""
Ejercicio 1

(Idem ejer2 de la unidad 1 pero implementando if/else):

Cree un programa que incorpore el módulo sys, al cual desde la terminal
se le puedan pasar tres parámetros. El programa debe tomar los
parámetros e idicar en la terminal si son múltiplos de dos. 
Utilice la estructura if/else

"""
# python Ejercicio_2.py 1 2 3

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


if ((a % 2) == 0) & ((b % 2) == 0) & ((c % 2) == 0):

    print("Todos los parametros ingresados son multiplos de dos.")

else:
    print("Uno de los parametros ingresados no son multiplos de dos")
