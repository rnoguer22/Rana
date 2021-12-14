import math, os, random, re, sys

def aVeryBigSum(ar):
    return sum(ar)   

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    
    ar_count = int(input("¿Cuantos elementos tiene la lista? ").strip())
    print ("Introduce los elementos de la lista")
    ar = []   # En esta lista se almacenaran los numeros
    for i in range (ar_count):   # Introducimos un bucle para introducir los numeros
        num = int(input())   # Introducimos un numero
        ar.append(num)   # El numero se almacena en la lista "ar"
    
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()