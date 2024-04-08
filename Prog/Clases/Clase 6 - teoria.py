#Menu
#Crear contacto
#Modificar contacto
#Eliminar contacto

def menu():
    print("Elija una opcion")
    print("1) Crear contacto")
    print("2) Modificar contacto")
    print("3) Eliminar contacto")
    print("4) Mostrar agenda")
    print("0) Para salir del programa")
    opcion = int(input())
    return opcion
pass


def crearContacto(diccAgenda):
    nombre = str(input("Ingrese el nombre del contacto "))
    if nombre in diccAgenda:
        yn = "Y"
        while yn != "Y" or yn != "N":
            yn = str(input("El contacto ya existe, desea reemplazarlo? Y/N "))
            if yn.upper() == "Y":
                telefono = int(input("Ingrese el telefono "))
                diccAgenda[nombre] = telefono
                print("El contacto",nombre,"se guardo exitosamente con el telefono",diccAgenda[nombre])
                break
            elif yn.upper() == "N":
                yn = str(input("De acuerdo, el contacto no sera modificado, presione enter para volver al menu principal "))
                break
            else:
                print("Perdon, no entendi")
    else:
        telefono = int(input("Ingrese el telefono "))
        diccAgenda[nombre] = telefono
        print("El contacto",nombre,"se guardo exitosamente con el telefono",diccAgenda[nombre])
pass

def modificarContacto(diccAgenda):
    i = 0
    while i == 0:
        nombre = str(input("Ingrese el contacto que desea modificar o presione 0 para salir "))
        if nombre in diccAgenda:
            telefono = int(input("Ingrese el nuevo telefono "))
            diccAgenda[nombre] = telefono
            print("El contacto",nombre,"se sobreescribio exitosamente con el telefono",diccAgenda[nombre])
            break
        elif nombre == "0":
            i = 1
        else:
            print("El nombre ingresado no pertenece a un contacto ")
pass

def eliminarContacto(diccAgenda):
    nombre = str(input("Ingrese el contacto a eliminar "))
    if nombre in diccAgenda:
        diccAgenda.pop(nombre)
        print("Contacto",nombre,"eliminado")
    else:
        print("El nombre ingresado no pertenece a un contacto ")
pass

def escribirAgenda(diccAgenda):
    print("Contacto : Telefono")
    listaClaves = list(diccAgenda)
    for i in range(len(diccAgenda)):
        print(listaClaves[i],":",diccAgenda[listaClaves[i]])
pass

def principal():
    diccAgenda = {"Jose":"156123123", "Maria":"156321321", "Franco":"3415856338"}
    opcionSel = menu()
    while opcionSel !=0:
        if opcionSel == 1:
            crearContacto(diccAgenda)
            opcionSel = menu()
        elif opcionSel == 2:
            modificarContacto(diccAgenda)
            opcionSel = menu()
        elif opcionSel == 3:
            eliminarContacto(diccAgenda)
            opcionSel = menu()
        elif opcionSel == 4:
            escribirAgenda(diccAgenda)
            opcionSel = menu()
        else:
            print("No entendi")
            opcionSel = menu()

principal()