import math, os, random, re, sys

def compareTriplets(a, b):
    calificacion_lucia = 0   # Aqui se va a almacenar la puntuacion de Lucia
    calificacion_carlos = 0  # Aqui se va a almacenar la puntiacion de Carlos
    for i in range (3):
        if a[i] > b[i]:
            calificacion_lucia += 1
        if a[i] < b[i]:
            calificacion_carlos += 1
        if a[i] == b[i]:
            continue
    matriz_retorno = [calificacion_lucia, calificacion_carlos]
    return matriz_retorno

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    
    a = []   # Creamos las listas donde se van a almacenar
    b = []   # los puntos de Lucia y de Carlos
    print ("Introduzca los puntos de Lucia:")
    for i in range (3):
        nota = int(input().rstrip())
        a.append(nota)   # Añadimos a la lista "a" los puntos de Lucia
    print ("Introduzca los puntos de Carlos:")
    for i in range (3):
        nota_ = int(input().rstrip())
        b.append(nota_)  # Añadimos a la lista "b" los puntos de Carlos

    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()