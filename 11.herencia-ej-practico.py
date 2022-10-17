#Herencia ejercicio practico 
#Realizar una calculadora con 4 las operaciones basicas
print("####### OPERACIONES BASICAS ######")
class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    def ingresardato(self):
        self.datos = [int(input("Ingresar dato "  +str(i+1) + " = ")) for i in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    def suma(self):
        a,b, = self.datos
        s = a + b
        print("El resultado de la suma es: ", s)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    def cuadrada(self):
        import math
        a, = self.datos
        print("El resultado de la raiz es: ", math.sqrt(a))

ejemplo = op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.suma())

ejemplo2 = raiz()
print(ejemplo2.ingresardato())
print(ejemplo2.cuadrada())

