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
    print("Han caido " + str(applesinsidethebox) + " manzanas dentro de la caja.")
    print("Han caido " + str(orangeinsedethebox) + " naranjas dentro de la caja.")