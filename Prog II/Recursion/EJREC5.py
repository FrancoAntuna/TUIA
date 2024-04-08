def recursiva(t: int, k: int) -> int:
    if t >= 100:
        return k
    else:
        return recursiva(t + k, k + 1)
pass

def iterativa (t:int, k:int) -> int:
    while t <= 100:
        t = t + k
        k = k + 1
    return k
pass

t = int(input("Ingrese t "))
k = int(input("Ingrese k "))
suma = recursiva(t, k)
print(suma)
suma = iterativa(t, k)
print(suma)