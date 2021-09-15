'''
Developer: Salazar
Date: 14 aug 2021
Descripcion: Scrypt Python que permita identificar el mayor de dos
Números ingresados por consola 
'''

import os

os.system("clear")

print("Ingrese primer numero: ")
n1 = int(input())
n2 =  int(input("Ingrese segundo numero: "))

if n1 > n2:
    print("El mayor es: ", n1)
elif n1 < n2:
    print("El mayor es: ", n2)
else :
    print("::: Los números son iguales :::")