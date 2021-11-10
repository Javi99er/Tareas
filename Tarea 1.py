# Funcion para la suma de digitos
def suma_digitos(numero):
    return sum([int(c) for c in str(numero)])

# Se desea que el formato de "a" sea entero
while True:
    try:
        a = int(input('ingrese un numero entero positivo a lo sumo 1000: '))
        break
    except (ValueError, TypeError, IndexError):
        print('Ingrese un numero valido')

# Como ya tenemos un numero entero, deseamos que este sea el numero T
T = a

# Primera dato que se desea como salida
if T <= 1000 and T > 0:
    print('Se desea saber la suma de los digitos de ', T, 'numeros enteros')
else:
    print('Este numero no es valido')

# Numero para saber cual numero N es el que se esta tomando
y = 0

while T > 0 and T <= 1000:
    T -= 1
    y += 1
    while True:
        try:
            b = int(input('Ingrese un numero entero positivo a lo sumo 1000000: '))
            break
        except (ValueError, TypeError, IndexError):
            print('Ingrese un numero valido')
    N = b
    if N < 0:
        print('La suma del numero ' , y, 'no es valido')
    else:
        x = suma_digitos(N)
        if  N > 0 and N <= 1000000:
            print('La suma del numero ', y, 'es ', x)
        else:
            print('La suma del numero ', y, 'no es valido')


