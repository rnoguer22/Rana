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