# Bases de Datos: SQL y NoSQL

## Tipos de Bases de Datos

### SQL (Bases de Datos Relacionales)
Las bases de datos relacionales se basan en el lenguaje SQL, organizando la información en:
- Tablas
- Filas
- Columnas 
- Relaciones entre datos

#### Ejemplos de Bases de Datos Relacionales
- MySQL
- PostgreSQL
- SQLite
- Oracle
- Microsoft SQL Server

### NoSQL (Bases de Datos No Relacionales)
Bases de datos que no utilizan el modelo relacional tradicional basado en SQL.

#### Ejemplos de Bases de Datos NoSQL
- MongoDB (Documental)
- Redis (Clave-Valor)
- Cassandra (Columnar)
- Neo4j (Grafos)
- DynamoDB (Clave-Valor)

## ¿Qué es SQL? 

**SQL (Structured Query Language)** es un lenguaje de programación especializado para:
- Administrar bases de datos relacionales
- Manipular datos estructurados
- Realizar consultas complejas

### Funciones Principales de SQL

#### 1. Consulta de Datos (SELECT)
- Extrae información específica de una base de datos
- Capacidades avanzadas:
  - Filtrar resultados
  - Ordenar datos
  - Agrupar información
  - Realizar cálculos y agregaciones

#### 2. Manipulación de Datos
- **INSERT**: Agregar nuevos registros
- **UPDATE**: Modificar datos existentes
- **DELETE**: Eliminar registros
- **MERGE**: Combinar operaciones de inserción y actualización

#### 3. Definición de Datos (DDL - Data Definition Language)
- **CREATE TABLE**: Crear nuevas estructuras de datos
- **ALTER TABLE**: Modificar estructuras existentes
- **DROP TABLE**: Eliminar tablas completas
- **TRUNCATE**: Eliminar todos los registros de una tabla

#### 4. Control de Datos (DCL - Data Control Language)
- Gestionar permisos de usuarios
- Controlar acceso a la información
- Mantener integridad de datos
- **GRANT**: Otorgar permisos
- **REVOKE**: Revocar permisos

### Características Avanzadas de SQL

#### Integridad de Datos
- Restricciones (CONSTRAINTS)
- Claves primarias y foráneas
- Validaciones de datos

#### Transacciones
- Garantizan operaciones atómicas
- Aseguran consistencia de datos
- Implementan principios ACID:
  - Atomicidad
  - Consistencia
  - Aislamiento
  - Durabilidad

### Ejemplo Práctico de Consulta SQL
```sql
-- Consulta para obtener usuarios mayores de 18 años, ordenados por edad
SELECT nombre, edad 
FROM usuarios 
WHERE edad >= 18 
ORDER BY edad DESC;
```

### Comparación SQL vs NoSQL

| Característica | SQL | NoSQL |
|---------------|-----|-------|
| Estructura | Rígida, esquema predefinido | Flexible, esquema dinámico |
| Escalabilidad | Vertical | Horizontal |
| Consistencia | Alta | Configurable |
| Uso típico | Transacciones complejas | Big Data, tiempo real |

## Consideraciones Finales

### Cuándo Usar SQL
- Aplicaciones con esquema de datos complejo
- Necesidad de transacciones ACID
- Relaciones complejas entre datos
- Sistemas financieros
- Aplicaciones empresariales

### Cuándo Usar NoSQL
- Grandes volúmenes de datos
- Datos sin estructura definida
- Alto rendimiento y escalabilidad
- Aplicaciones en tiempo real
- Sistemas de big data

**Nota**: La elección depende de los requisitos específicos de cada proyecto.

<hr/>

# Bases de Datos SQL: Estructura y Conceptos Fundamentales

## Introducción
Las bases de datos SQL son sistemas para almacenar y gestionar información de manera estructurada y eficiente.

## Componentes Principales de una Tabla

