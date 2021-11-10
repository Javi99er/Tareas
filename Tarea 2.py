while True:
    try:
        a = int(input('ingrese un numero entero positivo a lo sumo 10: '))
        break
    except (ValueError, TypeError, IndexError):
        print('Ingrese un numero valido')

T = a

if  T > 10:
    print('Ingrese un numero valido')
elif T < 0:
    print('Ingrese un numero valido')
else:
    while T > 0:
        L = []
        N = int(input('Ingrese un entero a lo sumo 10^5: '))
        Ai = map(int, input('Ingrese enteros a lo sumo 10^9: ').split())
        T -= 1
        for c in Ai:
                L.append(int(c))
        Respuesta = 2 if sum(list(L)) % 2 != 0 else 1
        print(Respuesta)