class Nodo():
    def __init__(self, valor, sig=None):
        self.valor = valor
        self.sig = sig


class ListaEnlazada():
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ""
        if self.head:
            iterador = self.head
            result = "["
            while iterador:
                
                result += str(iterador.valor)
                iterador = iterador.sig
                if iterador:
                    result += ", "
            
            result += "]"
        return result
    
    def __len__(self):
        n = self.head
        index = 0
        while n:
            n = n.sig
            index = index + 1
        return index

    def insert(self, valor, indice):
        nuevo_nodo = Nodo(valor)
        if isinstance(indice, int) and 0 <= indice <= len(self):
            if indice == 0:
                nuevo_nodo.sig = self.head
                self.head = nuevo_nodo
            else:
                anterior = self.head
                for i in range(indice - 1):
                    anterior = anterior.sig
                siguiente = anterior.sig
                anterior.sig = nuevo_nodo
                nuevo_nodo.sig = siguiente
        else:
            print("Error: Índice fuera de rango")

    def remove(self, valor):
        if self.head is None:
            return

        if self.head.valor == valor:
            self.head = self.head.sig
            return

        actual = self.head
        while actual.sig and actual.sig.valor != valor:
            actual = actual.sig

        if actual.sig:
            actual.sig = actual.sig.sig

    def pop(self):
        if self.head is None:
            return
        elif self.head.sig is None:
            self.head = None
        else:
            n = self.head
            while n.sig.sig is not None:
                n = n.sig
            n.sig = None

    def append(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            n = self.head
            while n.sig is not None:
                n = n.sig
            n.sig = nuevo_nodo

    def index(self, valor):
        index = 0
        n = self.head
        while n:
            if n.valor == valor:
                return index
            n = n.sig
            index += 1
        return "Error, indice fuera de rango"  # Si no se encuentra el valor, devolver -1


node = ListaEnlazada()
node.append(10)
node.pop()
node.append(5)
node.remove(2)
node.insert(10, 1)
node.insert(4, 0)
node.remove(9)
node.pop()
node.append(10)
node.append(19)
node.insert(4, 19)
print(node.index(2))
print(node.index(10))
print(node.index(1))
print(node)