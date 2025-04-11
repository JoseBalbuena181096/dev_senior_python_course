## Comandos de SQL

### SELECT 
Se utiliza pata recuparar datos de una o más tablas en la base de datos.
```
SELECT * FROM usuarios;
```

### Insert
Se utiliza para insertar nuevos registros en una tabla.
```
INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);
```

### UPDATE
Se utiliza para actualizar los valores de uno o más registros en una tabla
```
UPDATE usarios SET edad = 26 WHERE nombre='Juan';
```

### DELETE
Se utiliza eliminar uno o más registros de una tabla.
```
DELETE  FROM usuarios WHERE nombre = 'Jose';
```

### CREATE TABLE
Se utiliza para crear una tabla en la base de datos.
```
CREATE TABLE productos (
    id INT  PRIMARY KEY,
    NOMBRE VARCHAR(50),
    precio DECIMAL(10,2)
);
```

### ALTER TABLE
Se utiliza para modificar una tabla existente, como añadir o eliminar columnas.

```
ALTER TABLE productos ADD COLUMN descripcion VARCHAR(100);
```

### DROP TABLE
Se utiliza para eliminar  una tabla de la base de datos.
```
DROP TABLE productos;
```

### JOIN
Se utiliza para combinar filas de dos o más tablas basado en una condición relacionada.
```
SELECT * FROM usuarios JOIN pedidos ON usuarios.id = pedidos.usuarios.usuario_id;
```

### WHERE
Se utiliza para filtrar registros basados en una condición específica.
```
SELECT * FROM usuarios WHERE edad > 18;
```

### GROU BY
Se utiliza para agrupar filas en base a una columna específica.

```
SELECT ciudad, COUNT(*) FROM usuarios GROUP BY ciudad;
```

## Comandos un poco más avnazados.

###  UNION
Se utiliza para combinar el resultado de dos o más consultas en un solo conjunto de resultado.
```
SELECT nombre FROM clientes UNION  SELECT nombre FROM provedores;
```

### SUBCONSULTAS
Se utilizan para incluir una consulta dentro de otra consulta. La subconsulta se ejecuta primero y su resultado se utiliza en la consulta principal.
```
SELECT nombre FROM clientes WHERE id IN (SELECT cliente_id FROM pedidos);
```

### ORDER BY
Se utiliza para ordenar el resultado de una consulta en base a una o más columnas, ya sea en orden ascendente o desentende.
```
SELECT * FROM productos ORDER BY precio DESC;
```

La base de datos vive un servido el cual pude ser local o remoto.

La conexión a una base de datos se compone de:
-   Base de datos (a la que te quieres conectar).
-   El usuario (el usuario que se quiere conectar ala base de datos)
-   La contraseña (La contraseña para poder acceder al base de datos)

## Crear una conexión a mysql desde MySQL Workbench


Precionar en el mas de MySQL Connections
![alt text](image.png)

Modificar los campos para conexión tal como

Connection Name: "El nombre de la conexión"
Connection Method: Standard (TCP/IP)
HOST: Es la dirección ip del servidor de la base de datos (127.0.0.1) hace referencia a que la base de datos esta en local.
PORT: 3306 Es pueto por donde te puedes comunicar al servicio de la base de datos.
USERNAME: El usuario que se esta conectando al  base de datos (por defecto root es el super usuario que tiene todos los privilegios sobre la base de datos).
PASSWORD: es la contraseña para acceder al la base de datos.

![alt text](image-1.png)

Para probar la conexión precionado test de Connection.
![alt text](image-2.png)

## Importar informacion de una archivo existente

Ir al menu superior de opciones y seleccionar la opción de Server, despues la opción de Data Import para realizar la importación.
![alt text](image-3.png)

Despues ir a la opcion de Import from Dump Project Folder e importar la base de datos de un archivo.db

![alt text](image-4.png)

Despues crear un nuevo schema de los datos importados.
![alt text](image-5.png)

Uun esquema(o schema en inglés) es básicamente una colección de objetos de base de datos, como tablas, vistas, procedimientos almacenados, índices y otros elementos relacionados. En MySQL la base de datos y el esquemas es practicamente lo mismo.

Por último se realiza la importación en Start Import.
![alt text](image-6.png)

