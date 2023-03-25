option = 1

empanadas = []

while option != 0:
    print('*****Empanadas******')
    print('Opcion 1= Ingrese una empanada: ')
    print('Opcion 2= Mostrar todas las empandas que estan registradas: ')
    print('Opcion 3= Buscar empanadas por ID: ')
    print('Opcion 4= EDitar una empanada: ')
    print('Opcion 5= Eliminar una empanada: ')
    print('Presione 0 para salir: ')
    option = int(input('Escoja una opcion: '))
    if(option == 1):
        empanada = {}
        empanada['id'] = int(input('Digite el id de la empanada: '))
        empanada['nombre'] = (input('Digite el nombre de la empanada: '))
        empanada['precio'] = float(input('Digite el precio de la empanada: '))
        empanada['popularidad'] = int(input('Digite la popularida de la empanada: '))
        empanada['fechavencimiento'] = (input('Digite la fecha de la empanada: '))
        empanadas.append(empanada)
        print('Empanada Registrada...')

    elif(option == 2):
        for empanada in empanadas:
            print(empanada)
    elif(option == 3):
        recorrido = int(input('Digite la empanda que vas a buscar: '))
        for empanada in empanadas:
            if empanada['id'] == recorrido:
                print('Sin empanada')
            else:
                print('empanada econtrada ',empanada)
    elif(option == 4):
         recorrido = int(input('Digite la empanda que vas a buscar: '))
         for empanada in empanadas:
            if empanada['id'] == recorrido:
                print('Sin empanada')
            else:
                print('El precio actual de la empanda es: ')
                print(empanada['precio'])
                precioNuevo = float(input('Digita el nuevo precio: '))
                empanada['precio']=precioNuevo
    elif(option==5):
        recorrido = int(input('Digite la empanda que vas a buscar: '))
        for empanada in empanadas:
            if empanada['id'] == recorrido:
                print('Sin empanada')
    elif(option == 0):
        pass
    else:
        print('Opcion incorrecta')
