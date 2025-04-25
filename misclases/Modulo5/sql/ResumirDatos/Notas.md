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
	cliente,
	MAX(venta) AS maxima_compra
FROM ventas
WHERE YEAR(fecha) = 2018
GROUP BY cliente;
```