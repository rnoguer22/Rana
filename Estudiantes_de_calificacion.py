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
        grades.append(grades_item)   # Almacenamos esa nota en la lista

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()