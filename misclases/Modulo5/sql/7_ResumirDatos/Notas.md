### Agregaciones en SQL

Las agregaciones son funciones que permiten resumir datos en una sola fila. Realizar operaciones matematicas con los datos de una columna.

Tenemos 3 tipos de agregaciones:
1. Agregaciones de suma
2. Agregaciones de conteo
3. Agregaciones de promedio
4. Agregaciones de maximo
5. Agregaciones de minimo
6. Agregaciones de conteo distinto

Funcion MAX 
Esta funcion devuelve el valor maximo de una columna:
```sql
SELECT MAX(columna) FROM tabla;
```
Ejemplo traer el usuario con la mayor venta:
```sql
SELECT MAX(venta) FROM ventas;
```

El empleado con la mayor venta:
```sql
SELECT 
       v.venta AS venta_maxima, 
       v.venta_empleado, 
       v.Fecha
FROM ventas v
WHERE v.venta = (SELECT MAX(venta) FROM ventas);
```

Funcion SUM:
Esta funcion devuelve la suma de todos los valores de una columna:
```sql
SELECT SUM(columna) FROM tabla;
```

Ejemplo traer el total de ventas:
```sql
SELECT 
	SUM(venta) AS total_ventas
FROM ventas;
```

Funcion COUNT:
Esta funcion devuelve el conteo de todos los valores de una columna, si es null no se cuenta:

```sql
SELECT COUNT(columna) FROM tabla;
```

Ejemplo traer el total de ventas:
```sql
SELECT 
	COUNT(venta) AS total_ventas
FROM ventas;
```

Funcion DISTINCT:
Esta funcion devuelve el conteo de todos los valores de una columna, si es null no se cuenta:

```sql
SELECT DISTINCT(columna) FROM tabla;
```

Ejemplo conteo de empleados unicos:
```sql
SELECT 
	COUNT(DISTINCT venta_empleado) AS empleados_unicos
FROM ventas;
```

Funcion AVG:
Esta funcion devuelve el promedio de todos los valores de una columna:
```sql
SELECT AVG(columna) FROM tabla;
```

Ejemplo traer el promedio de ventas:
```sql
SELECT 
	AVG(venta) AS promedio_ventas
FROM ventas;
```

### GROUP BY

Permitre agrupar los registros en alguna operación de resumen o agregación como contar, maximos, minimos, promedios, sumas, etc.

```sql
SELECT 
	SUM(venta),
	ID_local
FROM ventas;
```

Formas de uso del GROUP BY:
1. Se coloca posterior a la clausula FROM o WHERE en caso de estar presente.
2. Se debe agrupar a partir de una de las columnas llamadas en la clausula SELECT.
3. Es usada con funciones de agregacion: count, max, min, sum, avg.

Ejemplo de uso:

```sql
SELECT 
	SUM(venta),
    ID_local
FROM ventas 
GROUP BY ID_local;
```

Si no tendo ninguna agregacion, el GROUP BY no tiene sentido.
```sql
SELECT 
	SUM(venta),
    venta_empleado
FROM ventas
GROUP BY venta_empleado;
```

### HAVING
Se usa para filtrar por campos agrupados, esto es útil por que WHERE no puede ser usado con GROUP BY.



Si lo que quieres es, por cada id_local, el producto con mayor venta total, 
puedes usar una subconsulta con funciones de ventana

```sql
SELECT 
  id_local,
  ANY_VALUE(clave_producto) AS clave_producto,
  SUM(venta) AS venta_total
FROM ventas
GROUP BY 
  id_local;
```

Agrupar por ambas columnas
Si lo que buscas es el total de ventas por local y por producto, simplemente agrúpalas a ambas:

```sql
SELECT 
	id_local,
	clave_producto,
	SUM(venta) AS venta_total
FROM ventas
GROUP BY
	ID_local,
	clave_producto;
```

Utilizando HAVING
Seleccionar solo los locales con ventas superiores a 1500:
```sql
SELECT 
	id_local,
	SUM(venta) AS venta_total
FROM ventas
GROUP BY 
	id_local
HAVING 
	venta_total > 1500;
```
Nota: HAVING  a diferencia de WHERE, se usa para filtrar por campos agrupados, y se coloca despues de GROUP BY.

WITH ROLLUP:

