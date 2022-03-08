# encapsulamiento > se declara  tipos de accesibilidad a los atributos y metodos

class producto:
    def __init__(self, nombre, precio):
        #existen 3 tipos de accesibilidad a los atributos y metodos de una clase: public
        self.nombre = nombre
        self.precio = precio

        # privado
        self.__ganancia = self.precio * 0.30

cepillo = producto('cepillo dental',3.80)        
# atributo publico = porque puedo acceder a este tanto desde la misma clase como en su instancia
sepillo.nombre

# atributo privado = solamente podra ser accedido a el dentro de la msima clase pero no desde su instancia
cepillo.__ganancia

print(cepillo.mostrar_info())
