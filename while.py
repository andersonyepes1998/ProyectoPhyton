#Que es el ciclo while en python
#Es un ciclo que va a repetir un grupo de odigo miestras se cumpla una condicion....

i = 5

while i < 20:
    print('El valor de i es: ',i)
    i+=1

num = int(input('ESCRIBE UN NUMERO POSITIVO... '))

while num < 0:
    print('Es un numero negativo')
    num = int(input('ESCRIBE UN NUMERO NEGTAIVO...PRUEBA DE NUEVO '))
print('El numero es:',num)
