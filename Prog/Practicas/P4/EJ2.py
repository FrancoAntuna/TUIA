#Imprimir la tabla de multiplicar del numero 5

tabla = int(input("ingrese el valor que desea obtener la tabla: "))


for i in range(1,11):
    print(i, "*", tabla, "=", i * tabla)