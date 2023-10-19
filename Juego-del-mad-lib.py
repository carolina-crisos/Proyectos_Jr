"""
Pedimos al usuario que introduzca varias entradas con varias preguntas.

Una vez que se obtiene las entradas, reorganizar para construir una historia.
"""
while True:

    print('''\n A continuación, rellene los siguientes 
    campos para crear una historia graciosa. \n''')

    nombre_universidad = input('Asigna el nombre de una universidad de tu país: ')
    animales = input('Ingresa el nombre de un animal en plural: ')
    verbo = input('Ahora, brinda un verbo: ')
    cantidad = int(input('Agrega una cantidad: '))
    adjetivo = input('Menciona un adjetivo calificativo: ')

    madlib = f'''\n ¡Noticia de última hora!
    La universidad {nombre_universidad}, anunció que sus 
    nuevos alumnos serán {animales}, para demostrar 
    que pueden {verbo} más que un alumno tradicional. 
    Su colegiatura costará {cantidad} pesos al semestre. 
    Esto será {adjetivo} para el país.
    '''

    print(madlib)

    continuar =  input('¿Deseas ingresar otras entradas? s/n: ')

    if continuar.lower() == 's':
        continue
    else:
        break

print('Fin del juego.')