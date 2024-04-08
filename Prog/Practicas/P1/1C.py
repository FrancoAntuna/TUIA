#Calcular la distancia de dos puntos en el plano
import math

xprimerpunto = float(input("Ingrese la coordenada X del primer punto "))
yprimerpunto = float(input("Ingrese la coordenada Y del primer punto "))

xsegundopunto = float(input("Ingrese la coordenada X del segundo punto "))
ysegundopunto = float(input("Ingrese la coordenada Y del segundo punto "))

distancia = math.sqrt(((xsegundopunto - xprimerpunto)**2)+((ysegundopunto - yprimerpunto)**2))

print("La distancia entre los dos puntos es","{0:.2f}".format(distancia))
