def n_esimo (n, suma):
    if n >= 0:
        suma = suma + n
        return n_esimo(n-1, suma)
    else:
        return suma
pass

n = int(input("Ingrese n "))
suma = 0
nEs = n_esimo(n, suma)
print(nEs)