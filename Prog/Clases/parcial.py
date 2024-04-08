nota=int(input("Ingrese la nota: "))

if nota < 6:
    print("Desaprobado")
elif nota < 0:
    print("Nota incorrecta")
elif nota>10:
    print("Nota incorrecta")
else:
    print("Aprobado")