Es un modificador utilizado para producir resumenes de las salidas de informacion de distintos grupos,
es decir, subtotales y totales.

La siguiente consulta, realiza un resumen de las ventas por local, y ademas, un resumen total de todas las ventas:
```sql
SELECT id_local, sum(venta) AS venta_total
FROM ventas
GROUP BY id_local
WITH ROLLUP;
```

La siguiente consulta, realiza un resumen de las ventas por local y producto, y ademas,
un resumen total de todas las ventas:

``` sql
SELECT id_local,clave_producto, sum(venta) AS venta_total
FROM ventas
GROUP BY 
	id_local,
    clave_producto
WITH ROLLUP;
```

El with rollup, es solo util en consultas rapidas.

## Ejercicios

### Informes Aggregate

Notas
-	El uso de SUM() nos permite obtener un resumen de datos al tener un nivel de agregacion, 
de sumas, recuerda los demas:
- MAX()
- MIN()
- AVG()
- COUNT()
- Es importante seleccionar las columnas necesarias para mostrar la informacion. que nos interesa.

Tienes que entregar un informe por cliente donde  entregas la siguiente informacion:

1. ¿Cual cliente realizo la compra maxima ene el año 2018?
```sql
SELECT
    c.nombre,
    MAX(v.venta) AS maxima_compra
FROM ventas v
JOIN clientes c ON v.ID_Cliente = c.ID_cliente
WHERE v.fecha_venta BETWEEN '2018-01-01' AND '2018-12-31'
GROUP BY c.nombre;
```

2. Cual fue el pago menor que recibimos en 2018

```sql
SELECT
	ID_pago,
    MIN(p.pago) AS minima_compra
FROM pagos p
WHERE p.fecha_pago BETWEEN '2018-01-01' AND '2018-12-31'
GROUP BY p.ID_pago;
```

3. Cuantas ventas hubo en el 2ndo semestre 2018
```sql
SELECT
	COUNT(*) AS ventas_2do_semestre
FROM ventas
WHERE YEAR(fecha_venta) = 2018
AND MONTH(fecha_venta) BETWEEN 7 AND 12;
```
```sql
SELECT 
	COUNT(*) AS CONTEO
FROM ventas
WHERE fecha_venta BETWEEN '2018-07-01' AND '2018-12-31';
```

### Ejercicios con GROUP BY
Importante:
El uso de GROUP BY te permite agrupar algún nivel de agrgación en base a otra columna.

Genera una vista para entregar el informa.

1. Las ventas por vendedor:
```sql
SELECT 
    ve.nombre,
    SUM(v.venta) AS total_ventas
FROM ventas v
JOIN `db_practica1`.`vendedores` ve ON v.id_vendedor =  ve.ID_Vendedor
GROUP BY ve.nombre;
```

2. Ventas por producto:
```sql
SELECT
	p.producto,
    SUM(v.venta) AS total_ventas
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY p.producto;
```

3. Resumen de compras por cliente en 2017:
```sql
SELECT
	c.nombre,
    SUM(v.venta) AS total_ventas
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
WHERE YEAR(v.fecha_venta) = 2017
GROUP BY c.nombre;
```

### Ejercicios con HAVING
Con HAVING  logramos tener otro filtro que aplica a funciones de agrecación en donde where NO PUEDE SER USADO
Recuerda el orden
1. SELECT
2. FROM
3. WHERE
4. GROUP BY
5. HAVING


Resumen de compras por cliente en 2017 que hayan sido mayores a 120000000:

```sql
SELECT 
	c.nombre,
    SUM(v.venta) AS total_ventas
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
WHERE  YEAR(v.fecha_venta) = 2017
GROUP BY c.nombre
HAVING total_ventas > 120000000; 
```

### Extra
Generando datos importantes
Importante:
-	El uso conjunto de JOINs, UNIOs Y GROUPs y funciones nos darán ese dato que queremos lograr.
- Ventaja de usar SQL es que puedes procesar millones de registros y hacer cálculos con información necesaria.

1. Dame la lista de los clientes morosos:

```sql
SELECT v.id, v.ID_cliente, v.venta, SUM(p.monto) AS pago, v.venta - SUM(p.monto) AS saldo
FROM pagos p
JOIN ventas v
ON p.ID_venta = v.id
GROUP BY p.ID_venta;
```