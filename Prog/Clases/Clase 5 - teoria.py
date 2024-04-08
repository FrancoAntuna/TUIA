palabra = input("Ingrese una palabra: ")
j = len(palabra) - 1
for i in range(len(palabra)):
    print("Indice actual:", j, "  Letra actuak:", palabra[j])
    j = j - 1
