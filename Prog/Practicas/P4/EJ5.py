
primervalor = 0
segundovalor = 1

rango = int(input("Ingrese la longitud de la secuencia de Fibonacci: "))

print(primervalor)
print(segundovalor)

for i in range(0,rango):
    tercervalor = primervalor + segundovalor
    primervalor = segundovalor
    segundovalor = tercervalor
    print(tercervalor)

