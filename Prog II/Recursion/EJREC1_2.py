def repite_hola(n: int):
    if n >= 0:
        print("Hola")
        return repite_hola(n-1)
pass

def repite_hola_concatenado(n:int) -> str:
    if n >= 0:
        return "Hola" + repite_hola_concatenado(n-1)
    return ''
pass

n = int(input("Ingrese n "))
repite_hola(n)
print(repite_hola_concatenado(n))