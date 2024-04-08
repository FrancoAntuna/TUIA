from typing import Any

class Celda:
    def __init__(self):
        self.valor = None
    
    def see(self) -> Any:
        return self.valor
        
    def exist(self) -> bool:
        return self.valor is not None

    def remove(self) -> None:
        self.valor = None
    
    def asign(self, valor: Any) -> None:
        self.valor = valor

        



cel = Celda()
cel.asign(1)
print(cel.exist())
print(cel.see())
cel.remove()
print(cel.exist())




    

