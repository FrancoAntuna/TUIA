class Nodo():
    def __init__(self, valor, sig = None):
        self.valor = valor
        self.sig = sig

class PilaEnlazada():
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if self.head:
            print(self.head.valor)

    def push(self, valor) -> None: #apila un nuevo elemento
        nuevo_nodo = Nodo(valor)
        if self.head:
            nuevo_nodo.sig = self.head
            self.head = nuevo_nodo
        else:
            self.head = nuevo_nodo

    def pop(self) -> int: #elimina y devuelve el ultimo elemento agregado
        if self.head:
            siguiente = self.head
            devuelve = self.head.valor
            self.head = siguiente.sig
            return devuelve

    def isEmpty(self) -> None: #chequea si la pila esta vacia
        if self.head:
            return "La pila no esta vacia"
        else:
            return "La pila esta vacia"

nodo = PilaEnlazada()
nodo.push(10)
nodo.push(20)
nodo.push(30)
print(nodo.pop())
print(nodo.isEmpty())
print(nodo.pop())
print(nodo.isEmpty())
print(nodo.pop())
print(nodo.isEmpty())
