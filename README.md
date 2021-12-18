# Rana
Pincha [aqui](https://github.com/rnoguer22/Rana.git) para acceder al link del repositorio

Hemos resuelto los integrantes del grupo (Paula Naranjo Burdallo y Ruben Nogueras Gonzalez), de manera conjunta, los ejercicios propuestos en "Entrega de Ejercicios Grupales".
El codigo y el diagrama de flujo de cada uno de los ejercicios de la entrega son los siguientes:

Suma simple de una matriz:

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
