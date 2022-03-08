# Programacion Orientada a Objetos > POO | OOP
# la programacion debe estar creada en base a clases
# toda parte dec odigo debe de ser tratada comosi fuese una plantilla
# clases > son plantillas para que puedan ser utilizadas varias veces sin la necesidad de modificar su forma en relacion al objeto sino que al revez


class Persona:
    # las variables creadas dentro de la clase pasan a llamarse atributos
    fec_nac = '200-01-01'
    nombre = 'juan'
    soltero = True
    estatura = 1.50


    #en cada metodo siempre como primer parametro obligatoriamente se utiliza la palabra self para hacer referencia dentro de una instancia a los atributos y metodos
    def saludar(self):
        self.decir_nombre()
        self.fec_nac
        print('hola como estan')
        return 'hola {}'.format(self.nombre)



# cuando una variable se crea a raiz de una clase, esta variable pasa a llamar instancia (instancia > copia en su totalidad de la clase)    
persona1 = Persona()
persona2 = Persona()
# modificamos el valor original swl atributo a uno personalizado
persona2.nombre = 'Eduardo'
persona1.nombre = 'carolina'


print(persona1.nombre)