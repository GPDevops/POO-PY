#metodo constructor
from mailbox import NoSuchMailboxError


class Persona:
    pass             #referencia de que por elmomento esta vacio
    def __init__(self,nombre,anio):
        self.nombre = nombre
        self.anio = anio
    def descripcion(self):
        return '{} tiene {} anios'.format(self.nombre,self.anio)
    def comentario(self,frase):
        return '{} dice: {}'.format(self.nombre,frase)

doctor = Persona('Jose',26)
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario('Hola que tal'))
        