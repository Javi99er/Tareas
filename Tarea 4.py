# invertir un numero
def inversion(x):
    if x == 0:
        print(0)

    elif x > 0:
        L = []
        a = str(x)
        for i in a:
            L.append(i)
        List1 = [num for num in reversed(L)]
        y = int(''.join(map(str, List1)))
        if  y <= (2**31 - 1):
            print(y)
        else:
            print(0)

    elif x < 0:
        x = -x
        b = str(x)
        M = []
        for i in b:
            M.append(i)
        List2 = [num for num in reversed(M)]
        z = int(''.join(map(str, List2)))
        if z <= (2**31):
            print(-z)
        else:
            print(0)

x = int(input())
inversion(x)