#!/bin/python3
import math, os, random, re, sys

def gameOfStones(n):

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    
    while True:
        n = input("Numero de piedras: ").strip()
        try:
            int(n) == True
            break
        except:
            print ("Introduzca un valor correcto por favor")
            pass
    
    result = gameOfStones(n)
    fptr.write(result + '\n')
    fptr.close()
