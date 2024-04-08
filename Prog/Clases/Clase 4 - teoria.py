lado1 = float(input("Ingrese el primer lado del triangulo: "))
lado2 = float(input("Ingrese el segundo lado del triangulo: "))
lado3 = float(input("Ingrese el tercer lado del triangulo "))

if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
    print("Los datos ingresados no corresponden a un triangulo")
elif lado1 == lado2 == lado3:
    print("El triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")