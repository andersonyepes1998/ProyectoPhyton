mesesAño = (input('Digitalice la fecha del año: '))

primavera1 = '20 de marzo'
primavera2 = '20 de junio'
verano1 = '21 de junio'
verano2 = '23 de septiembre'
otoño1 = '24 de septiembre'
otoño2 ='21 de diciembre'
invierno = '22 de diciembre a 19 de marzo'

if(mesesAño >= primavera1) or (mesesAño <= primavera2):
    print('Usted se encuentra en la siguiente estacion PRIMAVERA')
elif(mesesAño >= verano1 and mesesAño <= verano2) and (mesesAño >= verano2 and mesesAño <= verano1):
    print('Usted se encuentra en la siguiente estacion VERANO')
elif(mesesAño != otoño1 and mesesAño != otoño2):
    print('Usted se encuentra en la siguiente estacion OTOÑO')
else:
    print('Usted se encuentra en la siguiente estacion INVIERNO')