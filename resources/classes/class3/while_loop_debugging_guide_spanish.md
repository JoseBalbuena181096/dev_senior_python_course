
# 🐛 Depuración de un Bucle `while` en Python

El bucle `while` es una estructura de control que repite un bloque de código mientras se cumpla una condición. Al depurar un bucle `while`, es importante entender cómo cambia la condición en cada iteración y verificar que la condición se actualice correctamente para evitar bucles infinitos.

## Ejemplo de Bucle a Depurar

Consideremos el siguiente bucle `while`, que genera la serie de Fibonacci hasta alcanzar un valor máximo especificado.

```python
maximo = 10
a, b = 0, 1

while a <= maximo:
    print(a)
    tempA = a
    a = b
    b = tempA + b
```

### Descripción del Código

Este bucle `while` genera la serie de Fibonacci siempre que el valor de `a` no supere el valor `maximo` especificado (en este caso, `10`).

### Iteración Paso a Paso

Supongamos que el usuario define `maximo = 10`. Vamos a analizar cada paso:

### **Iteración 1**
- **Valores Iniciales**: `a = 0`, `b = 1`, `maximo = 10`
- **Condición**: `a <= maximo` (0 <= 10), es **verdadera**.
- **Impresión**: `print(a)` imprime `0`
- **Actualización**:
  - `tempA = a` asigna `tempA = 0`.
  - `a = b` actualiza `a` a `1`.
  - `b = tempA + b` actualiza `b` a `0 + 1 = 1`.
- **Nuevos Valores**: `a = 1`, `b = 1`

### **Iteración 2**
- **Valores Iniciales**: `a = 1`, `b = 1`
- **Condición**: `a <= maximo` (1 <= 10), es **verdadera**.
- **Impresión**: `print(a)` imprime `1`
- **Actualización**:
  - `tempA = a` asigna `tempA = 1`.
  - `a = b` actualiza `a` a `1`.
  - `b = tempA + b` actualiza `b` a `1 + 1 = 2`.
- **Nuevos Valores**: `a = 1`, `b = 2`

### **Iteración 3**
- **Valores Iniciales**: `a = 1`, `b = 2`
- **Condición**: `a <= maximo` (1 <= 10), es **verdadera**.
- **Impresión**: `print(a)` imprime `1`
- **Actualización**:
  - `tempA = a` asigna `tempA = 1`.
  - `a = b` actualiza `a` a `2`.
  - `b = tempA + b` actualiza `b` a `1 + 2 = 3`.
- **Nuevos Valores**: `a = 2`, `b = 3`

### **Iteración 4**
- **Valores Iniciales**: `a = 2`, `b = 3`
- **Condición**: `a <= maximo` (2 <= 10), es **verdadera**.
- **Impresión**: `print(a)` imprime `2`
- **Actualización**:
  - `tempA = a` asigna `tempA = 2`.
  - `a = b` actualiza `a` a `3`.
  - `b = tempA + b` actualiza `b` a `2 + 3 = 5`.
- **Nuevos Valores**: `a = 3`, `b = 5`

### **Iteración 5**
- **Valores Iniciales**: `a = 3`, `b = 5`
- **Condición**: `a <= maximo` (3 <= 10), es **verdadera**.
- **Impresión**: `print(a)` imprime `3`
- **Actualización**:
  - `tempA = a` asigna `tempA = 3`.
  - `a = b` actualiza `a` a `5`.
  - `b = tempA + b` actualiza `b` a `3 + 5 = 8`.
- **Nuevos Valores**: `a = 5`, `b = 8`

### **Iteración 6**
- **Valores Iniciales**: `a = 5`, `b = 8`
- **Condición**: `a <= maximo` (5 <= 10), es **verdadera**.
- **Impresión**: `print(a)` imprime `5`
- **Actualización**:
  - `tempA = a` asigna `tempA = 5`.
  - `a = b` actualiza `a` a `8`.
  - `b = tempA + b` actualiza `b` a `5 + 8 = 13`.
- **Nuevos Valores**: `a = 8`, `b = 13`

### **Iteración 7**
- **Valores Iniciales**: `a = 8`, `b = 13`
- **Condición**: `a <= maximo` (8 <= 10), es **verdadera**.
- **Impresión**: `print(a)` imprime `8`
- **Actualización**:
  - `tempA = a` asigna `tempA = 8`.
  - `a = b` actualiza `a` a `13`.
  - `b = tempA + b` actualiza `b` a `8 + 13 = 21`.
- **Nuevos Valores**: `a = 13`, `b = 21`

### **Iteración 8 (Condición Falsa)**
- **Valores Iniciales**: `a = 13`, `b = 21`
- **Condición**: `a <= maximo` (13 <= 10), es **falsa**.
- **Fin del bucle**: El bucle se detiene.

## Resumen de la Salida

El bucle genera la serie de Fibonacci hasta el valor de 10:
```
0
1
1
2
3
5
8
```

## Consejos para Depurar Bucles `while`

- **Usa `print`**: Agrega impresiones dentro del bucle para observar el cambio en cada variable y la condición.
- **Verifica la Condición**: Asegúrate de que la condición del `while` pueda cambiar en cada iteración para evitar bucles infinitos.
- **Debuggers**: Usa herramientas de depuración en tu IDE para ejecutar el código paso a paso.

Este análisis detallado de cada iteración ayuda a entender cómo y cuándo el bucle `while` finaliza, asegurando que tu programa funcione como esperas. ¡Feliz depuración! 🐍🐛
