'''
Primera forma de sumar los digitos de un numero

Sdigitos, ExtraerN = 0, 0.
NumEntero = int(input("Ingrese un numero entero: "))

while NumEntero != 0:
    ExtraerN = NumEntero % 10.
    NumEntero //= 10.
    Sdigitos += ExtraerN

print("La suma de los digitos es: {}".format(Sdigitos))
'''

'''
Segunda forma de sumar los digitos de un numero 
def sake(numero):
    return sum([int(c) for c in str(numero)])

def sake2(numero1):
    if isinstance(numero1, int):
        suma1 = sake(numero1)
        return suma1

x = int(input('ingrese un numero: '))

print(sake2(x))
print(sake(x))
'''

print('While controlado con Evento')
print('===============================')

print('Calcular promedio')
promedio=0.1
total=0
contar=0

print('Escribe el valor (-1 para salir):')
grado=int(input())

while grado !=-1:
  total=total+grado
  contar= contar + 1
  print('Escribe el valor (-1 para salir):')
  grado=int(input())

  promedio=total/contar
  print('El promedio es ' +str(promedio))