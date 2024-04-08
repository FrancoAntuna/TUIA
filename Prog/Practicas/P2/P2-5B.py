#se tiene una multitud afuera, cada persona le dirá su nombre a cada 
#otra persona en la multitud. Se quiere saber cuánto tiempo llevará 
#hacer esto, dado que decir una vez tu nombre lleva aproximádamente 
#4 segundos y medio.

cantidadpersonas = float(input("Ingrese la cantidad de personas: "))
tiempodemorado = cantidadpersonas*4.5 #se sabe por datos de ingreso que se demora 4.5s por persona
print("Se demoraria un tiempo de ",tiempodemorado,"s")