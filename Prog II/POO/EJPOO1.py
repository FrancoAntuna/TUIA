class Dinero:
    """
    Concepto abstracto que no deberemos instanciar nunca directamente
    """
    def monto(self) -> float:
        """
        Todo dinero, cualquiera sea su procedencia, debería proveernos
        con algún metodo de saber cuál es el monto que este representa.

        Este método retorna un flotante con el valor total real que cada
        instancia tiene dentro.

        Será más claro cuando lo veamos en la práctica.
        """
    pass

    def __str__(self) -> str:
        """
        Por completitud, y para corroborar nuestros programas,
        nos gustaría que todas las clases que deriven Dinero
        tengan alguna forma de representación por pantalla.
        """
        pass


class Moneda(Dinero):

    Denominaciones = { 1, 2, 5 }

    def __init__(self, denominacion:int):
        if denominacion in Moneda.Denominaciones:
            self.denominacion = denominacion
        else:
            print("Error en la construccion, denominacion invalida")
        pass

    def monto(self) -> float:
        pass

    def __str__(self) -> str:
        return "La moneda tiene una denominacion de " + str(self.denominacion)

moneda1 = Moneda(1)
print(moneda1)
moneda2 = Moneda(2)
print(moneda2)
moneda5 = Moneda(5)
print(moneda5)
monedafalsa= Moneda(3)