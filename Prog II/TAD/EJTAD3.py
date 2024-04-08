from typing import Any

class ConjuntoMatematico:
    def __init__(self, conjunto):
        self.conjunto = conjunto
    
    def see(self) -> Any:
        return self.conjunto
    
    def existElement(self, element) -> bool:
        return element in self.conjunto


lista = [1, 5, 6, 3, 6, 7, 5, 2, 0]
conj = ConjuntoMatematico(lista)
print(conj.see())
print(conj.existElement(5))