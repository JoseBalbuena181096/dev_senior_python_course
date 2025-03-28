## Crear la base de datos
```
CREATE DATABASE AcademiaDevSenior;
```

## Usar la base de datos

```
USE AcademiaDevSenior;
```


## Crear la tabla de estudiantes
```
CREATE TABLE Estudiantes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    edad INT,
    curso VARCHAR(100)
);
```

## Seleccionar la tabla de estudiantes
```
SELECT * FROM Estudiantes;
```

## Crear Tabla docentes

```
CREATE TABLE `academiadevsenior`.`docentes` (
  `idDocente` INT NOT NULL,
  `nombre` VARCHAR(100) NULL,
  `edad` INT NULL,
  `facultad` VARCHAR(100) NULL,
  PRIMARY KEY (`idDocente`));

```
## Insertar un estudiante

```
INSERT INTO Estudiantes(nombre, edad, curso) VALUES
('Jose Balbuena', 28, 'Programación'),
('Jesus Balbuena', 29, 'Programación');
```

```
\# Esto es un comentario en mysql, lleva gato al inicio
```

## Consultar solo algunos campos
```
SELECT nombre, curso FROM Estudiantes;
```

## Filtrar los datos

```
SELECT * FROM Estudiantes WHERE edad > 28;
```

## Actualizar datos
```
UPDATE Estudiantes SET curso = 'Ingenieria Sofware' WHERE id = 1;
```

## Eliminar datos

```
DELETE FROM Estudiantes WHERE id = 2;
```

## Usar Carbon para compartir codigo
```
https://carbon.now.sh/

```
## Crear tabla Profesores

```
CREATE TABLE Profesores(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  especialidad VARCHAR(50),
  experiencia INT
);
```

## Agregar 10 profesores y 10 estudiandes

```
INSERT INTO Estudiantes(nombre, edad, curso) VALUES
('Jose Palma', 18, 'Python'),
('María González', 22, 'Java'),
('Carlos Rodríguez', 20, 'JavaScript'),
('Ana Martínez', 19, 'Python'),
('Luis Fernández', 21, 'C++'),
('Sofía López', 17, 'JavaScript'),
('Diego Sánchez', 23, 'Java'),
('Laura Torres', 20, 'Python'),
('Juan Pérez', 18, 'C#'),
('Elena Ramírez', 19, 'JavaScript');
```
```
INSERT INTO Profesores(nombre, especialidad, experiencia) VALUES
('Jesus Palma', 'Programación', '4'),
('María García', 'Desarrollo Web', '7'),
('Carlos Rodríguez', 'Inteligencia Artificial', '6'),
('Ana Martínez', 'Bases de Datos', '5'),
('Luis Fernández', 'Redes y Sistemas', '8'),
('Sofía López', 'Ciberseguridad', '3'),
('Diego Sánchez', 'Programación Móvil', '5'),
('Laura Torres', 'Machine Learning', '6'),
('Juan Pérez', 'Cloud Computing', '4'),
('Elena Ramírez', 'Desarrollo de Software', '7');
```

## Actualizar la especialidad de un profesor


### Por id la forma correcta
```
UPDATE Profesores SET especialidad = 'Ciberseguridad' WHERE nombre = 'Ana Martínez';
```

### Por todo menos la primary key desactivando el modo seguro

```
SET SQL_SAFE_UPDATES = 0;
UPDATE Profesores SET especialidad = 'Ciberseguridad' WHERE nombre = 'Ana Martínez';
SET SQL_SAFE_UPDATES = 1;  
```

## Eliminar un elemento de una tabla


### Por id la forma correcta

```
DELETE FROM Profesores WHERE id = 3;
```

### Por todo menos la primary key desactivando el modo seguro

```
SET SQL_SAFE_UPDATES = 0;
DELETE FROM Profesores WHERE nombre = 'Sofía López';
SET SQL_SAFE_UPDATES = 1;
```


## Crear una tabla de cursos que se relacione con la de profesores
```
CREATE TABLE Cursos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    id_profesor INT,
    FOREIGN KEY (id_profesor) REFERENCES profesores(id)
);

```

Esto crea una relación uno a muchos de profesores a cursos porque:

Estructura de la clave foránea


id_profesor INT permite múltiples registros con el mismo valor de profesor
FOREIGN KEY (id_profesor) REFERENCES profesores(id) vincula cada curso a un profesor específico


Interpretación práctica


Un profesor puede tener múltiples cursos
Cada curso solo puede tener un profesor asignado
La base de datos permite que un mismo ID de profesor se repita en varios registros de cursos

Ejemplo para ilustrar:
## Tabla Profesores

```
INSERT INTO profesores (id, nombre) VALUES 
(1, 'Juan Pérez'),
(2, 'María García');
```

### Tabla Cursos
INSERT INTO Cursos (nombre, id_profesor) VALUES
('Matemáticas', 1),  -- Curso de Juan Pérez
('Física', 1),       -- Otro curso de Juan Pérez
('Biología', 2);     -- Curso de María García
En este ejemplo, Juan Pérez (id 1) tiene dos cursos, mientras que María García (id 2) tiene un curso, demostrando la relación uno a muchos.
Características clave:

Un profesor puede tener N cursos
Cada curso tiene solo 1 profesor
La clave foránea permite esta cardinalidad


## Crear una relación de estudiantes a cursos

```
ALTER TABLE Estudiantes 
ADD COLUMN id_curso INT,
ADD FOREIGN KEY (id_curso) REFERENCES Cursos(id);
```

Se establece una relación uno a muchos de Cursos a Estudiantes:

Un curso puede tener múltiples estudiantes
Cada estudiante pertenece a un único curso

Características de la relación:

Un registro en la tabla Cursos puede estar relacionado con varios registros en la tabla Estudiantes
Cada estudiante solo puede estar asociado a un curso a la vez


#### Insertar cursos
```
INSERT INTO Cursos (id, nombre, id_profesor) VALUES 
(1, 'Python', 2),
(2, 'C++', 1),
(3, 'Java', 3);
```

### No se puede eliminar una tabla si esta esta referenciada en otra tabla, se tiene que eliminar la referencia primero o eliminar primero la tabla que tiene la referencia de otra.



### Eliminar los elementos de la tabla estudiantes y reiniciar el contador 

```
SET SQL_SAFE_UPDATES = 0;
DELETE FROM Estudiantes;
SET SQL_SAFE_UPDATES = 1;

TRUNCATE TABLE Estudiantes;

```

### Eliminar la columna curso de Estudiantes

```
ALTER TABLE Estudiantes
DROP COLUMN curso;
```


### Insertar estudiantes con relaciones

```
INSERT INTO Estudiantes(nombre, edad, id_curso) VALUES
('Jose Balbuena', 28, 3),
('Jesus Balbuena', 26, 2),
('Maria Palma', 32, 1),
('Monse Palma', 33, 1);
```

### Unir la tabla cursos y estudiantes 

```
SELECT Estudiantes.nombre, Cursos.nombre AS Curso
FROM Estudiantes
JOIN Cursos ON Estudiantes.id_curso = Cursos.id;
```


