def ingresarGastos(diccGastos):
    gasto="1"
    monto=1
    accion=4
    while gasto !="0":
        print("--------------------------------------------")
        gasto=str(input("Ingrese el nombre del gasto (ingrese 0 para salir): "))
        print("--------------------------------------------")
        montoTotal=0
        accion=4
        if gasto in diccGastos:
            while accion != 1 and accion != 2 and accion != 3:
                print("--------------------------------------------")
                print("Ya existe el gasto",gasto)
                print("Ingrese (1) para agregar mas montos")
                print("Ingrese (2) para sobreescribirlo por completo")
                print("Ingrese (3) para omitir acciones")
                print("--------------------------------------------")
                accion=int(input("Accion: "))
                if accion != 1 and accion != 2 and accion != 3:
                    print("--------------------------------------------")
                    print("No entendi, ingrese una opcion valida")
        else:
            accion=4
        if gasto !="0":
            monto = 1
            if accion == 1:
                montoTotal=diccGastos[gasto]
                while monto != 0:
                    monto=float(input("Ingrese un monto(ingrese 0 para salir): "))
                    print("--------------------------------------------")
                    if monto != 0:
                        montoTotal=montoTotal+monto
                diccGastos[gasto]=montoTotal
            elif accion == 2 or accion == 4:
                while monto != 0:
                    monto=float(input("Ingrese un monto(ingrese 0 para salir): "))
                    print("--------------------------------------------")
                    if monto == 0:
                        break
                    montoTotal = montoTotal + monto
                diccGastos[gasto]=montoTotal
            elif accion == 3:
                continue
pass

# Programa principal
diccGastos={}
gastos = ingresarGastos(diccGastos)
print(diccGastos)
#total_categoria = calcularTotalPorCategoria(gastos)
#categoria_mayor_monto, mayor_monto = determinarCategoriaMayorMonto(total_categoria)
#gasto_total = calcularGastoTotal(total_categoria)
#mostrarResumenGastos(total_categoria, categoria_mayor_monto, mayor_monto, gasto_total)
#agregarGastosAdicionales("Transporte", "Ocio", Alimentos=200, Entretenimiento=150)
#mostrarGastosIndividuales("Alimentos", "Transporte", Otros=50)