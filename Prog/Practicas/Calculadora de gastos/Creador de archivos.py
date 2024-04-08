import random
contador = int(random.randint(0,9999))
print(contador)
archivo = open("archivoprueba%d.csv" % contador,'x')
archivo.write('nombre,apellido,edad\n')
archivo = open('archivoprueba.csv','r')
texto = archivo.read()
archivo.close()
print(texto)
