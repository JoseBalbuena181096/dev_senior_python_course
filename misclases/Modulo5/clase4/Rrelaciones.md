### Relaciones 1:1
Cada fila de la tabla se relecaiona con otra fila de otra tabla.

```

-- crear basede datos
CREATE DATABASE relaciones;

-- SELECCIONAR LA BASE DE DATOS 
USE relaciones;

-- tabla personas
create table Persona(
	id_persona INT primary key,
    nombre varchar(50)
);

-- Tabla pasaporte

create table Pasaporte(
	id_pasaporte int primary key,
    numero varchar(50),
    persona_id int unique,
    foreign key (persona_id) references Persona(id_persona)
);

```

Insertar una persona y un pasaporte debido a la relacion 
```
select * from Persona;
INSERT INTO `relaciones`.`Persona` (`id_persona`, `nombre`) VALUES ('1', 'Jose Palma');

select * from Pasaporte;
INSERT INTO `relaciones`.`Pasaporte` (`id_pasaporte`, `numero`, `persona_id`) VALUES ('1', '223211', '1');

```

### Relacion 1 a muchos (1:M)

Una fila de una tabla puede tener muchas filas en otra tabla (ejemplo un cliente puede tener muchos pedidos)

```
-- Tabla clientes
create table Clientes(
	id_cliente INT primary key,
    nombre varchar(50)
);

create table Pedidos(
	id_pedido int primary key,
    numero varchar(50),
    cliente_id int,
    foreign key (cliente_id) references Clientes(id_cliente)
);

```

Insertar elementos a la tabla de la siguiente forma dada las relaciones 
```

SELECT * FROM Clientes;
INSERT INTO `relaciones`.`Clientes` (`id_cliente`, `nombre`) VALUES ('1', 'Jose Palma');

SELECT * FROM Pedidos;
INSERT INTO `relaciones`.`Pedidos` (`id_pedido`, `numero`, `cliente_id`) VALUES ('1', '222', '1');
INSERT INTO `relaciones`.`Pedidos` (`id_pedido`, `numero`, `cliente_id`) VALUES ('2', '223', '1');

```

### Relacion muchos a muchas (M:M)
Varias filas de una tabla se relacionan con varias filas de otra tabla


```
-- Tabla Estudiante
create table Estudiantes(
	id_estudiante INT primary key,
    nombre varchar(50)
);

-- Tabla cursos
create table Curso(
	id_curso int primary key,
    nombre varchar(50)
);

-- Tabla intermedia: Estudiante curso

create table EstudianteCurso(
	estudiante_id int,
    curso_id int,
    primary key (estudiante_id, curso_id),
	foreign key (estudiante_id) references Estudiantes(id_estudiante),
    foreign key (curso_id) references Curso(id_curso)
);

```

### Crear base de datos biblioteca

-- crear basede datos
CREATE DATABASE biblioteca;

-- SELECCIONAR LA BASE DE DATOS 
USE biblioteca;

| Entidades  |Relaciones| 
|------------|----------|
| Libro      |    Libro -> Editorial -  Muchos a Uno (M:1) Muchos libros tienen una editorial|
| Autor      |    Libro <-> Autor  -  Muchos a Muchos (M:M) Muchos libros pueden tener Muchos autores|
| Editorial  |    Usuarios ->  Prestamo - Uno a Muchos (1:M)  Un usuario puede tener Muchos prestamos|
| Usuario    |    libro -> Prestamo - Uno a Muchos (1:M) Un libro puede tener Muchos Prestamos |
| Prestamo   |  |

-    Creacion de la base de datos biblioteca

```
-- Tabla Editorial
CREATE TABLE Editorial(
	id_editorial INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais VARCHAR(100),
    anio_fundacion INT
);

-- Tabla Autor
CREATE TABLE Autor(
	id_autor INT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE,
    biografia TEXT
);

-- Tabla Libro (Relacion uno a muchos(1:N))
CREATE TABLE Libro(
    id_libro INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    anio_publicacion INT,
    numero_paginas INT,
    genero VARCHAR(50),
    editorial_id INT,
    FOREIGN KEY (editorial_id) REFERENCES Editorial(id_editorial)
);

-- Table intermedia LibroAutor (Relacion muchos a muchos(N:N))S
CREATE TABLE LibroAutor(
    libro_id INT,
    autor_id INT,
    PRIMARY KEY (libro_id, autor_id),
    FOREIGN KEY (libro_id) REFERENCES Libro(id_libro),
    FOREIGN KEY (autor_id) REFERENCES Autor(id_autor)
);

-- Tabla Usuario
CREATE TABLE Usuario(
    id_usuario INT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla prestamo (Relacion uno a muchos(1:N))
CREATE TABLE Prestamo(
    id_prestamo INT PRIMARY KEY,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE,
    estado VARCHAR(20) DEFAULT 'pendiente', -- 'Pendiente', 'Devuelto', 'cancelado'
    usuario_id INT,
    libro_id INT,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (libro_id) REFERENCES Libro(id_libro)
);

-- Insert de prueba para todas las tablas

-- Editorial
INSERT INTO Editorial(id_editorial, nombre, pais, anio_fundacion)
VALUES (1, 'Editorial Planeta', 'Espa a', 1949),
       (2, 'Anagrama', 'Espa a', 1969),
       (3, 'Santillana', 'Argentina', 1960);

-- Autor
INSERT INTO Autor(id_autor, nombre_completo, nacionalidad, fecha_nacimiento, biografia)
VALUES (1, 'Gabriel Garcia Marquez', 'Colombia', '1927-03-06', 'Escritor colombiano ganador del Premio Nobel de Literatura en 1982'),
       (2, 'Ernesto S bato', 'Argentina', '1911-06-24', 'Escritor argentino'),
       (3, 'Julio Cort zar', 'Argentina', '1914-08-26', 'Escritor argentino');

-- Libro
INSERT INTO Libro(id_libro, titulo, isbn, anio_publicacion, numero_paginas, genero, editorial_id)
VALUES (1, 'Cien a os de soledad', '978-607-07-0366-8', 1967, 448, 'Novela', 1),
       (2, 'El t nel', '978-84-339-0416-4', 1959, 272, 'Novela', 2),
       (3, 'Rayuela', '978-950-49-1441-6', 1963, 560, 'Novela', 3);

-- LibroAutor
INSERT INTO LibroAutor(libro_id, autor_id)
VALUES (1, 1),
       (2, 2),
       (3, 3);

-- Usuario
INSERT INTO Usuario(id_usuario, nombre_completo, correo_electronico, telefono, direccion)
VALUES (1, 'Juan P rez', 'jperez@dominio.com', '1234567', 'Calle 1 # 2-3'),
       (2, 'Mar a G mez', 'mgomez@dominio.com', '9876543', 'Calle 2 # 4-5'),
       (3, 'Pedro L pez', 'plopez@dominio.com', '555-1234', 'Calle 3 # 6-7');

-- Prestamo
INSERT INTO Prestamo(id_prestamo, fecha_prestamo, fecha_devolucion, estado, usuario_id, libro_id)
VALUES (1, '2020-01-01', NULL, 'pendiente', 1, 1),
       (2, '2020-01-15', '2020-01-20', 'devuelto', 2, 2),
       (3, '2020-02-01', NULL, 'cancelado', 3, 3);
```

