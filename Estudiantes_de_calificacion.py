import math, os, random, re, sys

def gradingStudents(grades):
    
    def sig_multiplo_5(numero):
        multiplos_5 = []
        for i in range (1,101):
            if i % 5 == 0:
                multiplos_5.append(i)
        multiplos_5.append(numero)
        multiplos_5.sort()
        n = multiplos_5.index(numero)
        n += 1
        sig_multiplo = multiplos_5[n]
        return sig_multiplo

    grades_redond = []

    for i in grades:
        if 40 <= i <= 100:
            diferencia = sig_multiplo_5(i) - i
            if diferencia < 3:
                m = sig_multiplo_5(i)
                grades_redond.append(m)
            else:
                grades_redond.append(i)
        else:
            grades_redond.append(i)
    return grades_redond

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

fptr.write('\n'.join(map(str, result)))
fptr.write('\n')

fptr.close()