### 1. Filas (Registros)
- Representan una entrada individual en la tabla
- Cada fila contiene datos específicos para un elemento único
- **Ejemplo**: En una tabla de Empleados, cada fila representa un empleado concreto

### 2. Columnas (Campos)
- Definen los tipos de información almacenados
- Cada columna tiene un tipo de dato específico
- Representan características o atributos de los registros
- **Ejemplo**: Nombre, Apellido, Salario, Fecha de Contratación

## Claves (Keys)

### Primary Key (Clave Primaria)
- Identificador único para cada registro en una tabla
- Garantiza la unicidad de los registros
- No puede contener valores nulos

#### Ejemplo de Sintaxis
```sql
CREATE TABLE Empleados (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Salario DECIMAL(10,2)
);
```

### Foreign Key (Clave Foránea)
- Establece relaciones entre tablas
- Hace referencia a la primary key de otra tabla
- Mantiene la integridad referencial

#### Ejemplo de Implementación
```sql
CREATE TABLE Departamentos (
    DepartamentoID INT PRIMARY KEY,
    NombreDepartamento VARCHAR(50)
);

CREATE TABLE Empleados (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    DepartamentoID INT,
    FOREIGN KEY (DepartamentoID) REFERENCES Departamentos(DepartamentoID)
);
```

## Tipos de Relaciones

### 1. One-to-One (Uno a Uno)
- Cada registro de una tabla se relaciona con un único registro de otra tabla

### 2. One-to-Many (Uno a Muchos)
- Un registro de una tabla puede relacionarse con múltiples registros de otra tabla

### 3. Many-to-Many (Muchos a Muchos)
- Múltiples registros de una tabla se relacionan con múltiples registros de otra tabla

## Beneficios del Modelo Relacional
- Previene la redundancia de datos
- Mantiene la consistencia de la información
- Permite consultas complejas
- Facilita la organización de grandes volúmenes de información

## Consideraciones Importantes
- La estructura de las tablas debe diseñarse cuidadosamente
- Las relaciones entre tablas deben ser claras y lógicas
- Es fundamental mantener la integridad de los datos


# Relaciones en Bases de Datos SQL: Ejemplos Prácticos

## 1. Relación One-to-One (Uno a Uno)
### Ejemplo: Usuarios y Perfiles de Usuario

```sql
-- Tabla de Usuarios
CREATE TABLE Usuarios (
    UsuarioID INT PRIMARY KEY,
    Username VARCHAR(50) UNIQUE,
    Email VARCHAR(100) UNIQUE
);

-- Tabla de Perfiles
CREATE TABLE Perfiles (
    PerfilID INT PRIMARY KEY,
    UsuarioID INT UNIQUE,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    FechaNacimiento DATE,
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID)
);
```
**Explicación**: Cada usuario tiene exactamente un perfil, y cada perfil pertenece a un único usuario.

## 2. Relación One-to-Many (Uno a Muchos)
### Ejemplo: Departamentos y Empleados

```sql
-- Tabla de Departamentos
CREATE TABLE Departamentos (
    DepartamentoID INT PRIMARY KEY,
    NombreDepartamento VARCHAR(50),
    Ubicacion VARCHAR(100)
);

-- Tabla de Empleados
CREATE TABLE Empleados (
    EmpleadoID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    DepartamentoID INT,
    Salario DECIMAL(10,2),
    FOREIGN KEY (DepartamentoID) REFERENCES Departamentos(DepartamentoID)
);
```
**Explicación**: Un departamento puede tener múltiples empleados, pero cada empleado pertenece a un solo departamento.

## 3. Relación Many-to-Many (Muchos a Muchos)
### Ejemplo: Estudiantes y Cursos

