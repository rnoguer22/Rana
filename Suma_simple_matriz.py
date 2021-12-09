import os

def simpleArraySum(ar):
    ar_suma = 0
    for i in ar:
        ar_suma += i
    return ar_suma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
    # Comentario de prueba
    # Otro comentario de prueba