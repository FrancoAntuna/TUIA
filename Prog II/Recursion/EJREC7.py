def positivo_digitos(n, digitos):
    if len(n) > 0:
        digitos = digitos + 1
        n = n[:-1]
        return positivo_digitos(n, digitos)
    else:
        return digitos
pass

def verificacion(n):
    if n%2 != 0:
        n = int(input("Ingrese n "))
        verificacion(n)
pass

n = int(input("Ingrese n "))
verificacion(n)
n = str(n)
digitos = 0
cant = positivo_digitos(n, digitos)
print(cant)

