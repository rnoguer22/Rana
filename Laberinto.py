#Importamos librerias a utilizar
import math
import os
import random
import re
import sys

#Determinamos las coordenadas de nuestro laberinto
class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def comparate(self,x,y):
        if(self.x==x and self.y==y):
            return True
        else:
            return False