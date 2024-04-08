class Vector:
    def __init__(self, dimension):
        self.vector = [0] * dimension
        self.dimension = dimension
    
    def get(self, posicion):
        if 1 <= posicion <= self.dimension:
           return self.vector[posicion - 1]
        return None
    
    def put(self, valor, posicion):
        if 1 <= posicion <= self.dimension:
            self.vector[posicion - 1] = valor
            return valor
        return None
    
    def __add__(self, other):
        if self.dimension != other.dimension:
           
            return None
        resultado = Vector(self.dimension)
        for i in range(1, self.dimension + 1):
            suma = (self.get(i) + other.get(i))
            resultado.put(i, suma)

            

        
A = Vector(3)
A.put(1, 1)
A.put(2, 2)
A.put(3, 3)

B = Vector(3)
B.put(1, 1)
B.put(2, 2)
B.put(3, 3)