```sql
-- Tabla de Estudiantes
CREATE TABLE Estudiantes (
    EstudianteID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Email VARCHAR(100)
);

-- Tabla de Cursos
CREATE TABLE Cursos (
    CursoID INT PRIMARY KEY,
    NombreCurso VARCHAR(100),
    Profesor VARCHAR(100)
);

-- Tabla de Inscripciones (Tabla Puente)
CREATE TABLE Inscripciones (
    InscripcionID INT PRIMARY KEY,
    EstudianteID INT,
    CursoID INT,
    FechaInscripcion DATE,
    FOREIGN KEY (EstudianteID) REFERENCES Estudiantes(EstudianteID),
    FOREIGN KEY (CursoID) REFERENCES Cursos(CursoID)
);
```
**Explicación**: 
- Un estudiante puede inscribirse en múltiples cursos
- Un curso puede tener múltiples estudiantes
- Se utiliza una tabla puente (Inscripciones) para gestionar esta relación compleja

## 4. Ejemplo Complejo: Sistema de Biblioteca

```sql
-- Tabla de Autores
CREATE TABLE Autores (
    AutorID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Nacionalidad VARCHAR(50)
);

-- Tabla de Libros
CREATE TABLE Libros (
    LibroID INT PRIMARY KEY,
    Titulo VARCHAR(100),
    AñoPublicacion INT,
    AutorID INT,
    FOREIGN KEY (AutorID) REFERENCES Autores(AutorID)
);

-- Tabla de Préstamos
CREATE TABLE Prestamos (
    PrestamoID INT PRIMARY KEY,
    LibroID INT,
    UsuarioID INT,
    FechaPrestamo DATE,
    FechaDevolucion DATE,
    FOREIGN KEY (LibroID) REFERENCES Libros(LibroID),
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID)
);
```
**Explicación**:
- Relación One-to-Many entre Autores y Libros
- Relación Many-to-Many entre Libros y Usuarios a través de la tabla Préstamos

## Consideraciones Importantes
- Las claves foráneas mantienen la integridad referencial
- El diseño de la base de datos debe reflejar las relaciones lógicas del mundo real
- Las relaciones ayudan a organizar y estructurar la información de manera eficiente

# Comandos MySQL por Terminal

## Conexión y Bases de Datos

### 1. Conectarse a MySQL
```bash
mysql -u usuario -p
```
Reemplaza "usuario" con tu nombre de usuario de MySQL. Se te pedirá introducir la contraseña.

### 2. Mostrar Bases de Datos
```sql
SHOW DATABASES;
```

### 3. Crear Base de Datos
```sql
CREATE DATABASE nombre_base_datos;
```

### 4. Seleccionar Base de Datos
```sql
USE nombre_base_datos;
```

## Gestión de Tablas

### 5. Mostrar Tablas
```sql
SHOW TABLES;
```

### 6. Crear Tabla
```sql
CREATE TABLE nombre_tabla (
    columna1 tipo_dato,
    columna2 tipo_dato,
    PRIMARY KEY (columna1)
);
```

## Operaciones con Datos

### 7. Insertar Datos
```sql
INSERT INTO nombre_tabla (columna1, columna2) 
VALUES ('valor1', 'valor2');
```

### 8. Consultar Datos
```sql
-- Mostrar todos los registros
SELECT * FROM nombre_tabla;

-- Consulta con condiciones
SELECT * FROM nombre_tabla WHERE condicion;
```

### 9. Actualizar Registros
```sql
UPDATE nombre_tabla 
SET columna1 = 'nuevo_valor' 
WHERE condicion;
```

### 10. Eliminar Registros
```sql
DELETE FROM nombre_tabla WHERE condicion;
```

## Comandos Generales

### 11. Salir de MySQL
```sql
EXIT;
```

## Comandos de Terminal

### 12. Exportar Base de Datos
```bash
mysqldump -u usuario -p nombre_base_datos > respaldo.sql
```

### 13. Importar Base de Datos
```bash
mysql -u usuario -p nombre_base_datos < respaldo.sql
```

## Consejos Importantes

