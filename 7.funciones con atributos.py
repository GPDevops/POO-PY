#funciones para obtener atributos: getattr, hasattr, setattr, delattr
class Persona:
    edad = 27
    nombre = "Victor"
    pais = "Brasil"      #atributo a borrarse con la funcion delattr

doctor = Persona ()

print("La edad es: ", doctor.edad)
print("La edad es: ", getattr(doctor, 'edad'))  #1ra funcion getattr
print('El doctor tiene como parametro edad?: ', hasattr(doctor,'edad')) ##2da funcion hasattr
print('El doctor tiene como parametro apellido?: ', hasattr(doctor,'apellido')) ##2da funcion hasattr con atributo inexistente

print("Antes era: ", doctor.nombre)
setattr(doctor, 'nombre', 'Gonzalo')    #3ra funcion setattr para cambio de valores de los atributos
print("Ahora es: ", doctor.nombre)

delattr(Persona,'pais')             #4ta funcion delattr borra el atributo pais de la clase Persona