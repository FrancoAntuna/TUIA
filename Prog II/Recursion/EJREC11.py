def es_potencia(n: int, b: int) -> bool:
    if n == b or n == 1:
        return True
    elif b == 1 or n < b:
        return False
    else:
        return es_potencia(n/b, b)


print(es_potencia(8,2))
print(es_potencia(64,4))
print(es_potencia(70,10))
print(es_potencia(8,1))
print(es_potencia(1,8))