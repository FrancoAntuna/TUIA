#Hay dos personas con nombres muy largos, pero similares. Se quiere 
#conocer, por un lado, si tienen el mismo tamaño, y por otro lado si 
#son iguales. Ayuda para el programa: buscar la función len

primernombre = str(input("Ingrese el primer nombre: "))
segundonombre = str(input("Ingrese el segundo nombre: "))

largoprimernombre = len(primernombre)
largosegunnombre = len(segundonombre)

mismonombre = primernombre == segundonombre

print("¿Tienen el mismo largo?",largoprimernombre == largosegunnombre,
      "¿Son iguales?",mismonombre)