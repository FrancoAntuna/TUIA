def iterativa(l: list[int]) -> int:
    c = 1
    for i in l:
        c = c * i
    return c
pass

def recursiva(l: list[int], c) -> int:
    if len(l) != 0:
        c = c * l[0]
        return recursiva(l[1:], c)
    return c

pass

l = [1, 2, 4, 5]
multiplicacion = iterativa(l)
print(multiplicacion)
c = 1
multiplicacion = recursiva(l, c)
print(multiplicacion)
