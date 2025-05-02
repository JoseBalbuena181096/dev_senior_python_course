## Tipos de datos 

### ¿Qué es el tipo de datos?
Atributo que indica al la maquina cómo manejar los datos.

### Formato de dato
Es como el usuario ve el tipo de dato:
$1,052,896.00 -> (Tipo de dato numérico intuido por el usuario pero debe preguntar a la computadora para confirmar, no suponer pudiera ser un string).

Ejemplo de error:
multiplicar  $100 * $5 = $500 (pero se debe especificar que 100 y 5 son tipos de datos INT para que tengan la posiblidad de multiplicarse).

### Los tipos de datos que tenemos son:

-   STRING/ Cadena-Textos
-   DATOS NUMÉRICOS
-   TIEMPO / FECHA
-   BLOB / BINARIOS
-   ESPACIALES

### Strings Cadena de Texto

STRING = TEXTO
¿Cómo se guardan los textos en SQL?

-   Números Postales
-   Números de celulares
-   Nombres
-   Cantidades

En SQL tenemos 2 familias en particular de string:

-   CHAR ->  De longitud fijan como:
            -   Código postal (son de 5 caracteres)
            -   RFC (10 Caracteres)
            -   Telefono celular (9 caracteres)

-   VARCHAR ->   De longitud variable, hasta 100 caractes, Es necesario especificar el máximo de caracteres:
            -   Nombres de personas (Los nombres son variables)
            -   Direcciones
            -   Emails.

Según el idioma que estés guardando son la cantidad de bytes que se pueden utilizar por caracter.

Inglés y Español -> Un caracter = 1 BYTE "JOSE" Tiene 4 bytes
Caracteres ásiaticos -> Un caracter  = 3 BYTES 

El limite de VARCHAR es de 0 a 65535 bytes. 
### Otros tipos de texto
-   MIDIUMTEXT (16 millones de caracteres)
-   LONGTEXT (4GB caracteres)
-   TINYTEXT (255 bytes)
-   TEXT (64,000 bytes)

### TIPOS DE DATOS NÚMERICOS.

### Integer = Entero
<-- -4 -- -3 -- -2 -- -1 -- 0 -- 1 -- 2 -- 3 -- 4 -->
    Integer negativo      cero     Integer positivo

Si pasamos por ejemplo 3.1416 sólo va aceptar 3.

¿Porqué es importante definir enteros?
-   Mal aprovechamiento de la memoria, los decimales ocupan más operaciones y espacio en memoria.

Tip: 
Usar enteros en la medida de lo posible y decimal solo cuando la situción lo amerite.

#### Variaciones de enteros
-   INT ->  Sólo se guardan números enteros.
            Valor mínimo: -2 147 483 648
            Valor máximo: 2 147 483 647
            Almacenamiento: 4 bytes
-   TINYINT ->  Sólo se guardan números enteros.
                Valor mínimo: -128
                Valor máximo: 127
                Almacenamiento: 1 byte
-   UNSIGNED TINYINT -> Sólo se guardan números enteros.
                        Valor mínimo: 0
                        Valor máximo: 255
                        Amacenamiento: 1 Byte
-   SMALLINT -> Sólo se guardan números enteros.
                Valor mínimo: -32768
                Valor máximo: 32767
                Almacenamiento: 2 bytes
-   MEDIUMINT ->    Sólo se guardan números enteros.
                    Valor mínimo: - 8 388 608
                    Valor máximo: 8 388 607
                    Almacenamiento: 3 bytes
-   BIGINT ->   Sólo se guardan números enteros.
                Valor mínimo: - 2 ^ 63
                Valor máximo: 2 ^ 63
                Almacenamiento: 4 byte

Practicamente siempre se utiliza INT, salvo muy pocos casos.

Función ZEROFILL
Coloca 0 adicionales a un número para dejar un largo estándar establecido.
INT 3
Con ZEROFILL 001  Sin zerofill 1

### DECIMALES

¿Cómo se les puede llamar?
-   FLOAT, DOUBLE, DECIMAL, NUMERIC, FIXED
En Posgrest se usa diferentes nomenclaturas.

Un número como 0.000000000000000000000000000000000000000001 es enorme en memoria.

En MySQL se ocupan de la siguiente forma:

DECIMAL(p, e)
p = presición, 3.14159265 -> el número de digitos totales antes y despues del punto p=8
e = escala, 3.14 e=2  

DECIMAL(5,2)
p=5 123.45000
e=2 123.45

# 💡 Tipo de Dato DECIMAL en MySQL

En MySQL, el tipo de dato **`DECIMAL(p, e)`** se utiliza para almacenar números decimales de manera precisa, especialmente en cálculos financieros o mediciones exactas.

---

## 🔍 ¿Qué significa cada parámetro?
- **`p` (precisión):** El número total de dígitos que puede almacenar el número, incluyendo los dígitos antes y después del punto decimal.  
- **`e` (escala):** El número de dígitos que aparecerán después del punto decimal.  

### 📌 Fórmula:
- **Número máximo de dígitos en total:** `p`  
- **Número de dígitos después del punto decimal:** `e`  
- **Número de dígitos antes del punto decimal:** `p - e`  

---

## 💡 Ejemplo: `DECIMAL(5, 2)`
En este caso:  
- `p = 5` → El número total de dígitos es 5.  
- `e = 2` → El número de díg

## DATOS BOOLEANOS

Dato con dos valores posibles:
- TRUE -> 1
- FALSE -> 0

## TIEMPOS Y FECHAS

Para guardar fechas en SQL se sigue el formato DATE:

DATE -> YYYY-MM-DD donde YYYY es el año, MM el mes y DD el día (2019-11-05)

Si tu pasas la fecha Miércoles 22 de Octubre del 1940 es diferente de 1940-10-22
 
TIME -> HH:MM:SS DONDE HH es hora, MM minutos y SS segundos en formto militar es decir 5:23:18 pm sería 17:23:18

DATETIME -> Es combinar Fecha y Tiempo YYYY-MM-DD HH:MM:SS es basicamente combinar la fecha y el tiempo.

TIMESTAMP -> Marca(estampa) de tiempo para saber cuando se modifica un registro YYYY-MM-DD HH:MM:SS

Se tiene también tenemos YEAR, MONTH, DAY

## Enum

Una lista de donde puedes seleccionar valores. No se vale agarrar fuera de la listita.

![alt text](image.png)

No se vale escribirlos de ninguna manera que yo no autorice, no se vae decir nada que yo no esté de acuerdo con eso.

ENUM ->  color ENUM('verde', 'blanco', 'rojo'); 

## BINARY LARGE OBJECT (BLOB)
Almacena datos no estructurados, como imágenes, notas de voz, o mezclas de estos.
Guardar datos no estructurado, no se recomneda guardarlos en una base de datos, lo que provoca es mucho peso en la DB y sea lenta.

TINYBLOB -> 255 bytes MÁXIMO
BLOB -> 65 KILOBYTES MÁXIMO
MIEDIUMBLOB -> 16MBYTES MÁXIMO
LONGBLOG -> 4 GIGABYTES MÁXIMO (Nunca usarlo practicamenete)

### JSON
Javascrit Object Notation

Sirve para guardar datos semi estructurados que vienen de internet, que se pueden guardar directamete en la base de datos.
Un twitter puede almacenarce como un JSON.

