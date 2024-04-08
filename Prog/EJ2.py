def orden(num1, num2, num3):
   """
      Recibe 3 valores N1, N2 y N3 que seran ordenados
      y con la funcion sorted se ordena de menor a mayor
      por default. Luego convierte la lsita a una tupla
      utilizando el metodo tuple
   """ 
   bandera = num1
   indice = 0
   list = [num1, num2, num3]
   tupla = tuple(sorted(list))
   return tupla
pass

def divisor(m, n):
   if m%n == 0:
      return True
   else:
      return False
pass



N1 = int(input("Ingrese el primer numero"))
N2 = int(input("Ingrese el segundo numero")) 
N3 = int(input("Ingrese el tercer numero"))

if divisor (N1, N2) == True:
   print ("El segundo numero es divisor del primero")

sumaDivisor = 0
for i in range (1, N3):
   if divisor(N3, i):
      sumaDivisor = sumaDivisor + i
print("La suma de los divisores de",N3,"es",sumaDivisor)   


tuplaOrdenada = orden(N1, N2, N3)

print(type(tuplaOrdenada))
print(tuplaOrdenada)