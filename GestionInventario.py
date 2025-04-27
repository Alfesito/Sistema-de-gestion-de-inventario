from Pool import Pool
from Producto import Producto

class GestionInventario:
    SELECCIONAR_PRODUCTOS = "SELECT * FROM productos"
    INSERTAR_PRODUCTO = "INSERT INTO productos (nombre, precio, cantidad, categoria) VALUES (%s, %s, %s, %s)"
    ACTUALIZAR_PRODUCTO = "UPDATE productos SET nombre = %s, precio = %s, cantidad = %s, categoria = %s WHERE id = %s"
    ELIMINAR_PRODUCTO = "DELETE FROM productos WHERE id = %s"
    BUSCAR_PRODUCTO_NOMBRE = "SELECT * FROM productos WHERE nombre = %s"
    BUSCAR_PRODUCTO_CATEGORIA = "SELECT * FROM productos WHERE categoria = %s"

    @classmethod
    def seleccionar_productos(cls):
        conexion = None
        try:
            conexion = Pool.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR_PRODUCTOS)
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])
                productos.append(producto)
            return productos
        except Exception as err:
            print(f"Error: {err}")
        finally:
            if conexion is not None:
                cursor.close()
                Pool.liberar_conexion(conexion)

    @classmethod
    def insertar_producto(cls, producto):
        conexion = None
        try:
            conexion = Pool.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.precio, producto.cantidad, producto.categoria)
            cursor.execute(cls.INSERTAR_PRODUCTO, valores)
            conexion.commit()
            print(f"Producto insertado: {producto}")
        except Exception as err:
            print(f"Error: {err}")
        finally:
            if conexion is not None:
                cursor.close()
                Pool.liberar_conexion(conexion)

    @classmethod
    def actualizar_producto(cls, producto):
        conexion = None
        try:
            conexion = Pool.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.precio, producto.cantidad, producto.categoria, producto.id)
            cursor.execute(cls.ACTUALIZAR_PRODUCTO, valores)
            conexion.commit()
            print(f"Producto actualizado: {producto}")
        except Exception as err:
            print(f"Error: {err}")
        finally:
            if conexion is not None:
                cursor.close()
                Pool.liberar_conexion(conexion)

    @classmethod
    def eliminar_producto(cls, producto):
        conexion = None
        try:
            conexion = Pool.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.id,)
            cursor.execute(cls.ELIMINAR_PRODUCTO, valores)
            conexion.commit()
            print(f"Producto eliminado: {producto}")
        except Exception as err:
            print(f"Error: {err}")
        finally:
            if conexion is not None:
                cursor.close()
                Pool.liberar_conexion(conexion)

    @classmethod
    def buscar_producto(cls, tipo_busqueda, valor):
        conexion = None
        try:
            conexion = Pool.obtener_conexion()
            cursor = conexion.cursor()
            
            if tipo_busqueda == "nombre":
                consulta = cls.BUSCAR_PRODUCTO_NOMBRE
            elif tipo_busqueda == "categoria":
                consulta = cls.BUSCAR_PRODUCTO_CATEGORIA
            else:
                raise ValueError("Tipo de búsqueda no válido. Usa 'nombre' o 'categoria'.")

            cursor.execute(consulta, (valor,))
            registros = cursor.fetchall()
            
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])
                productos.append(producto)
                
            return productos

        except Exception as err:
            print(f"Error: {err}")
        finally:
            if conexion is not None:
                cursor.close()
                Pool.liberar_conexion(conexion)

if __name__ == "__main__":
    # Ejemplo de uso
    gestion_inventario = GestionInventario()
    
    # Insertar un producto
    # nuevo_producto = Producto(None, "Producto A", 10.99, 100, "Categoria 1")
    # gestion_inventario.insertar_producto(nuevo_producto)
    
    # Seleccionar todos los productos
    productos = gestion_inventario.seleccionar_productos()
    for producto in productos:
        print(producto)
    
    # Actualizar un producto
    if productos:
        producto_a_actualizar = productos[0]
        producto_a_actualizar.precio = 200.0
        gestion_inventario.actualizar_producto(producto_a_actualizar)
    
    # Buscar un producto por nombre
    resultado_busqueda = gestion_inventario.buscar_producto("nombre", "Producto A")
    for producto in resultado_busqueda:
        print(producto)
    
    # Eliminar un producto
    # if productos:
    #     producto_a_eliminar = productos[2]
    #     gestion_inventario.eliminar_producto(producto_a_eliminar)