--   Consultas entre tablas (con JOIN)

```
-- Mostrar todos los prestamos con informacion de usuario y libro
SELECT 
    p.id_prestamo AS id_prestamo,
    U.nombre_completo AS nombre_usuario,
    L.titulo AS titulo_libro,
    P.fecha_prestamo,
    p.fecha_devolucion,
    p.estado
FROM prestamo P
JOIN usuario U ON P.usuario_id = U.id_usuario
JOIN libro L ON P.libro_id = L.id_libro;

```


```
-- Mostrar todos los prestamos con informacion de usuario y libro
SELECT 
    p.id_prestamo AS id_prestamo,
    U.nombre_completo AS nombre_usuario,
    L.titulo AS titulo_libro,
    P.fecha_prestamo,
    p.fecha_devolucion,
    p.estado,
    CASE
        WHEN p.estado = 'cancelado' THEN 'Prestamo cancelado'
        WHEN p.fecha_devolucion IS NULL THEN 'Libro aun no ha sido devuelto'
        ELSE 'Libro devuelto'
    END AS obsevacion
FROM prestamo P
JOIN usuario U ON P.usuario_id = U.id_usuario
JOIN libro L ON P.libro_id = L.id_libro;

--Opcion 2

SELECT 
    p.id_prestamo AS id_prestamo,
    U.nombre_completo AS nombre_usuario,
    L.titulo AS titulo_libro,
    P.fecha_prestamo,
    CASE
        WHEN p.estado = 'cancelado' THEN 'Prestamo cancelado'
        WHEN p.fecha_devolucion IS NULL THEN 'Libro aun no ha sido devuelto'
        ELSE DATE_FORMAT(p.fecha_devolucion, '%Y-%m-%d')
    END AS obsevacion,
	p.estado
FROM prestamo P
JOIN usuario U ON P.usuario_id = U.id_usuario
JOIN libro L ON P.libro_id = L.id_libro;


-- Opcion sin alias
SELECT 
    prestamo.id_prestamo,
    usuario.nombre_completo,
    libro.titulo,
    prestamo.fecha_prestamo,
    CASE
        WHEN prestamo.estado = 'cancelado' THEN 'Prestamo cancelado'
        WHEN prestamo.fecha_devolucion IS NULL THEN 'Libro aun no ha sido devuelto'
        ELSE DATE_FORMAT(prestamo.fecha_devolucion, '%Y-%m-%d')
    END AS fecha_devolucion,
    prestamo.estado

FROM prestamo
JOIN usuario ON prestamo.usuario_id = usuario.id_usuario
JOIN libro ON prestamo.libro_id = libro.id_libro;


-- Obtener todos los libros de un autor
SELECT
    L.titulo as Libro,
    A.nombre_completo as Autor, 
    L.isbn as Isbn
FROM Libro as L
JOIN LibroAutor as LA ON L.id_libro = LA.libro_id
JOIN Autor as A ON LA.autor_id = A.id_autor;

-- Obtener todos los libros de un autor
SELECT
    l.titulo AS libro, 
    A.nombre_completo AS autor,
    l.isbn
FROM Libro as l
JOIN LibroAutor as LA ON l.id_libro = LA.libro_id
JOIN Autor as A ON LA.autor_id = A.id_autor

-- Listar los libros por editorial
SELECT
    L.titulo AS libro, 
    E.nombre AS editorial,
    L.isbn
FROM Libro as L
JOIN Editorial as E ON L.editorial_id = E.id_editorial

-- Consultar los prestasmo realizados en una fecha especifica
SELECT 
    p.id_prestamo
FROM Prestamo p
JOIN Usuario u ON p.usuario_id = u.id_usuario
JOIN Libro l ON p.libro_id = l.id_libro
WHERE p.fecha_prestamo = '2020-01-01';

```

