#metodos
#estructura de las sentencias
# CLASS nombre de la clase:
#       DEF nombre del metodo (SELF):
#           SELF.nombre de la variable = ALGORITMO O VALOR
class Matematica:           #Clase
    def suma (self):        #Metodo
        self.n1 = 2
        self.n2 = 3
s = Matematica ()           #Objeto
s.suma ()
print(s.n1 + s.n2)
