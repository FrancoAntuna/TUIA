#Dada la secuencia
#12 75 150 180 145 525 50
#Imprimir los numeros divisibles por 5 menores a 150

for i in [12, 75, 150, 180, 145, 525, 50]:
    if i%5 == 0 and i < 150:
        print(i)