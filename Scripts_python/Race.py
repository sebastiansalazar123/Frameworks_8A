'''
Se requiere un Script en Python que permita simular el juego  de 
carrera numerica con dos Players.
La carrera inicia  en la posicion CERO y finaliza en la posicion 100.
El juego se realiza por default con 2 jugadores.
El jugagador que lluge primero a la meta (posición 100 sera el ganador).
Si un jugador genera 3 pares consecutivos en el lanzamiento de los dados será directamente ganador.
Repite tiro si y solo si saca PAR.
'''

#randint => Genera valores númericos enteros (+,-)
#uniform => Genera valores númericos reales [R] (+,-)

import os
from random import randint, uniform 

os.system("clear")

dice1 = randint(1,6)
dice2 = randint(1,6)

print("Dice 1: ", dice1)
print("Dice 2: ", dice2)