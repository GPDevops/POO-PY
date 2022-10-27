#poliformismo
#sobrecarga de metodos - posibilibidad que uan subclase cuente con metodos del mismo nombre
#la clase superior define comportamientos
#poliformismo viene del griego poli=muchas y morfismo = formas
#Poliformismo es la capacidad que tienen los objetos en diferentes clases para usar un comportamiento
# o atributo del mismo nombre pero con diferente valor
from mailbox import NoSuchMailboxError


class Auto:
    rueda = 4
    def desplazamiento(self):
        print("El auto se esta moviendo sobre 4 ruedas")

class Moto:
    rueda = 2
    def desplazamiento(self):
        print("La moto se esta moviendo sobre 2 ruedas")

class Animales:
    def __init__(self, nombre):
        self.nombre = nombre
    def tipo_animal(self):
        pass
class Leon(Animales):
    def tipo_animal(self):
        print("animal salvaje")

class Perro(Animales):
    def tipo_animal(self):
        print("animal domestico")

nuevo_animal = Leon("Simba")
nuevo_animal.tipo_animal()

nuevo_animal2 = Perro("Bobby")
nuevo_animal2.tipo_animal()