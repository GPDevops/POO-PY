#metodo constructor __INIT__()

class Persona:
    pass                                    #referencia de que la clase por momento esta vacio
    def __init__(self,nombre,anio):                                 #metodo1
        self.nombre = nombre
        self.anio = anio
    def descripcion(self):                                          #metodo2
        return '{} tiene {} anios'.format(self.nombre,self.anio)
    def comentario(self,frase):                                     #metodo3
        return '{} dice: {}'.format(self.nombre,frase)

doctor = Persona('Jose',26)                                         #definicion del objeto
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario('Hola que tal'))
        