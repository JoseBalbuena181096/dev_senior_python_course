paises = ('Colombia', 'Mexico', 'Ecuador', 'Venezuela')
print(type(paises))

# lenght of list
print(len(paises))

# El numero 2
print(paises[2])

# El ultimo pais
print(paises[-1])

for pais in paises:
    print(pais)

paises = list(paises)
paises[1] = 'Argentina'
paises = tuple(paises)
print(paises)

# La tuplas no se debe poder modificar 

# eliminar la tupla 
del paises
print(paises)
