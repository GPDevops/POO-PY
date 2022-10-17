#metodos 2 utilizando la funcion INIT (constructor)
class Ropa:
    def __init__(self):                 #Doble rayita baja __INIT__ Doble rayita baja
        self.marca = "Brand1"
        self.talla = "M"
        self.color = "rojo"
camisa = Ropa()
print(camisa.talla)
print(camisa.marca)