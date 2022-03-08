class Animal:
    # metodo constructor: este metodo se llamara cuando vayamos a crear una nueva instancia de la clase
    def __init__(self, nombre, sexo, nro_patas):
        # crear unos nuevos atributos dentro de la clase y estos ya no seran staticos
        self.nombre = nombre
        self.sexo = sexo
        self.patas = nro_patas
    
    def description(self):
        # si queremos que los atributos que vamos a utilizar sean creados y puedan ser
        # accedidos desde cualquier parte de la instancia de la clase entonces las deberemos de crear en el constructor
        return 'yo soy {}, soy {}, y tengo{}, patas'.format(
            self.patas, #0
            self.sexo, #1
            self.nombre, #2
        )

foca = Animal('foca', 'M', 2)        
caballo = Animal('caballo', 'M', 4)
gato = Animal('gato', 'F', 4)

print(foca.description())
print(caballo.description())
print(gato.description())