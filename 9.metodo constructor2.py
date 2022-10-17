#metodo constructor2
#modificar un atributo

class Email:
    pass             #referencia de que la clase por momento esta vacio
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)
