#f-string - video 11
#repaso de format y str.format
#format %

curso = "python"
print("tutoriales de % s"%curso)

nombre = "Victor"
edad = 25
print("Hola soy, % s y tengo % s anios."%(nombre,edad))

#str.format()
nombre = "Ana"
edad = 30
print("Que tal soy {} y mi edad es {} anios.".format(nombre, edad))

#Now f-string
nombre = "Pedro"
edad = 35
print(f"Hola soy {nombre} y mi edad es {edad} anios.")

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    #def __str__(self):              #representacion informal
    def __repr__(self):

        return f"Hola que tal soy {self.nombre} {self.apellido} y tengo {self.edad} anios"

nuevo_estudiante = Estudiante("Victor","Cruz", "17")
#print(f"{nuevo_estudiante}")
print(f"{nuevo_estudiante !r}")     #representacion con los valores tal como son, es decir string, int, etc