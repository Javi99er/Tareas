import math

# Saber si un numero es potencia de dos
def potencia(n):
    R = math.log2(n)
    if round(R) == R:
        if round(R) == 0:
            print('False')
        else:
            print('True')
    else:
        print('False')

'''
T = int(input('Ingrese un entero entre uno y treinta: '))
for i in range(T):
    N = int(input('Ingrese un entero entre uno y 2^30: '))
    potencia(N)
'''
T = int(input())
for _ in range(T):
    N = int(input())
    potencia(N)