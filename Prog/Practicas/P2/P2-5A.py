#Se tienen dos habitaciones dentro de un hogar, cada una con temperatura
#ambiente. Se requiere saber a que temperatura estaran las habitaciones
#dado suficiente tiempo para que se trasnmita el calor de una a la otra.
#Se conoce que en este caso es valido promediar temperaturas

temperatura1 = float(input("Ingrese la temperatura de una habitacion: "))
temperatura2 = float(input("Ingrese la temperatura de la otra habitacion: "))

promediotemperatura = (temperatura1 + temperatura2)/2 #siendo 2 la cantidad de habitaciones

print("La temperatura final de ambas habitaciones sera de",promediotemperatura,"°")
