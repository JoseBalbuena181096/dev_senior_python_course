nombres = ['Juan', 'Sebastian', 'Melissa', 'Xiaomara'] 

print(type(nombres))

# primer elemento de la lista
print(nombres[0])

# ultimo elemento de la lista
print(nombres[-1])

# punto de partida si se toma y el de finalizacion no se toma
# print(nombres[0:2])
print(nombres[:2])

# todos 
print(nombres[:])

# solo el 2
print(nombres[2:3])

# saber elemtos de mi lista 
print(len(nombres))

# agregar un elemento al final de la lista
nombres.append('Elizabeth')
print(nombres)

# insertar un elemnto a la lista en un indice especifico
nombres.insert(1, 'Maria')
print(nombres)

nombres.remove('Elizabeth')
print(nombres)

# mover a elizabeth en primero
nombres.insert(1, 'Elizabeth')
print(nombres)

nombres.append('Elizabeth')
print(nombres)

# Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

# nombres.pop(1)
# print(nombres)

# Eliminar sebastian 
# Eliminar el ultimo elemento de la lista
del nombres[3]
print(nombres)

nombres.remove('Elizabeth')
print(nombres)

# limpar la lista
nombres.clear()
print(nombres)

# del nombres
# print(nombres)