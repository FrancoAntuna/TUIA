import datetime


def ingreso_datos(listaDatos):

    bandera = 1
    while bandera != 0:
        datosPersonas = []
        datosPersonas.append(str(input("Ingrese el nombre: ")))
        datosPersonas.append(str(input("Ingrese el apellido: ")))
        datosPersonas.append(str(input("Ingrese la localidad: ")))
        datosPersonas.append(int(input("Ingrese la edad: ")))
        datosPersonas.append(int(input("Ingrese el DNI: ")))
        datosPersonas.append(str(input("Ingrese la carrera: ")))
        datosPersonas.append(int(input("Ingrese el año de inicio: ")))
        listaDatos.append(datosPersonas)
        print(listaDatos)
        bandera = int(input("1 para ingresar otra persona, 0 para salir: "))

pass

def calculo_años(listaDatos):
    anio = 2023
    for i in range(len(listaDatos)):
        listaCalculo = listaDatos[i]
        calculo = anio - listaCalculo[6]
        listaCalculo.append(calculo)
        listaDatos[i] = listaCalculo
        print(listaDatos[i])

pass


listaDatos = []
ingreso_datos(listaDatos)
calculo_años(listaDatos)