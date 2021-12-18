import math, os, random, re, sys

def aVeryBigSum(ar):
    return sum(ar)   # La funcion devuelve la suma de los elementos de la lista

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    
    ar_count = int(input("¿Cuantos elementos tiene la lista? ").strip())
    print ("Introduce los elementos de la lista")
    ar = []   # En esta lista se almacenaran los numeros
    for i in range (ar_count):   # Introducimos un bucle para introducir los numeros
        num = int(input())   # Introducimos un numero
        ar.append(num)   # El numero se almacena en la lista "ar"
    
    result = aVeryBigSum(ar)   # Llamamos a la funcion
    fptr.write(str(result))   # Escribimos el resultado en el archivo OUTPUT_PATH
    fptr.close()