Crear la base de datos -> "datos"

 ```
 -- Crear la base de datos
CREATE DATABASE IF NOT EXISTS datos;
USE datos;

-- Crear tabla Local
CREATE TABLE IF NOT EXISTS Local (
    ID_Local INT PRIMARY KEY,
    Letra_zona CHAR(1),
    Direccion VARCHAR(100),
    Telefono VARCHAR(15)
);

-- Crear tabla Empleados
CREATE TABLE IF NOT EXISTS Empleados (
    ID_empleado INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Telefono VARCHAR(15),
    Edad INT,
    Domicilio VARCHAR(100),
    ID_Gerente INT,
    FOREIGN KEY (ID_Gerente) REFERENCES Empleados(ID_empleado)
);

-- Crear tabla Productos
CREATE TABLE IF NOT EXISTS Productos (
    producto_id INT AUTO_INCREMENT PRIMARY KEY,
    clave_producto VARCHAR(10) UNIQUE,
    Producto VARCHAR(50)
);

-- Crear tabla Tamanos
CREATE TABLE IF NOT EXISTS Tamanos (
    tamano_id INT AUTO_INCREMENT PRIMARY KEY,
    Tamano VARCHAR(5) UNIQUE,
    Descripcion VARCHAR(50),
    Tamano_CMS INT
);

-- Crear tabla Ingredientes
CREATE TABLE IF NOT EXISTS Ingredientes (
    ingrediente_id INT AUTO_INCREMENT PRIMARY KEY,
    clave_ingrediente VARCHAR(10) UNIQUE,
    Ingredientes VARCHAR(50),
    precio_porcion DECIMAL(10,2)
);

-- Crear tabla Venta_Detalle
CREATE TABLE IF NOT EXISTS Venta_Detalle (
    detalle_id INT AUTO_INCREMENT PRIMARY KEY,
    ID_venta INT UNIQUE,
    Tipo VARCHAR(10)
);

-- Crear tabla Ventas
CREATE TABLE IF NOT EXISTS Ventas (
    ID_venta INT AUTO_INCREMENT PRIMARY KEY,
    Fecha DATE,
    ID_local INT,
    clave_producto VARCHAR(10),
    venta DECIMAL(10,2),
    venta_empleado INT,
    FOREIGN KEY (ID_local) REFERENCES Local(ID_Local),
    FOREIGN KEY (clave_producto) REFERENCES Productos(clave_producto),
    FOREIGN KEY (venta_empleado) REFERENCES Empleados(ID_empleado)
);

-- Insertar datos en la tabla Local
INSERT INTO Local (ID_Local, Letra_zona, Direccion, Telefono) VALUES
(1, 'A', 'Av de las Rosas 123', '357894'),
(2, 'B', 'Calle poniente manzana 4', '377896'),
(3, 'C', 'Insurgentes 558', '347899'),
(4, 'D', 'Rinconada de Magnolias 409', '378341'),
(5, 'E', 'Americas 299', NULL);

-- Insertar datos en la tabla Empleados
INSERT INTO Empleados (ID_empleado, Nombre, Apellido, Telefono, Edad, Domicilio, ID_Gerente) VALUES
(5942572, 'Jesus', 'Agudelo', '34616222', 35, NULL, NULL);

INSERT INTO Empleados (ID_empleado, Nombre, Apellido, Telefono, Edad, Domicilio, ID_Gerente) VALUES
(1111222, 'Alberto', 'Barrientos', '34766613', 26, 'Federal 233', 5942572),
(9922377, 'Alexander', 'Martinez', '36554872', 28, 'Camino viejo 123', 5942572),
(3833745, 'Maria', 'Zapata', '35354455', 34, 'Boulevard 85', 5942572),
(2520477, 'Egidio', 'Lopez', '33444383', 24, 'Rosas 996', 5942572),
(9611338, 'Haygnes', 'Ortiz', '35400189', 27, 'General Diaz 343', 5942572),
(4245367, 'Alexandra', 'Zapata', '33467136', 31, 'Ingenieros 234', 5942572),
(2630867, 'Elena', 'Atehortua', '35581732', 37, 'Sierra del tigre 299', 5942572),
(2310967, 'Jairo', 'Mira', '36403810', 29, 'Calle 25 interior 2', 5942572),
(6931035, 'Albeiro', 'Villa', '33631010', 39, 'Carniceros 233', 5942572),
(6332756, 'Reinaldo', 'Gonzalez', '36642727', 43, 'Vallarta 711', 5942572),
(5728566, 'Carlos', 'Rodriguez', '35556677', 33, 'Av. Principal 123', 5942572);

-- Insertar datos en la tabla Productos
INSERT INTO Productos (clave_producto, Producto) VALUES
('pzz', 'Pizza'),
('clz', 'Calzone'),
('qsd', 'Quesadilla'),
('brr', 'Burrito');

-- Insertar datos en la tabla Tamanos
INSERT INTO Tamanos (Tamano, Descripcion, Tamano_CMS) VALUES
('P', 'Pequeño', 20),
('M', 'Mediano', 30),
('G', 'Grande', 40),
('EG', 'Extra Grande', 50);

-- Insertar datos en la tabla Ingredientes
INSERT INTO Ingredientes (clave_ingrediente, Ingredientes, precio_porcion) VALUES
('pep', 'Pepperoni', 8.00),
('ceb', 'Cebolla', 5.00),
('pim', 'Pimiento', 10.00),
('sal', 'Salchicha', 5.00),
('piñ', 'Piña', 8.00),
('que', 'queso', 5.00);

-- Insertar datos en la tabla Venta_Detalle
INSERT INTO Venta_Detalle (ID_venta, Tipo) VALUES
(1, 'Local'),
(2, 'Llevar'),
(3, 'Llevar'),
(4, 'Local'),
(5, 'LLevar'),
(6, 'Local'),
(7, 'LLevar'),
(8, 'Local'),
(9, 'Local'),
(10, 'Llevar'),
(11, 'Llevar'),
(12, 'Llevar'),
(13, 'Local'),
(14, 'Local'),
(15, 'Llevar'),
(16, 'Llevar'),
(17, 'Llevar'),
(18, 'Local'),
(19, 'Llevar'),
(20, 'Llevar'),
(21, 'Local'),
(22, 'Llevar');

-- Insertar datos en la tabla Ventas (con fechas en formato YYYY-MM-DD)
INSERT INTO Ventas (ID_venta, Fecha, ID_local, clave_producto, venta, venta_empleado) VALUES
(1, '2018-11-18', 2, 'pzz', 1302.00, 2630867),
(2, '2018-09-17', 2, 'clz', 953.00, 2310967),
(3, '2018-10-18', 4, 'brr', 1286.00, 6931035),
(4, '2018-10-30', 1, 'brr', 889.00, 9922377),
(5, '2018-05-16', 1, 'qsd', 495.00, 2520477),
(6, '2018-12-15', 3, 'pzz', 544.00, 9611338),
(7, '2018-07-28', 4, 'pzz', 1444.00, 6332756),
(8, '2018-10-05', 1, 'pzz', 435.00, 2520477),
(9, '2018-04-20', 1, 'qsd', 1203.00, 9922377),
(10, '2018-06-08', 1, 'brr', 1038.00, 6332756),
(11, '2018-08-22', 1, 'brr', 404.00, 3833745),
(12, '2019-09-03', 1, 'pzz', 1362.00, 5728566),
(13, '2019-07-16', 3, 'qsd', 1054.00, 2310967),
(14, '2019-08-27', 3, 'clz', 303.00, 3833745),
(15, '2019-12-15', 1, 'brr', 871.00, 2520477),
(16, '2019-07-30', 3, 'brr', 1062.00, 5728566),
(17, '2019-10-25', 1, 'pzz', 1376.00, 6332756),
(18, '2019-12-14', 3, 'pzz', 957.00, 2310967),
(19, '2019-08-14', 2, 'clz', 972.00, 2310967),
(20, '2019-12-01', 1, 'pzz', 1455.00, 2310967),
(21, '2019-06-08', 4, 'qsd', 497.00, 5728566),
(22, '2019-07-25', 3, 'clz', 1179.00, 2310967);
 ```

Insertar un nuevo producto 
```
INSERT INTO `datos`.`productos` (`producto_id`, `clave_producto`, `Producto`) VALUES ('5', 'MIX', 'Mix Pack');
```

Insertar una nueva columna 
```
ALTER TABLE `datos`.`productos` 
ADD COLUMN `Caracteristicas` JSON NULL AFTER `Producto`;
```

Insertar un Json de caracteristicas al producto con el id 5 
```
UPDATE Productos 
SET caracteristicas = '{"dimension":[5,10,20],"productos":["pizza", "burrito"],"cantidad":2}'
WHERE producto_id=5;
```

#### Función JSON_EXTRACT
Extrae y devuelve los valores deseados del tipo de dato JSON.

```
SELECT producto_id, Producto, JSON_EXTRACT(Caracteristicas, "$.dimension")
FROM productos;
```
![alt text](image-7.png)

```
SELECT producto_id, Producto, JSON_EXTRACT(Caracteristicas, "$.productos") AS productos_incluidos
FROM productos;
```
![alt text](image-8.png)

