
# 🐍 Fundamentos de Programación en Python

¡Bienvenidos! En este archivo, aprenderás los fundamentos básicos de programación en Python. Este es el primer paso para convertirte en un programador. ¡Empecemos! 🚀

## 1. Variables 📦
Las variables son "cajas" donde podemos almacenar información. En Python, se crean de manera sencilla:

```python
nombre = "Juan"
edad = 25
altura = 1.75
```

En este ejemplo:
- `nombre` almacena una cadena de texto (string) `"Juan"`.
- `edad` almacena un número entero (int) `25`.
- `altura` almacena un número decimal (float) `1.75`.

## 2. Tipos de Datos 📊
Python maneja varios tipos de datos que te permiten trabajar con información de diferentes formas:

- **Enteros** (`int`): Números sin decimales, por ejemplo, `42`.
- **Flotantes** (`float`): Números con decimales, como `3.14`.
- **Cadenas** (`str`): Texto, por ejemplo, `"Hola, mundo"`.
- **Booleanos** (`bool`): Valores de `True` o `False`.

### Ejemplos
```python
es_estudiante = True  # Booleano
pi = 3.14159          # Flotante
mensaje = "Hola"      # Cadena
```

## 3. Operadores Aritméticos ➕➖✖️➗
Los operadores aritméticos se usan para hacer cálculos matemáticos:

- `+` : Suma
- `-` : Resta
- `*` : Multiplicación
- `/` : División
- `//` : División entera
- `%` : Módulo (resto de una división)
- `**` : Potencia

### Ejemplo
```python
a = 10
b = 3
suma = a + b       # 13
resta = a - b      # 7
multiplicacion = a * b  # 30
division = a / b   # 3.3333
modulo = a % b     # 1
potencia = a ** b  # 1000
```

## 4. Operadores Relacionales 🔍
Los operadores relacionales comparan valores y devuelven un valor booleano (`True` o `False`):

- `==` : Igual a
- `!=` : Diferente de
- `>` : Mayor que
- `<` : Menor que
- `>=` : Mayor o igual que
- `<=` : Menor o igual que

### Ejemplo
```python
x = 5
y = 10
print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
```

## 5. Operadores Lógicos 🔗
Los operadores lógicos se usan para combinar expresiones lógicas:

- `and` : Devuelve `True` si ambas expresiones son verdaderas.
- `or` : Devuelve `True` si al menos una de las expresiones es verdadera.
- `not` : Invierte el valor de una expresión (si es `True`, lo convierte en `False` y viceversa).

### Ejemplo
```python
es_adulto = True
tiene_permiso = False
puede_entrar = es_adulto and tiene_permiso  # False
puede_entrar_otra_condicion = es_adulto or tiene_permiso  # True
```

## 6. Tipos de Operaciones 🔢
Python permite realizar diferentes tipos de operaciones, como:

- **Operaciones Matemáticas**: Sumas, restas, multiplicaciones, etc.
- **Comparaciones**: Comparar valores para tomar decisiones.
- **Operaciones Lógicas**: Combinar múltiples condiciones para verificar si son verdaderas o falsas.

### Ejemplo Completo
```python
a = 10
b = 5
es_mayor = a > b  # True
es_igual = a == b  # False

resultado = es_mayor and not es_igual  # True
```

## 🎉 ¡Listo para Programar!
Con estos conceptos básicos, ya puedes empezar a escribir tus primeros programas en Python. Practica creando variables, haciendo cálculos, y combinando condiciones. ¡Diviértete explorando el mundo de Python! 🐍✨
