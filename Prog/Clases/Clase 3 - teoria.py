#x = int(input("ingrese un numero: "))
#if x > 1:
#    print("HelloWorld")
#else:
#    print("WorldHello")
#
#dia = int(input("Ingrese un dia del 1 al 7: "))
#if 1 <= dia <= 7:
#    if dia == 1:
#        print("Lunes")
#    elif dia == 2:
#        print("Martes")
#    elif dia == 3:
#        print("Miercoles")
#    elif dia == 4:
#        print("Jueves")
#    elif dia == 5:
#        print("Viernes")
#    elif dia == 6:
#        print("Sabado")
#    else:
#        print("Domingo")
#    else:
#        print("error, ingrese un numero valido")

#Determinar o informar el mayor valor de 3 numeros enteros

numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
numero3 = int(input("Ingrese el tercer valor: "))
if numero1 == numero2 == numero3:
    print("Los tres valores son iguales")
elif numero1 < numero2 < numero3:
    print("El mayor valor es", numero3)
elif numero3 < numero2 < numero1:
    print("El mayor valor es", numero1)
else:
    print("El mayor valor es", numero2)

