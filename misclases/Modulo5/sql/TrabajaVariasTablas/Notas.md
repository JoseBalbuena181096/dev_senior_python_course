### Trabajar con más de una Tabla

#### Cláusula JOIN
Se utiliza para combinar filas de dos o más tablas, basadas en una columna relacionada entre ellas.

Unir una tabla ventas (la tabla interna) con la tabla local (la tabla externa), sql me dide una letra para hacer referencia a esa tabla, la primera letra del nombre de la tabla por lo regular.

### ON
```
JOIN local (ON) 
```
Sobre que columna vamos a emparejarlas.
No existen reglas definidas para seleccionar las columnas donde se emparejan, se debe selecionar en base al conocimiento de la base de datos propia y el filling para saber cuales son las dos columnas que unen las tablas, 
generalmente es una clase clave o identificador.


La siguiente query, selecciona todo de la tabla ventas y lo une con la tabla local en donde el ID_local de ventas y el ID_Local  de local, son el mismo. 

```
SELECT *
FROM ventas v
JOIN local l 
	ON v.ID_local = l.ID_LOCAL;
```
La siguiente query, selecciona todo de la tabla ventas y lo une con la tabla local en donde el ID_local de ventas y ID_Local de local, son el mismo, y une la tabla ventas con la tabla empleados donde venta_empleado de la tabla ventas es igual al ID_empleado de la tabla empleado

```
SELECT *
FROM ventas v
JOIN local l
    ON v.ID_local = l.ID_Local
JOIN empleados e
    ON v.venta_empleado = e.ID_empleado;
```

De la consulta anterior depuramos la información, vamos a traer de la tabla ventas el campo ventas_id, fecha, clave_producto, ventya, de la tabla local el Direccion y de la tabla empleado el nombre y el apellido.

```
SELECT 
    v.ventas_id,
    v.fecha,
    l.domicilio,
    v.clave_producto,
    v.venta,
    e.nombre,
    e.apellido
FROM ventas v
JOIN local l
    ON v.ID_local = l.ID_Local
JOIN empleados e
    ON v.venta_empleado = e.ID_empleado;
```

#### ¿Qué pasa cuando tu tienes que hacer JOINS?

De dos Schemas diferentes:
![alt text](image.png)

Cuando deseamos realizar una Query de un Schema diferente al que encuantro seleccionado se debe hacer referencia al Schema, es decir se debe seleccionar el nombre_del_schema.nombre_tabla:

Esta seleccionado el schema biblioteca:
```
USE  biblioteca;
```
Pero de esta forma podemos consultar de un schema diferente como datos atravez de acceder por el punto datos.empleados:
```
SELECT *
FROM datos.empleados;
```
Como utilizar JOIN con tablas de diferentes schemas, para eso se usa la referencia al schema y el nombre de la tabla es decir nombre_schema.nombre tabla.

```
SELECT *
FROM periodo1 p
JOIN datos.empleados e
    ON p.ID_empleado = e.ID_empleado;
```

Para solo seleccionar las columnas deseadas de esas tablas, las columnas periodo1_ID, Fecha, el Nombre del empleados, el Apellido de empleados y el Local y Turno_completo de periodo1:

```
SELECT 
    p.periodo1_ID,
    p.Fecha,
    p.Nombre,
    e.Apellido,
    p.Local,
    p.Turno_completo
FROM periodo1 p
JOIN datos.empleados e
    ON p.ID_empleado = e.ID_empleado;
```

