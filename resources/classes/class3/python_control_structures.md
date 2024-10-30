
# 🔄 Estructuras de Control de Flujo en Python

En Python, las estructuras de control de flujo nos permiten tomar decisiones y repetir acciones en nuestro programa. En esta documentación, exploraremos las **condicionales** y los **bucles** básicos que puedes usar para hacer tu código más dinámico y flexible. ¡Vamos a descubrir cómo funcionan! 🚀

## 1. **Condicionales: `if`, `else`, `elif`** 🧩

Las condicionales te permiten ejecutar diferentes bloques de código según ciertas condiciones. Es como decirle a tu programa: "si ocurre esto, haz esto otro".

### 🌟 **¿Cómo se usan?**
- `if`: Se usa para verificar si una condición es verdadera.
- `elif`: Significa "else if" y se usa para añadir más condiciones si la primera no se cumple.
- `else`: Se ejecuta si ninguna de las condiciones anteriores es verdadera.

### 📋 **Ejemplo**
```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad 🎉")
elif edad >= 13:
    print("Eres un adolescente 😊")
else:
    print("Eres un niño 👶")
```
En este ejemplo:
- Si `edad` es mayor o igual a 18, se imprime "Eres mayor de edad 🎉".
- Si no, pero `edad` es mayor o igual a 13, se imprime "Eres un adolescente 😊".
- De lo contrario, se imprime "Eres un niño 👶".

### ✅ **Beneficios**:
- Permiten que el programa tome decisiones en tiempo real.
- Hacen el código más dinámico y adaptable a diferentes situaciones.

## 2. **Bucles: `for` y `while`** 🔄

Los bucles te permiten repetir un bloque de código varias veces. Esto es útil cuando necesitas realizar la misma acción múltiples veces sin tener que escribir el mismo código una y otra vez.

### 2.1 **Bucle `for`** ➰

El bucle `for` se usa cuando se sabe de antemano cuántas veces queremos repetir una acción (por ejemplo, al iterar sobre una lista o un rango de números).

### 📋 **Ejemplo**
```python
for iteration in range(10):
    print(f"This is the iteration number: {iteration}")
```
En este ejemplo, el bucle `for` recorre cada numero dentro del rango 0-9 y ejecuta el bloque de código para cada uno.

### 2.2 **Bucle `while`** 🔁

El bucle `while` se usa cuando no se sabe cuántas veces se repetirá una acción y depende de una condición que puede cambiar durante la ejecución.

### 📋 **Ejemplo**
```python
contador = 1

while contador <= 5:
    print(f"Este es el número {contador}")
    contador += 1
```
Aquí, el bucle `while` continúa ejecutándose mientras `contador` sea menor o igual a 5.

### 🔍 **¿Cómo saber cuál usar?**
- Usa `for` cuando sabes de antemano cuántas veces se ejecutará el bucle (por ejemplo, al recorrer una lista o un rango de números).
- Usa `while` cuando la cantidad de iteraciones dependa de una condición que puede cambiar dentro del bucle.

## 🎯 **Consejos y Buenas Prácticas**
- **Evita bucles infinitos**: Cuando uses `while`, asegúrate de que la condición eventualmente se vuelva falsa para que el bucle se detenga.
- **Usa `break` y `continue` cuando sea necesario**:
  - `break` se usa para salir de un bucle antes de que termine.
  - `continue` salta a la siguiente iteración, omitiendo el código que está después de él en esa vuelta.

### 📋 **Ejemplo de `break` y `continue`**
```python
for numero in range(1, 6):
    if numero == 3:
        print("Número 3 encontrado, saliendo del bucle.")
        break  # Sale del bucle cuando encuentra el número 3
    print(numero)

for numero in range(1, 6):
    if numero == 3:
        print("Saltando el número 3.")
        continue  # Salta a la siguiente iteración cuando encuentra el número 3
    print(numero)
```

## 🎉 ¡Listo para Programar!
Con estas estructuras de control, puedes hacer que tu programa tome decisiones y repita acciones de manera eficiente. ¡Experimenta con `if`, `for`, y `while` para ver cómo puedes hacer que tu código sea más dinámico y flexible! 💪🐍