#lista en python

productos = ["Carne", "Papa", "tomate"]
productos.append("Yuca")
print(productos)

# tuplas python
codigo_postal = (45401, "Zipaquira")
# no es valio modificar el valor de una tupla
# codigo_postal[1] = 33342 
print(codigo_postal)

# Set (conjunto) em Python
categorias = {'Terror', 'Drama', 'ScFc'}
categorias.add('Suspenso')
print(categorias)

# Diccionarios (dict) en Python
clientes = {
    "id": 1010,
    "Nombre": "Jose Balbuena"
}

print(clientes)
clientes['email'] = "josebalbuena181096@gmail.com"
print(clientes)

