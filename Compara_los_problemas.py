import math, os, random, re, sys

def compareTriplets(a, b):
    calificacion_lucia = 0
    calificacion_carlos = 0
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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()