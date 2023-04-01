def saludarPersona(nombre):
    print('hola como estas señor ',nombre)

saludarPersona('Mathias')


def saludarPersona(nombre2='johana'):
    print('hola como estas señora ',nombre2)

saludarPersona()


#FUNCIONES LAMBDAS

#Las funciones lambdas, son funciones que sirven para abreviar o resumir una funcion,
#para convertirla en una expresion mas simple...

#de una funcion LAMBDA a una funcion tradicional si sepuede pasar, pero de no de una,
#tradiconal a LAMBDA...

saludar2 = lambda nombre3:f'hola hijo mio como te llamas, {nombre3}'
print(saludar2('Mathias'))


##########         RETOS              ############
'''
temperatura = int(input('Digite la temperatura de medellin: '))

temperaturaResult = lambda temperatura: temperatura+8
print(temperaturaResult)

ancho= int(input('Digitalice el ancho: '))
alto= int(input('Digitalice el alto: '))'''

result = lambda ancho,alto: ancho*alto
perimetro = lambda lado,lado2: (lado*2)+(lado2*2)
print('El area del cuadrado seria ',result(5,3), ' y el perimetro es igual a ',perimetro(5,3))
print('*****')
print('*****')
print('*****')