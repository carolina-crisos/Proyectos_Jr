from datetime import datetime

print('\nBrindanos tus datos personales.\n')


while True:
    try:
        nombre = input('Ingresa tu nombre: ')
        if nombre.strip() and nombre.replace(" ", "").isalpha():
            break
        else:
            raise ValueError
    except ValueError:
        print('Error! Ingrese un nombre válido sin números ni caracteres especiales.')


while True:
    try:
        fecha_nac = datetime.strptime(input('Añade tu fecha de nacimiento (dd/mm/aaaa): '), '%d/%m/%Y')
        break
    except ValueError:
        print('Error! Ingresa una fecha válida en el formato dd/mm/aaaa.')


while True:
    try:
        direccion = input('Escribe tu dirección (calle, colonia): ')
        if ',' not in direccion:
            raise ValueError
        direccion = direccion.split(',')
        break
    except ValueError:
        print('Error! La dirección debe tener el formato (calle, colonia).')


while True:
    meta = input('Menciona tu meta principal, en máximo 15 palabras: ')
    if len(meta.split()) <= 15:
        break
    else:
        print('Error! La meta debe tener un máximo de 15 palabras.')


biografia = f'''
Biografía:
- Nombre: {nombre.title()}
- Fecha de nacimiento: {fecha_nac.strftime('%d/%m/%Y')}
- Calle: {direccion[0].strip().title()}
- Colonia: {direccion[1].strip().title()}  
- Metas personales: {meta.capitalize()}.
'''

print(biografia)




