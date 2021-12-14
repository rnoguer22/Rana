import math, os, random, re, sys

def staircase(n):
    escalera = []
    for i in range (n):
        escalera.append(["#"]*(i+1))   # Añade a la lista otra lista con el numero de #
        print ("".join(escalera[i]))   # Printamos cada indice de la lista de manera separa

if __name__ == '__main__':

    n = int(input("Tamaño de la escalera: ").strip())
    staircase(n)