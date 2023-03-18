#----------- MENÚ -------------#

Codigo = ['001','002']
Nombre = ['Anderson yepes', 'Mathias yepes']
Puesto = ['Ing Software', 'Ing Sistemas']
Telefono = [3147247816,3126251762]

print('\n.....Menú Principal...\n')

menuPrincipal = int(input(' 1 - Ver la lista de la platilla: '
                          '\n 2 - Insertar Persona'
                          '\n 3 - Eliminar Persona'
                          '\n 4 - Modificar Persona'
                          '\n 0 - Salir\n'))

while menuPrincipal !=0:

    if menuPrincipal == 1:
        print('\n Codigo |  Nombre       | Puesto           |  Telefono\n')

        for i in range(len(Codigo)):
            print('',Codigo[i],'   ',Nombre[i],'   ',Puesto[i],'   ',Telefono[i],'')

    elif menuPrincipal == 2:

        print('\nLlena los siguientes datos: \n')
        Codigo.append(input('Codigo de la persona: '))
        Nombre.append(input('Nombre de la persona: '))
        Puesto.append(input('Puesto de la persona: '))
        Telefono.append(int(input('Telefono de la persona: ')))

    elif menuPrincipal == 3:
        print('\nEliminado persona.\n')
        cod = input('Ingresa el Codigo para eliminar: \n')
        for i in range(len(Codigo)-1,-1,-1):
            if Codigo[i] == cod:
                Codigo.pop(i)
                Nombre.pop(i)
                Puesto.pop(i)
                Telefono.pop(i)
        print('Persona Eiminada...')

    elif menuPrincipal == 4:

        print('\nModificando persona.\n')
        cod = input('Ingresa el Codigo para Modificar: \n')
        for i in range(len(Codigo)):
            if Codigo[i] == cod:
                Nombre[i] = input('Cual es el nuevo nombre: ')
                Puesto[i] = input('Cual es el nuevo puesto: ')
                Telefono[i] = int(input('Cual es el nuevo numero de telefono: '))
        print('Persona modificada....')

    else:
        print('Por favor digite una opcion correcta.\n')
    
    menuPrincipal = int(input('\n 1 - Ver la lista de la platilla: '
                          '\n 2 - Insertar Persona'
                          '\n 3 - Eliminar Persona'
                          '\n 4 - Modificar Persona'
                          '\n 0 - Salir\n'))
    