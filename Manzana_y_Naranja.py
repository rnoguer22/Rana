#Importamos librerias a utilizar
import math
import os
import random
import re
import sys

#Definimos la función para contabilizar las manzanas y naranjas
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesinsidethebox=0
    orangeinsedethebox=0
    for apple in apples:
        if(a+apple>=s and a+apple<=t):
            applesinsidethebox+=1
    for orange in oranges:
        if(b+orange>=s and b+orange<=t):
            orangeinsedethebox+=1
    print("Han caido " + str(applesinsidethebox) + " manzanas dentro de la caja")
    print("Han caido " + str(orangeinsedethebox) + " naranjas dentro de la caja.")
    
#Definimos una condición para contabilizar las manzanas y naranjas 
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()


    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
