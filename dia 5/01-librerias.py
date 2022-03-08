from camelcase import CamelCase

instanciaCC = CamelCase('mundo','del')

texto = 'Bienvenidos al mundo del backen'
print(instanciaCC.hump(texto))


# TODO: hacer lo mismo que el camelcase sin la libreria