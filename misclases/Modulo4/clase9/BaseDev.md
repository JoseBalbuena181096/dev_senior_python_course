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
