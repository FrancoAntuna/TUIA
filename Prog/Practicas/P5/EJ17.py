# Dado un diccionario donde la clave es el DNI (formato cadena) y el valor es la 
#cantidad de dosis de vacunas contra el covid, filtrar del mismo las personas que 
#tienen 2 dosis y guardarlas en la estructura de datos que crea conveniente. Esta 
#información será uilizada para recordarles que ya tienen disponible
#la tercera dosis.

listaVacunados = {}
i = 1
while i != 0:
    dni = str(input("Ingrese el DNI de la persona o 0 para salir: "))
    if dni == "0":
        break
    dosis = int(input("Ingrese la cantidad de Dosis: "))
    listaVacunados[dni] = dosis

listaNombres = list(listaVacunados)
listaDosis = list(listaVacunados.values())
for i in range(len(listaVacunados)):
    if listaDosis[i] == 2:
        print("DNI N:",listaNombres[i],"ya tiene disponible la 3ra dosis")