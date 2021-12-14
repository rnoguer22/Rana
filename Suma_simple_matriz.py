import os

def simpleArraySum(ar):
    return sum(ar)   

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    
    ar_count = int(input("Introduzca el tamaño de la matriz: ").strip())
    ar = []
    print ("Ahora introduzca los elementos de la matriz:")
    for _ in range (ar_count):
        num = int(input().strip())
        ar.append(num)
    
    result = simpleArraySum(ar)
    fptr.write(str(result))
    fptr.close()