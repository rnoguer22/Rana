#!/bin/python3
import math, os, random, re, sys

def gameOfStones(n):
    if n % 8 == 0 or n % 7 == 0:   # El jugador1 tiene mucha ventaja al empezar siempre el juego,
        ganador = "Jugador2"       # esto hace que si jugamos de una manera optima, el jugador2
    else:                          # solo pueda ganar si n es multiplo de 7 u  8
        ganador = "Jugador1"
    return ganador
         
if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    t = int(input("¿Cuantas partiditas nos vamos a echar? ").rstrip())
    for i in range(1, t+1):
        while True:
            n = input(f"Numero de piedras de la {i}º partida: ").rstrip()
            try:
                int(n) == True
                n = int(n)
                break
            except:
                print ("Introduzca un valor correcto por favor")
                pass
    
        result = gameOfStones(n)
        fptr.write(result + '\n')
    fptr.close()