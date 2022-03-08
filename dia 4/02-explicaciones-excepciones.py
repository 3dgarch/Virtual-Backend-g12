productId = input('ingresa el id del producto: ')
 # iremos a la bd y buscaremos ese producto
 # 1, 2, 3, 4, 5, 6, 7, 8, 9, 

 try:
     if(productId == '10'):
         # emitira un error manualmente
         # se utiliza para no continuar con el flujo normal del proyecto
         raise Exception('El producto no existe en la bd')
    # if validar la cantidad de productos
    # if validdar la fecha de vencimiento
    print('la pasarela de pagos concluyo exitosamente..')
    print('la ejecucion continuara..') 
except Exception as e:   
    # ingresara si hubo error
    print('ups algo salio mal con el producto a buscar, mensaje:',e.args[0]) 
else:
    print('el producto encontrado es: ')    