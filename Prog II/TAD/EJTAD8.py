class Pila():
    def __init__(self,):
        self.valores = []

    def __str__(self):
        if not self.valores:
            return "Pila vacia"

        else:
            return str(self.valores[0])


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




nodo = Pila()
nodo.push(10)
nodo.push(20)
nodo.push(30)
print(nodo.pop())
nodo.isEmpty()
print(nodo.pop())
nodo.isEmpty()
print(nodo.pop())
nodo.isEmpty()
print(nodo.pop())