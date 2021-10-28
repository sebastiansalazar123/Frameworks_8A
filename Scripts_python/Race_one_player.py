'''
Developer: Salazar
Reto:
        Requerimiento del Script:

        -> Un solo jugador lanza los dados
        -> Debe recorrer  de cero (0) a cien posiciones (100)
        -> El puede termina cuando:
            - Cuando el judor obtenga dos pares consecutivos
            - Cuando llegue a la meta (100+)
'''

'''
    Description: Script en Python que permita lanzar los dados de manera indefinida Y sólo 
    finalizará cuando se genere un PAR de DADOS (1,1 - 2,2 - 3,3 - 4,4 - 5,5 - 6,6)
'''
import os
from random import randint

#Functions


ban1 = True
ban2 = True
a = 0

def dices() :
    status = True

    while status :     #while status ==> while status == True
        os.system("clear")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        a = dice1 + dice2
        print("D1: ", dice1)
        print("D2: ", dice2)


        if dice1 == dice2 :
            print("::: PRIMER PAR!!!!!!!!!!!!!!. Sigue intenando :::" + a)
            
            status = False 

        else :
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...33333" )
            
dices()  

