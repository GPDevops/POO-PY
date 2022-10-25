#metodos clase y estaticos - video 12
# def _metodo(self):
# def _metodo(cls):
# def _metodo():

#Una clase es como una plantilla para crear objetos
#Un objeto se crea usando el constructor de una clase
#Una vez que el objeto es creado, se le conoce como una "instancia de la clase"
#hay 3 tipos de metodos: "metodos estaticos", "metodos clase" y "metodos instancia"
#El metodo clase comparte una caracteristica con el metodo estatico
#este metodo puede ser llamado sin crear una instancia de la clase
# @classmethod 

class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    
    def __repr__(self):
        return f"pastel({self.ingredientes !r})"
    
    @classmethod
    def Pastel_chocolate(cls):
        return cls(["harina","leche","chocolate"])
    
    @classmethod
    def Pastel_vainilla(cls):
        return cls(["harina","leche","vainilla"])

print(Pastel.Pastel_chocolate())

#metodo estatico
#@staticmethod
#pueden ser llamados sin tener una instancia de la clase, 
#ademas este tipo de metodo no tiene acceso al exterior
#por lo cual no pueden acceder a ningun otro atributo o llamar 
#a ninguna otra funcion dentro de la clase
import math
class Pastel:
    def __init__(self, ingredientes, tamanio):
        self.ingredientes = ingredientes
        self.tamanio = tamanio
    def __repr__(self):
        return (f"Pastel({self.ingredientes},"f"{self.tamanio})")
    def area(self):
        return self.tamanio_area(self.tamanio)
    
    @staticmethod
    def tamanio_area(A):
        return A ** 2 * math.pi

nuevo_pastel = Pastel(["harina","azucar","leche","crema"], 4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamanio)
print(nuevo_pastel.tamanio_area(1))

        

        