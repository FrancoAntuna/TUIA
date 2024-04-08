#Escriba los siguientes programas. Nota: No utilice los metodos index, min, max, 
#reverse.
#a. Dada una lista de números list y un número n, determine en qué índice de la lista
#list se
#encuentra el número n. En caso de no encontrarlo, el programa mostrará -1. Ejemplos

#list = [11 ,25 ,3 , -4 ,95]
#n = 3
# El programa debería mostrar
#2

contador = 0
numseleccionado = int(input("Eliga un numero [11,25,3,-4,95]: "))

list = [11 ,25, 3, -4, 95]
for i in range(len(list)):
    if list[i] == numseleccionado:
        print("El numero se encuentra en el indice",i)


