#herencia multiple - video10
#Se refiere a la posibildad de crear una clase a partir de multiples clase superiores
#class Base_uno:
#       pass
#class Basae_dos:
#       pass
#class DerivadoMultiple(Base_uno, Base_dos):
#       pass

#herencia multinivel
#Las caracteristicas de la clase base y la clase derivada se heredan en la nueva clase derivada

#class Base:
#       pass
#class derivado-uno(Base):
#       pass
#class derivado-dos(Derivado-uno):
#       pass

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("llamando...")
    def ocupado(self):
        pass
    def fotografia(self):
        print("tomando fotos..")

class Camara:
    def __init__(self):
        pass

class Reproduccion:
    def __init__(self):
        pass
    def reproducciondemusica(self):
        print("reproduciendo musica..")
    def reproducirvideo(self):
        print("reproducir un video..")

class smartphone(Telefono, Camara, Reproduccion):
    def __del__(self):                          #constructor para limpiar los recursos
        print("telefono apagado")

movil = smartphone()
#print(dir(movil))
print(movil.fotografia())
print(movil.llamar())