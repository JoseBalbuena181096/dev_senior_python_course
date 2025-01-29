# codificación camel case
# 1.5 float 35 int johan manurl str

ventasTotales = 0.0

# solicitar el numero de productos
numProductos = int(input("Ingrese el número de productos a gestionar"))

# listas para almacenar la informacion 
nombres = []
precios = []
cantidades = []

print("Ingresos inical de productos a la tienda: ")

for i in range(numProductos):
    print(f'Producto {i+1}: ')
    nombre = input("Ingresa el nombre del producto: ").lower()
    nombres.append(nombre)
    precio = float(input("Ingrese el precio del producto: "))
    precios.append(precio)
    cantidad = int(input("Digite la cantidad de producto: "))
    cantidades.append(cantidad)


# la mejor manera para crear un menu un ciclo
while True:
    print('\n --- MENU GESTION TIENDA --- \n')
    print('\n 1.) Vender productos')
    print('\n 2.) Mostrar inventario')
    print('\n 3.) Mostrar Ventas totales')
    print('\n 4.) Salir')

    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        print('\nVender producto')
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input("Ingrese la cantidad a vender"))
        productoEncontrado = False

        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f'Venta realizada total de esta venta ${totalVenta:.2f}')
                    print(f'Quedan {cantidades[i]} unidades de {nombres[i]} en stock')
                else:
                    print(f'Cantidad insuficiente en inventario solo quedan {cantidades[i]}')
                break
        if not productoEncontrado:
            print(f'Producto {nombre} no encontrado en stock')
    
    elif opcion == 2:
        print('\nMonstrar inventario')
        for i in range(len(nombres)):
            print(f'\nProducto {i+1}: {nombres[i].capitalize()} \
                   Precio: {precios[i]:.2f} Cantidad: {cantidades[i]}')

    elif opcion == 3:
        print(f'\nMonstrar ventas totales acumuladas: ${ventasTotales:.2f}')
    
    elif opcion == 4:
        print('\nGracias por usar el sistema de gestion de la tienda')
        print('\nHasta luego vuelva pronto')
        break
    
    else:
        print("\nOpcion invalida ingrese entre uno y cuatro")

                    

        


