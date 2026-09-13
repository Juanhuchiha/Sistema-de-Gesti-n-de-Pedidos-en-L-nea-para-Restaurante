from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
    {"id_producto": 1, "nombre": "Café Latte", "precio": 4500, "stock": 20},
    {"id_producto": 2, "nombre": "Sandwich Vegetariano", "precio": 8500, "stock": 15}
]

pedidos = []

@app.route('/productos', methods=['GET'])
def get_productos():
    return jsonify(productos)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    return jsonify({"mensaje": "Usuario registrado", "usuario": data}), 201

@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    data = request.get_json()
    pedidos.append(data)
    return jsonify({"mensaje": "Pedido creado", "pedido": data}), 201

@app.route('/pedidos/<int:id_pedido>', methods=['GET'])
def get_pedido(id_pedido):
    if id_pedido < len(pedidos):
        return jsonify(pedidos[id_pedido])
    return jsonify({"error": "Pedido no encontrado"}), 404

@app.route('/reportes/ventas', methods=['GET'])
def reporte_ventas():
    return jsonify({"total_pedidos": len(pedidos)})

if __name__ == '__main__':
    app.run(debug=True)
