class Producto:
    def __init__(self, id, nombre, precio, cantidad, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def __str__(self):
        return f"Id: {self.id}, Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Categoria: {self.categoria}"