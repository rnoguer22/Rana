import math, os, random, re, sys

def staircase(n):
    escalera = []
    for i in range (n):
        escalera.append(["#"]*i)   # Añade a la lista otra lista con el numero de #
        print (escalera)

if __name__ == '__main__':

    n = int(input("Tamaño de la escalera: ").strip())
    staircase(n)