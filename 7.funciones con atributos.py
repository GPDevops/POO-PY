#!
#funciones para atributos
class Persona:
    edad = 27
    nombre = "Victor"

doctor = Persona ()

print("La edad es: ", doctor.edad)
print("La edad es: ", getattr(doctor, 'edad'))  #1ra funcion getattr
print('El doctor tiene una edad: ', hasattr(doctor,'edad')) ##2da funcion hssattr
print('El doctor tiene una edad: ', hasattr(doctor,'apellido')) ##2da funcion hasattr con atributo inexistente

print("Antes era: ", doctor.nombre)
setattr(doctor, 'nombre', 'Gonzalo')
print("Ahora es: ", doctor.nombre)