- Termina siempre las sentencias SQL con punto y coma (`;`)
- Reemplaza "usuario", "nombre_base_datos", "nombre_tabla" con tus valores específicos
- Usa comillas simples para valores de texto
- Ten precaución con los comandos `DELETE` y `UPDATE`
- Verifica siempre las condiciones `WHERE` antes de ejecutar

## Tipos de Datos Comunes

- `INT`: Números enteros
- `VARCHAR(n)`: Cadenas de texto de longitud variable
- `DATE`: Fechas
- `DECIMAL(m,n)`: Números decimales
- `BOOLEAN`: Valores verdadero/falso

## Ejemplos Prácticos

### Crear Tabla de Usuarios
```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    fecha_registro DATE
);
```

### Insertar Usuario
```sql
INSERT INTO usuarios (nombre, email, fecha_registro) 
VALUES ('Juan Pérez', 'juan@ejemplo.com', '2024-03-25');
```

### Consulta Avanzada
```sql
SELECT nombre, email 
FROM usuarios 
WHERE fecha_registro > '2024-01-01';
```

**Nota**: Siempre realiza copias de seguridad antes de hacer cambios importantes en tus bases de datos.

## 3. Verificación de Puerto desde Cliente MySQL

### Paso a Paso

#### Conectarse a MySQL
```bash
mysql -u root -p
```
- Presiona Enter
- Introduce tu contraseña de MySQL

### Comandos dentro del Cliente MySQL

#### 1. Mostrar Puerto Actual
```sql
SHOW VARIABLES LIKE 'port';
```
- Mostrará el puerto actual de conexión
- Generalmente aparecerá como `3306`

#### 2. Información Detallada del Servidor
```sql
STATUS;
```
- Muestra información completa del servidor
- Incluye detalles de conexión y puerto

#### 3. Consultar Variables de Conexión
```sql
SELECT @@port;
```
- Método alternativo para mostrar puerto
- Devuelve directamente el número de puerto

### Ejemplos de Salida

```
mysql> SHOW VARIABLES LIKE 'port';
+---------------+-------+
| Variable_Name | Value |
+---------------+-------+
| port          | 3306  |
+---------------+-------+
```

### Consejos Importantes

- Asegúrate de tener permisos de acceso
- La contraseña distingue mayúsculas/minúsculas
- El puerto predeterminado es 3306
- Algunos servidores pueden usar puertos personalizados

### Solución de Problemas

Si no puedes conectarte:
- Verifica credenciales
- Confirma que el servicio MySQL está activo
- Revisa configuraciones de firewall

### Salir del Cliente MySQL
```sql
EXIT;
```
o 
```sql
\q
```

**Nota**: Los comandos pueden variar ligeramente según la versión de MySQL.

# Modificar Puerto MySQL en Windows

## Método 1: MySQL Workbench
1. Abrir MySQL Workbench
2. Conectar al servidor local
3. Ir a: Server > Options File
4. Buscar o agregar línea `port=nuevo_numero_puerto`
5. Guardar cambios
6. Reiniciar servicio MySQL

## Método 2: Archivo my.ini
1. Ubicar archivo `my.ini`
   - Ruta típica: `C:\ProgramData\MySQL\MySQL Server X.X\`
   - X.X = Versión de MySQL

2. Editar archivo
```ini
# Buscar o agregar línea
port=3307
```

## Método 3: Línea de Comandos
```cmd
# Detener servicio MySQL
net stop mysql

# Configurar nuevo puerto
mysqld --port=3307

# Reiniciar servicio
net start mysql
```

## Verificar Nuevo Puerto
```cmd
# Verificar puertos en uso
netstat -ano | findstr :3306
netstat -ano | findstr :3307
```

## Configuración en Firewall
1. Panel de Control
2. Sistema y Seguridad
3. Firewall de Windows
4. Configuración avanzada
5. Crear nueva regla de entrada para nuevo puerto

## Consideraciones
- Respaldar configuración
- Actualizar cadenas de conexión
- Reiniciar servicios
- Verificar permisos

**Nota**: Los pasos pueden variar según versión de MySQL