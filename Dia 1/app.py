import re
from flask import Flask, request
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
CORS(app=app)


clientes = [
    {
        "nombre": "Eduardo",
        "pais": "PERU",
        "edad": 29,
        "id": 1,
        "organos": True,
        "casado": False
    }
]


@app.route('/')
def esatdo():
    hora_del_servidor = datetime.now()
    return {
        'status': True,
        'hour': hora_del_servidor.strftime('%d/%m/%y %H:%M:%S')
    }


@app.route('/clientes', methods=['POST', 'GET'])
def obtener_clientes():
    # solamente puede ser llamado en cada controlador (funcion que se ejecutara cuandoi se realice una peticion desde el front)
    print(request.method)
    # request.method > mostrara el tipo de metodo al cual esta haciendo la consulta el front
    print(request.get_json())
    # request.get_json() > devolvera la informacion enviada por el body y la convertira a un diccionario para que python lo pueda entender y manipular

    if request.method == 'POST':
        # ingresara cuando el metodo sea POST
        data = request.get_json()
        data['id'] = len(clientes) + 1
        # DATA > AGREGAR UNA LLAVE LLAMADA ID QUE SERA LA LONGITUD DE LA LISTA ACTUAL
        clientes.append(data)

        return {
            'message': 'Cliente agregado exitosamente',
            'clientes': data
        }
    else:
        # elif request.method == 'GET:
        # ingresara cuando el metodo sea GER
        return {
            'message': 'la lista de clientes',
            'clientes': clientes
        }


# v1
def buscar_usuario(id):
 #   for cliente in clientes:
 #       if cliente.get('id') == id:
 #           return cliente

# v2
  for posicion in range(0, len(clientes)):
    if clientes[posicion].get('id') == id:
        return ( clientes[posicion], posicion )




@app.route('/cliente/<int:id>', methods=['GET', 'PUT'])
def gestion_usuario(id):
    print(id)
    if request.method == 'GET':
        usuario = buscar_usuario(id)
        if usuario:
            return usuario[0]
        else:
            return {
            'message': 'el usuatio no se encontro'
        }, 404

    elif request.method == 'PUT':
        resultado = buscar_usuario(id)
        if resultado is not None:
            [cliente, posicion] = resultado

            data = request.get_json()
        else:
            return{
                'message': 'El usurio no se encontro'
            }, 404
    
    elif request.method == 'DELETE':
        resultado = buscar_usuario(id)
        if resultado:
            [usuario ,posicion] = resultado
            usuario_eliminado = clientes.pop(posicion)
            return {
                'message': 'usuario eliminado exitosamenete',
                'usuario': usuario_eliminado
            }
        else:
            return {
                'message': 'el usuario a eliminar no se encontro'
            }


# debug < si esta habilitada(true) se reiniciara  automaticamnete el servidor cada vez que guardamos cambios en cualquier  archivo
app.run(debug=True)
