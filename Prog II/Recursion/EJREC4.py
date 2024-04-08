def imprimir_para_atras(n: int):
    if n != 0:
        print(n)
        imprimir_para_atras(n-1)
pass

n = int(input("Ingrese n "))
imprimir_para_atras(n)