#Herencia: Permite crear una nueva clase a partir de una o mas clases existentes
#class NombreSubClase (NOMBRECLASESUPERIOR):
#class CLASEBASE:
#   Cuerpo de la clase base
#class DerivadoClase (CLASEBASE):
#    Cuerpo de la clase derivada
class Pokemon:                      #Clase padre
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre, self.tipo)
class pikachu(Pokemon):             #Clase hija
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre,tipoataque)
class charmander(Pokemon):          #Clase hija
    def ataque(self,tipodefensa):
     return '{} tipo de defensa: {}'.format(self.nombre,tipodefensa)

nuevo_pokemon = pikachu('Boby','electrico')
nuevo_pokemon2 = charmander('Dragon','Defensor')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('ataque trueno'))
print(nuevo_pokemon2.descripcion())
print(nuevo_pokemon2.ataque('Defensa lateral'))



