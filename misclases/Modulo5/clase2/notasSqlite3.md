# PARA SQLITE3

-- Crear tabla Profesores
CREATE TABLE Profesores(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT,
  especialidad TEXT,
  experiencia INTEGER
);

-- Crear tabla Cursos con relación a Profesores
CREATE TABLE Cursos(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT,
  id_profesor INTEGER,
  FOREIGN KEY (id_profesor) REFERENCES Profesores(id)
);

-- Crear tabla Estudiantes con relación a Cursos
CREATE TABLE Estudiantes(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT,
  edad INTEGER,
  id_curso INTEGER,
  FOREIGN KEY (id_curso) REFERENCES Cursos(id)
);

-- Crear tabla Docentes
CREATE TABLE docentes(
  idDocente INTEGER PRIMARY KEY,
  nombre TEXT,
  edad INTEGER,
  facultad TEXT
);

-- Insertar 3 registros en la tabla Profesores
INSERT INTO Profesores (nombre, especialidad, experiencia) VALUES
('Jesus Palma', 'Programación', 4),
('María García', 'Desarrollo Web', 7),
('Carlos Rodríguez', 'Inteligencia Artificial', 6);

-- Insertar 3 registros en la tabla Cursos
INSERT INTO Cursos (nombre, id_profesor) VALUES
('Python', 1),
('C++', 2),
('Java', 3);

-- Insertar 3 registros en la tabla Estudiantes
INSERT INTO Estudiantes (nombre, edad, id_curso) VALUES
('Jose Balbuena', 28, 3),
('Jesus Balbuena', 26, 2),
('Maria Palma', 32, 1);

-- Insertar 3 registros en la tabla Docentes
INSERT INTO docentes (idDocente, nombre, edad, facultad) VALUES
(1, 'Ana Martínez', 45, 'Ciencias de la Computación'),
(2, 'Luis Fernández', 52, 'Ingeniería de Software'),
(3, 'Sofía López', 38, 'Sistemas de Información');