#1 Proponga un algoritmo para resolver cada uno de los siguientes problemas

#Dada la base y altura de un rectangulo, informar el area y su perimetro

base = float(input("Ingrese la longitud de la base en centimetros "))
altura = float(input("Ingrese la longitud de la altura en centimetros "))

area = base * altura
perim = base * 2 + altura * 2

print("El rectangulo de base",base,"cm y altura",altura,"cm, tiene un perimetro de", perim,"cm2 y una area total de",area,"cm3" )



