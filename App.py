from flask import Flask, render_template, request, redirect, url_for
from GestionInventario import GestionInventario
from Producto import Producto
from unidecode import unidecode

app = Flask(__name__)

@app.route('/')
def index():
    productos = GestionInventario.seleccionar_productos()
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    categoria = request.form['categoria']
    nuevo_producto = Producto(None, nombre, precio, cantidad, categoria)
    GestionInventario.insertar_producto(nuevo_producto)
    return redirect(url_for('index'))

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    categoria = request.form['categoria']
    producto_actualizado = Producto(id, nombre, precio, cantidad, categoria)
    GestionInventario.actualizar_producto(producto_actualizado)
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    producto_a_eliminar = Producto(id, None, None, None, None)
    GestionInventario.eliminar_producto(producto_a_eliminar)
    return redirect(url_for('index'))

@app.route('/buscar', methods=['POST'])
def buscar():
    tipo_busqueda = request.form['tipo']
    valor = request.form['valor']

    # Normalizar el valor de búsqueda: convertir a minúsculas y eliminar tildes
    valor_normalizado = unidecode(valor.lower())

    productos = []

    if valor != '':
        if tipo_busqueda == 'nombre':
            productos = GestionInventario.buscar_producto('nombre', valor_normalizado)
        elif tipo_busqueda == 'categoria':
            productos = GestionInventario.buscar_producto('categoria', valor_normalizado)
    else:
        productos = GestionInventario.seleccionar_productos()

    
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
