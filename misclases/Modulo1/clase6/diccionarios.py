conceptosProgramacion = {
    'POO' : 'Programación Orientada a Objetos',
    'IDE' : 'Entorno de desarollo',
    'DBMS' : 'Sistema de Gestión de Base de Datos'
}

print(conceptosProgramacion)
# Tamaño de un diccionario
print(len(conceptosProgramacion))

# Obtener un elemento del diccionario
print(conceptosProgramacion['DBMS'])

# Obtener un elemento del diccionario por get
print(conceptosProgramacion.get('POO'))

# Cambiar el valor de una clave
conceptosProgramacion['DBMS'] = 'Database Manager System'
print(conceptosProgramacion)

# Imprimir las claves del diccionario
for concepto in conceptosProgramacion:
    print(concepto)

# Imprimir las claves del diccionario y items
for keys, value in conceptosProgramacion.items():
    print(keys, value)
    
