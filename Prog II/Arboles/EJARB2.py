class Tree:
    def __init__(self, cargo, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
    
    def __str__(self):
        return "|" + str(self.cargo) + " " + str(self.left)+ " " + str(self.right) + "|"
        pass

    def nodos(self,cantR = 0, cantL = 0)  -> int:
        if self.left == None and self.right == None:
            return (cantR + cantL + 1)
        cantR = self.right.nodos()
        cantL = self.left.nodos()
        return (cantR + cantL + 1)
        pass

    def menor_mayor(self, 
                    mayorR = float("-inf"), menorR = float("inf"), 
                    mayorL = float("-inf"), menorL = float("inf")): # -> tuple(int, int):

        if self.left != None:
            mayorL, menorL = self.left.menor_mayor()
        if self.right != None:
            mayorR, menorR = self.right.menor_mayor()
        mayor = max(self.cargo, mayorL, mayorR)
        menor = min(self.cargo, menorL, menorR)
        return (mayor, menor)

    def buscar(self, element: any, respuesta = None) -> bool:
        if element == self.cargo:
            return True
        if self.left != None:
            respuesta = self.left.buscar(element)
            if respuesta != None:
                return True
        if self.right != None:
            respuesta = self.left.buscar(element)
            if respuesta != None:
                return True
        if respuesta == True:
            return "Existe"
        else:
            return "No existe"
        
        
        pass

    def altura(self) -> int:
        pass

arbol = Tree(1, Tree(2, Tree(4), Tree(6)), Tree(3, Tree(5), Tree(7)))
print(arbol)
print(arbol.nodos())
print(arbol.menor_mayor())
print(arbol.buscar(7))


