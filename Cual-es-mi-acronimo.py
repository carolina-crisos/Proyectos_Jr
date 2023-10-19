print('''
Escribe el nombre completo de alguna 
organización, empresa o persona. 
Vamos a generar su acrónimo!
''')

nombre_completo = input('Ingresa el texto indicado: ').title()


acrónimo = ''.join(word[0] for word in nombre_completo.split())

print('El acrónimo generado es:', acrónimo)
