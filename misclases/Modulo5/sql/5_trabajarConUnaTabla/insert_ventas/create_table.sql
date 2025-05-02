CREATE TABLE IF NOT EXISTS ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_venta DATE NOT NULL,
    id_producto INT NOT NULL,
    id_zona INT NOT NULL,
    venta DECIMAL(10,2) NOT NULL,
    id_vendedor INT NOT NULL,
    id_cliente INT NOT NULL
); 