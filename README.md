# Rana
Pincha [aqui](https://github.com/rnoguer22/Rana.git) para acceder al link del repositorio

Hemos resuelto los integrantes del grupo (Paula Naranjo Borrallo y Ruben Nogueras Gonzalez), de manera conjunta, los ejercicios propuestos en "Entrega de Ejercicios Grupales".
El codigo y el diagrama de flujo de cada uno de los ejercicios de la entrega son los siguientes:

Suma simple de una matriz:

```PYTHON3
import os
def simpleArraySum(ar):
    return sum(ar)   # Devuelve la suma de los elementos de la matriz  

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')   # Abrimos el archivo
    
    ar_count = int(input("Introduzca el tamaño de la matriz: ").strip())
    ar = []   # Definimos ar como una lista vacia
    print ("Ahora introduzca los elementos de la matriz:")
    for _ in range (ar_count):
        num = int(input().strip())
        ar.append(num)   # De esta manera podemos introducir los numeros a la lista "ar"
    
    result = simpleArraySum(ar)   # Llamamos a la funcion
    fptr.write(str(result))   # Escribimos la suma de los numeros en el fichero OUTPUT_PATH
    fptr.close()
```


 
<img width="744" alt="Captura de pantalla 2021-12-18 a las 17 17 33" src="https://user-images.githubusercontent.com/91721496/146648068-aff2e8e3-39ee-460c-a52d-d2a1028bf595.png">


    
Compara los problemas:
```Python3
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

    fptr.close()
```

![Diagrama_Compara_los_problemas](https://user-images.githubusercontent.com/91721762/146639922-b466d457-b009-4ed9-afad-c76e14785d33.png)

Una suma muy grande:

```Python3
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
```

  <img width="774" alt="Captura de pantalla 2021-12-18 a las 17 28 17" src="https://user-images.githubusercontent.com/91721496/146648472-1e795677-188b-434c-943e-fbbd61c39a4a.png">
  
    
La escalera:
```Python3
import math, os, random, re, sys

def staircase(n):
    escalera = []
    for i in range (n):
        escalera.append(["#"]*(i+1))   # Añade a la lista otra lista con el numero de #
        print ("".join(escalera[i]))   # Printamos cada indice de la lista de manera separa

if __name__ == '__main__':

    n = int(input("Tamaño de la escalera: ").strip())
    staircase(n)
```

![Diagrama_La_escalera](https://user-images.githubusercontent.com/91721762/146639943-2117cef0-08b6-49c6-80b6-bd79547e893e.png)

Juego de piedras:
```Python3
import math, os, random, re, sys

def gameOfStones(n):
    if n % 8 == 0 or n % 7 == 0:   # El jugador1 tiene mucha ventaja al empezar siempre el juego,
        ganador = "Jugador2"       # esto hace que si jugamos de una manera optima, el jugador2
    else:                          # solo pueda ganar si n es multiplo de 7 u  8
        ganador = "Jugador1"
    return ganador
         
if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    t = int(input("¿Cuantas partiditas nos vamos a echar? ").rstrip())
    for i in range(1, t+1):
        while True:
            n = input(f"Numero de piedras de la {i}º partida: ").rstrip()
            try:
                int(n) == True
                n = int(n)
                break
            except:
                print ("Introduzca un valor correcto por favor")
                pass
    
        result = gameOfStones(n)
        fptr.write(result + '\n')
    fptr.close()
```

![Diagrama_Juego_piedras](https://user-images.githubusercontent.com/91721762/146639959-84922a99-816c-479e-95a0-97769582218c.png)

Rana en laberinto:
```Python3
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
#Determinamos las coordenadas del tunel
class Tunel:
    def __init__(self, x1, y1, x2, y2):
        self.extremo1 = Coordenadas(x1, y1)
        self.extremo2 = Coordenadas(x2, y2)
        
#Definimos una funcion para movernos dentro del tunel
def buscaTunel(Casillax,Casillay,tuneles):
    coordenadas = Coordenadas(Casillax, Casillay)
    for t in tuneles:
        if(t.extremo1.comparate(Casillax,Casillay)==True):
            coordenadas.x=t.extremo2.x
            coordenadas.y=t.extremo2.y
            break
        elif(t.extremo2.comparate(Casillax,Casillay)==True):
            coordenadas.x=t.extremo1.x
            coordenadas.y=t.extremo1.y
            break
    return coordenadas

#Definimos una funcion para explorar las casillas
def exploracion(Casillax, Casillay, laberinto, n , m, tuneles):
    num=0
    den=0
    probabilidad=0.0
    if(Casillax>0 and laberinto[Casillax-1][Casillay]!="#"):
        den +=1
        if(laberinto[Casillax-1][Casillay]=="%"):
            num+=1
    if(Casillax<n-1 and laberinto[Casillax+1][Casillay]!="#"):
        den +=1
        if(laberinto[Casillax+1][Casillay]=="%"):
            num+=1
    if(Casillay<m-1 and laberinto[Casillax][Casillay+1]!="#"):
        den +=1
        if(laberinto[Casillax][Casillay+1]=="%"):
            num+=1
    if(Casillay>0 and laberinto[Casillax][Casillay-1]!="#"):
        den +=1
        if(laberinto[Casillax][Casillay-1]=="%"):
            num+=1
    if(den==0):
        return probabilidad
    probabilidad=num/den
    if(Casillax>0 and laberinto[Casillax-1][Casillay]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax-1,Casillay,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den
    if(Casillax<n-1 and laberinto[Casillax+1][Casillay]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax+1,Casillay,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den
    if(Casillay<m-1 and laberinto[Casillax][Casillay+1]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax,Casillay+1,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den
    if(Casillay>0 and laberinto[Casillax][Casillay-1]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax,Casillay-1,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=(exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den)
    return probabilidad 

#Utilizamos una condición para las propiedades del laberinto
if __name__ == '__main__':
    print("Por favor introduzca las dimensiones del laberinto y el número de tuneles:(filas, columnas, tuneles)")
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])
    laberinto=[]
    for n_itr in range(n):
        print("Fila " + str(n_itr) + " del laberinto:(# muro,porcentaje salida, * bomba, $ vacia o tunel")
        row = input()
        laberinto.append(list(row))
```

<img width="727" alt="Captura de pantalla 2021-12-18 a las 17 44 14" src="https://user-images.githubusercontent.com/91721496/146648921-2717916b-666b-436c-bcf8-b62faa8fd08f.png">


Estudiantes de calificacion:
```Python3
import math, os, random, re, sys

def gradingStudents(grades):
    
    # Esta funcion nos calcula el siguiente multiplo de 5 de cada nota almacenada en grades
    def sig_multiplo_5(numero):
        multiplos_5 = []
        for i in range (1,101):
            if i % 5 == 0:   # Si el resto de dividir la nota entre 5 es 0, es un multiplo
                multiplos_5.append(i)
        multiplos_5.append(numero)
        multiplos_5.sort()   # Ordenamos los numeros de la lista
        n = multiplos_5.index(numero)
        n += 1   # Este sera el indice del siguiente multiplo de 5 de la variable "numero"
        sig_multiplo = multiplos_5[n]
        return sig_multiplo   # La funcion devuelve el siguiente multiplo de 5

    grades_redond = []

    for i in grades:
        if 40 <= i <= 100:
            diferencia = sig_multiplo_5(i) - i
            if diferencia < 3:
                m = sig_multiplo_5(i)   # Redondea la nota al siguiente multiplo de 5
                grades_redond.append(m)   # Añade la nota redondeada a la lista
            else:
                grades_redond.append(i)   # No redondea la nota
        else:
            grades_redond.append(i)   # La nota es < 40 por lo tanto se queda igual
    return grades_redond   # Devuelve las notas finales

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')   # Abrimos el archivo
    grades_count = int(input("Introduzca el numero de estudiantes: ").strip())
    grades = []   # En esta lista se almacenaran las notas iniciales de los estudiantes
    
    for _ in range(grades_count):
        grades_item = random.randint(0, 100)   # A cada estudiante se le asigna una nota random
        print (grades_item)
        grades.append(grades_item)   # Almacenamos esa nota en la lista

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))

    fptr.close()
```

![Diagrama_Estudiantes_de_calificacion](https://user-images.githubusercontent.com/91721762/146640011-bf12fc30-393f-4813-805c-dafbcf2a3e97.png)

Manzana y naranja:
```Python3
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

```



<img width="723" alt="Captura de pantalla 2021-12-18 a las 17 49 40" src="https://user-images.githubusercontent.com/91721496/146649079-fadeaf91-cf31-424b-9727-68c85c02c8f2.png">
