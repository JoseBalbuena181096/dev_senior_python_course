lenguajes = {'Java', 'Python', 'JavaScrip'}
print(lenguajes)

# tamaño del set
print(len(lenguajes))

# ver si un elemento esta en el set
print('Go' in lenguajes)

# ver si un elemento esta en el set
print('Python' in lenguajes)

# Agregar un elemento
lenguajes.add('Go')
print(lenguajes)

for lenguaje in lenguajes:
    print(lenguaje)

# Elminar un elemento
lenguajes.remove('Java')
print(lenguajes) 

lenguajes.discard('Python')
print(lenguajes) 

