#Supongamos que una heladera te contrata para crear un programa que les
#ayude a llevar el control de ventas diarias. Para ello, se te pide qe desarrolles
#un programa que realice las siguientes tareas

#1- Ingrese los sabores de helados que se vendieron durante el dia y la cantidad de
#unidades vendidas de cada sabor

#2- Calcule el total de ventas para cada sabor de helado
#3- Determine el sabor de helado mas vendido y la cantidad de unidades vendidas
#4- Determine cuantas unidades de helado se vendieron en total durante el dia 
#5- Muestre los resultados de la venta en un formato legible para el usuario

def ventas(diccVentas):
    opcion = str(input("Desea registrar una venta? Y/N "))
    while opcion.upper() != "Y" and opcion.upper() != "N":
        opcion = str(input("No entendi, desea registrar una venta? Y/N "))
    while opcion.upper() == "Y":
        sabor = str(input("Ingrese el sabor: "))
        if sabor not in diccVentas:
            cantidad = int(input("Ingrese la cantidad vendida: "))
            diccVentas[sabor] = cantidad
        else:
            modificar = str(input("Ya se registro una venta de este sabor, desea sumar unidades? Y/N "))
            if modificar.uppder() == "N":
                cantidad = int(input("Ingrese la cantidad: "))
                diccVentas[sabor] = diccVentas[sabor] + cantidad
        opcion = str(input("Desea registar otra venta? Y/N "))
        while opcion.upper() != "Y" and opcion.upper() != "N":
            opcion = str(input("No entendi, desea registrar una venta? Y/N "))

pass


def masVendido(diccVentas):
    if not diccVentas:
        print("No hay ventas registradas")
        return
    listaVentas = list(diccVentas)
    listaCantidades = list(diccVentas.values())
    mayor = 0
    for i in range(len(listaVentas)):
        if listaCantidades[i] > mayor:
            mayor = listaCantidades[i]
            mayorHelado = listaVentas[i]
    print("El helado mas vendido fue",mayorHelado,"con",mayor,"unidades vendidas")
pass

def total(diccVentas):
    if not diccVentas:
        print("No hay ventas registradas")
        return
    listaCantidades = list(diccVentas.values())
    sumaCantidades = 0
    for i in range(len(listaCantidades)):
        sumaCantidades = sumaCantidades + listaCantidades[i]
    print("El total vendido es de",sumaCantidades,"unidades")
pass

pass

def escribirVentas(diccVentas):
    if not diccVentas:
        print("No hay ventas registradas")
        return
    print("Sabor : Ventas")
    listaClaves = list(diccVentas)
    for i in range(len(diccVentas)):
        print(listaClaves[i],":",diccVentas[listaClaves[i]])
pass

def menu():
    print("")
    print("--------------------------------")
    print("1) Registrar o modificar ventas")
    print("2) Desplegar lista de ventas")
    print("3) Sabor mas vendido")
    print("4) Unidades totales vendidas")
    print("5) Imprimir resumen")
    print("--------------------------------")
    print("")
    opcion = int(input("Ingrese una opcion, o ingrese 0 para salir "))
    return opcion
pass

def principal():
    opcion = menu()
    diccVentas = {}
    while opcion != 0:
        if opcion == 1:
            ventas(diccVentas)
            opcion = menu()
        elif opcion == 2:
            escribirVentas(diccVentas)
            opcion = menu()
        elif opcion == 3:
            masVendido(diccVentas)
            opcion = menu()
        elif opcion == 4:
            total(diccVentas)
            opcion = menu()
        elif opcion == 5:
            escribirVentas(diccVentas)
            print("")
            print("")
            masVendido(diccVentas)
            print("")
            print("")
            total(diccVentas)
            opcion = menu()
        else:
            if opcion != 0:
                print("No entendi, por favor ingrese una opcion valida")
                opcion = menu()
pass

principal()