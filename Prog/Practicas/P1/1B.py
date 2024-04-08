#Calcular la nota final de un alumno que se obtiene de promediar las 3 notas de sus parciales

primernota = float(input("Ingrese la primer nota del alumno "))
segundanota = float(input("Ingrese la segunda nota del alumno "))
tercernota = float(input("Ingrese la tercer nota del alumno "))

promedionota = (primernota + segundanota + tercernota)/3

print("La nota final es","{0:.2f}".format(promedionota))

