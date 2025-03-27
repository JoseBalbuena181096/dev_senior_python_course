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
