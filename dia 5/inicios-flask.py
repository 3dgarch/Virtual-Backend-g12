# no se puede crear un archivo con el mismo
from flask import Flask
from datetime import datetime


#__name__ > muestra si el archivo es el archivo raiz o principal del proyecto,  si el archivo es el archivo principal esntonces el valor de __name__ sera __main__
app = Flask(__name__)

# los decoradores es un patron de software que se utiliza para modificar el funcionamiento de un metodo o de una clase en particular sin la necesidad de emplear otros  metodos como la herencia
@app.route('/')

# voy a modificar el comportamiento del metodo route para cuando su ruta sea '/' y su nuevo comportamiento sera el siguiente definido en la funcion inicial
def inicial():
    print('Me llamo')
    # siempre en los controladores tenemos que devolver una respuesta!
    return 'Bienvenido a mi API 😎'


@app.route('/api/info')
def info_app():
    return {
        'fecha': datetime.now() # esto me devuelve la hora  y fecha actual del servidor
    }


# inicializaremos nuestro servidor de flask
app.run(debug=True)