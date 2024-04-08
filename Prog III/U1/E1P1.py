"""Cruce de río con pesos
Tres personas A, B, C y D un bote se encuentran en la misma orilla de un río. El río se
puede cruzar únicamente en bote y debe haber al menos una persona a bordo para
poder navegarlo. El bote tiene una capacidad de kg y bajo ningún motivo se puede
exceder. Los pesos de las personas son: 100, 60 y 40 kg para A, B y C,
respectivamente. El objetivo es que todas las personas lleguen al otro lado del río en el
menor número de cruces.
1. Formular este problema como un problema de búsqueda.
2. Graficar el espacio de estados y hallar una solución óptima. ¿Cuántos estados son
alcanzables?"""

"""
Universo de estados:
    (A, B, C, D) ∈ {0, 1}

    Los estados representan 0 si esta del lado derecho o 1 si esta del lado izquierdo

Estado inicial:
    (A, B, C, D) ∈ {0, 1} / A = B = C = D = 0

Posibles estados objetivos:
    (A, B, C, D) ∈ {0, 1} / A = B = C = D = 1
    (A, B, C, D) ∈ {0, 1} / A = B = C = 1 & D = 0


Univeso de acciones:
    P(A, B, C) = A*100 + B*60 * C*40 <= 100

Modelo de transicion
    resultado(S,A) = resultado((A, B, C, D) ∈ {0, 1},   Si A = 1 -> peso(A) = 100
                                                        Si B = 1 -> peso(B) = 60
                                                        Si C = 1 -> peso(C) = 40
                                                        Si D = 1 -> peso(A) + peso(B) + peso(C) < 100)

Test objetivo
    (A, B, C, D) ∈ {0, 1} / A = B = C = 1

Costos de caminos
    C = 1 V U(acciones)







"""
class Persona:

    def __init__ (self,nombre):
        self.nombre = nombre

class Bote:
    def __init__(self,bote,pasajero = None):
        self.bote = bote
        self.pasajero = pasajero

A = Persona("A")
B = Persona("B")
C = Persona("C")

bote = Bote("D")

