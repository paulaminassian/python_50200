class Clientes:
    def __init__ (self, nombre, apellido, dni): #  edad, telefono, estado_civil, productos)
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.compras = []
    
    def __str__(self):
        return f'Datos del Cliente: Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}'
    
    def comprar(self, producto, cantidad):
        compra_actual = {'producto': producto, 'cantidad': cantidad}
        self.compras.append(compra_actual)
        print(f'{cantidad} unidades de {producto} compradas. Gracias por su compra.')
    
    def reclamos(self, motivo):
        print(f'Su reclamo ha sido registrado. Motivo: {motivo}. Nos pondremos en contacto con usted pronto.')


