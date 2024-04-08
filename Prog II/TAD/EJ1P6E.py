import itertools

class Pila():
    def __init__(self):
        self.valores = []

    def __str__(self):
        if not self.valores:
            return "Pila vacia"

        else:
            return str(self.valores)


    def push(self, valor):
        self.valores.append(0)
        for i in range(len(self.valores)-1, 0, -1):
            self.valores[i] = self.valores[i-1]
        self.valores[0] = valor


    def pop(self):
        if not self.valores:
            print("Pila vacia")
            return False
        else:
            devuelve = self.valores[0]
            for i in range(len(self.valores)-1):
                self.valores[i] = self.valores[i+1]
            self.valores.pop()
            return devuelve


    def isEmpty(self):
        if not self.valores: 
            
            print("Pila vacia")
            return True
        else:
            print("Existen elementos en la pila")
            return False


def RangePila(cantidad):
    rango = Pila()
    SumadorPila(rango, cantidad)
    return rango
pass

def SumadorPila(rango, cantidad):
    if cantidad != 0:
        rango.push(cantidad)
        return SumadorPila(rango, cantidad - 1)
    return
pass

"""
def ContadorRangePila():

pass
"""

cant = int(input("Ingrese valor"))
Rango = RangePila(cant)
print(Rango)

