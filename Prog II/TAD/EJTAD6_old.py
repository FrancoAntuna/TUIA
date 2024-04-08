class Nodo():
    def __init__(self, valor, sig = None):
        self.valor = valor
        self.sig = sig


class ListaEnlazada():
    def __init__(self) -> None:
        self.head = None
        pass

    def __str__(self):
        if self.head:
            iterador = self.head
            while iterador:
                print(iterador.valor)
                iterador = iterador.sig
        pass
    
    def __len__(self):
        n = self.head
        index = 0
        while n.sig:
            n = n.sig
            index = index + 1
        return index

    def insert(self, valor, indice) -> None:
        nuevo_nodo = Nodo(valor)
        if isinstance(indice, int) and indice >= 0 and indice < len(self):
            if indice == 0:
                nuevo_nodo.sig = (self.head)
                self.head = nuevo_nodo
                return
            anterior = self.head
            for i in range(indice - 1):
                anterior = anterior.sig
            siguiente = anterior.sig
            anterior.sig = nuevo_nodo
            nuevo_nodo.sig = siguiente
        else:
            print("error bla bq")
            return
        
    def remove(self, n) -> None:
        if self.head is None:
            return
        else:
            vector = self.head
            vector.sig = None
        pass

    def pop(self) -> None:
        if self.head is None:
            return 
        elif self.head.sig is None:
            # Caso especial: solo hay un elemento en la lista.
            self.head = None
        else:
            n = self.head
            while n.sig.sig is not None:
                n = n.sig
            n.sig = None

    def append(self, signodo) -> None:
        if self.head is None:
            self.head = signodo
        else:
            n = self.head
            while n.sig is not None:
                n = n.sig
            n.sig = signodo
        pass

    def index(self, val):
        if self.head is None:
            return
        else:
            index = 0
            n = self.head
            j = self.head
            while val != n.valor or j.sig is not None:
                n = n.valor
                j = j.sig
                index = index + 1
        return index
    

node = ListaEnlazada()
node.index(2)
node.append(10)
node.pop()
node.append(5)
node.remove(2)
node.insert(10, 1)