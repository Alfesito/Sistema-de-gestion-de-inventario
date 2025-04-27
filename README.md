# Sistema-de-gestion-de-inventario

## Enunciado de la Práctica

### Descripción
Crear un programa en Python que simule un sistema de gestión de contactos. El programa debe permitir a los usuarios realizar las siguientes acciones:

1. **Agregar un contacto**: Permite al usuario agregar un contacto a la lista de contactos. Los contactos deben tener atributos como nombre, número de teléfono y correo electrónico.
2. **Mostrar todos los contactos**: Muestra una lista de todos los contactos disponibles.
3. **Buscar un contacto**: Permite al usuario buscar un contacto por nombre.
4. **Eliminar un contacto**: Permite al usuario eliminar un contacto de la lista.

### Requisitos

1. Utiliza clases para representar los contactos y el sistema de gestión de contactos.
2. Implementa métodos para agregar, mostrar, buscar y eliminar contactos.
3. Utiliza estructuras de control y ciclos para manejar la interacción con el usuario.
4. Utiliza manejo de archivos para guardar y cargar la lista de contactos en un archivo de texto.
5. Implementa gestión de errores para manejar situaciones como:
   - Intentar agregar un contacto con un formato de correo electrónico inválido.
   - Intentar buscar o eliminar un contacto que no existe.
   - Manejo de errores al leer o escribir en el archivo.

### Instrucciones

1. Crea una clase `Contacto` con atributos para el nombre, número de teléfono y correo electrónico.
2. Crea una clase `GestionContactos` que contenga una lista de contactos y métodos para agregar, mostrar, buscar y eliminar contactos.
3. Implementa un menú que permita al usuario seleccionar una acción (agregar, mostrar, buscar o eliminar un contacto).
4. Utiliza un archivo de texto para guardar la lista de contactos y carga los datos al iniciar el programa.
5. Implementa validaciones para asegurar que el formato del correo electrónico es válido y que los campos requeridos no están vacíos.
6. Implementa manejo de excepciones para capturar y manejar errores relacionados con el archivo y las operaciones de contacto.

##x# Entrega
Los estudiantes deben entregar el código fuente del programa junto con un archivo de texto que contenga algunos contactos de ejemplo.

--------------------------------------------------------------------------------

# Pasos seguidos

## 1. Backend

### 1.1. Creación de clase Producto

Creamos la clase producto con el constructor y el método __str__. Los parámetros utilizados son:
    - Id : int
    - Nombre : string
    - Precio : float
    - Cantidad : int
    - Categoria : string

### 1.2. Creación de base de datos de gestion de inventario

Creamos la base de datos en mysql con los parámetros de la clase Producto como columnas.

> create database gestion_inventario;
> use gestion_inventario;
> create table productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio FLOAT NOT NULL,
    cantidad INT NOT NULL,
    categoria VARCHAR(50)
);
> INSERT INTO productos (nombre, precio, cantidad, categoria) 
VALUES ('Laptop Lenovo', 799.99, 10, 'Electrónica');
> INSERT INTO productos (nombre, precio, cantidad, categoria) 
VALUES ('Camiseta Nike', 29.99, 50, 'Ropa');
> INSERT INTO productos (nombre, precio, cantidad, categoria) 
VALUES ('Cafetera Philips', 89.50, 20, 'Electrodomésticos');

### 1.3. Creación de la clase Pool

Con esta clase Pool queremos relizar un proxy entre la base de datos y Gestión de Inventarios (DAO). Se han creado los siguientes métodos de clase:
    - obtener_pool
    - obtener_conexion
    - liberar_conexion

### 1.4. Creación de las clase GestionInventario

La clase GestionInventario es la encargada de los métodos para agregar, mostrar, buscar, actualizar y eliminar productos de la base de datos, especificando, los metedos que se van a utlizar en la aplicación son:
    - Listar todos los productos:
        SELECT * FROM productos
    - Agregar productos:
        INSERT INTO productos (nombre, precio, cantidad, categoria) VALUES (%s, %s, %s, %s)
    - Actualizar productos:
        UPDATE productos SET nombre = %s, precio = %s, cantidad = %s, categoria = %s WHERE id = %s
    - Eliminar productos:
        DELETE FROM productos WHERE id = %s
    - Buscar productos según su nombre y su categoria:
        SELECT * FROM productos WHERE nombre = %s
        SELECT * FROM productos WHERE categoria = %s

## Frontend
El Frontend se ha realizado con Flask y Bootstrap. Se ha creado un archivo App.py para la parte de Flask y un index.html para la interfaz gráfica web donde el usuario puede realizar las distintas acciones:

### 1. **`/` - `index()`**
   - Muestra todos los productos.

### 2. **`/agregar` - `agregar()`**
   - Agrega un nuevo producto a la base de datos.
   - **Método**: `POST`

### 3. **`/actualizar/<int:id>` - `actualizar(id)`**
   - Actualiza un producto existente por su `id`.
   - **Método**: `POST`

### 4. **`/eliminar/<int:id>` - `eliminar(id)`**
   - Elimina un producto por su `id`.
   - **Método**: `GET`

### 5. **`/buscar` - `buscar()`**
   - Busca productos por nombre o categoría (sin sensibilidad a mayúsculas ni tildes).
   - **Método**: `POST`