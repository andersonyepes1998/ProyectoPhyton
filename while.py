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

####################################

edad = int(input('ESCRIBE LA EDAD DEL ALUMNO... '))

if edad >= 18:
    print('Es mayor de edad...')
else:
    print('Es menor de edad...')


numeros_desendentes = sorted([77, 22, 9, -6, 4000],reverse=True)

print("Ordenados en orden descendente: ",numeros_desendentes)


numeros_desendentes = sorted([77, 22, 9, -6, 4000])

print("Ordenados en orden ascendente: ",numeros_desendentes)
