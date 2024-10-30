
# 🐛 Depuración de un Bucle `for` en Python

La depuración de un bucle `for` es fundamental para entender el comportamiento de cada iteración, especialmente cuando trabajamos con lógica compleja como en la generación de la serie de Fibonacci. En esta guía, explicaremos cómo depurar un bucle `for` en Python, detallando cada iteración paso a paso para comprender el flujo y verificar el correcto funcionamiento.

## Ejemplo de Bucle a Depurar

Consideremos el siguiente bucle `for`, que genera la serie de Fibonacci hasta el número de términos especificado.

```python
terminos = 5

a, b = 0, 1
for i in range(terminos):
    print(a)
    tempA = a
    a = b
    b = tempA + b
```

### Descripción del Código

Este bucle genera la serie de Fibonacci siguiendo los siguientes pasos:
1. **Inicializa `a` y `b`**: El primer término `a` comienza en 0 y el segundo término `b` en 1.
2. **Iteración del bucle**: Cada iteración del bucle genera el siguiente número de la serie de Fibonacci y actualiza los valores de `a` y `b`.
3. **Variable Temporal**: Utiliza una variable temporal `tempA` para almacenar el valor actual de `a`, de modo que el cálculo de `b` sea correcto.

### Iteración Paso a Paso

Supongamos que el usuario ingresa `terminos = 5`. Vamos a analizar cada paso:

### **Iteración 1 (i = 0)**
- **Valores Iniciales**: `a = 0`, `b = 1`
- **Impresión**: `print(a)` imprime `0`
- **Actualización**:
  - `tempA = a` asigna `tempA = 0`.
  - `a = b` actualiza `a` a `1`.
  - `b = tempA + b` actualiza `b` a `0 + 1 = 1`.
- **Nuevos Valores**: `a = 1`, `b = 1`

### **Iteración 2 (i = 1)**
- **Valores Iniciales**: `a = 1`, `b = 1`
- **Impresión**: `print(a)` imprime `1`
- **Actualización**:
  - `tempA = a` asigna `tempA = 1`.
  - `a = b` actualiza `a` a `1`.
  - `b = tempA + b` actualiza `b` a `1 + 1 = 2`.
- **Nuevos Valores**: `a = 1`, `b = 2`

### **Iteración 3 (i = 2)**
- **Valores Iniciales**: `a = 1`, `b = 2`
- **Impresión**: `print(a)` imprime `1`
- **Actualización**:
  - `tempA = a` asigna `tempA = 1`.
  - `a = b` actualiza `a` a `2`.
  - `b = tempA + b` actualiza `b` a `1 + 2 = 3`.
- **Nuevos Valores**: `a = 2`, `b = 3`

### **Iteración 4 (i = 3)**
- **Valores Iniciales**: `a = 2`, `b = 3`
- **Impresión**: `print(a)` imprime `2`
- **Actualización**:
  - `tempA = a` asigna `tempA = 2`.
  - `a = b` actualiza `a` a `3`.
  - `b = tempA + b` actualiza `b` a `2 + 3 = 5`.
- **Nuevos Valores**: `a = 3`, `b = 5`

### **Iteración 5 (i = 4)**
- **Valores Iniciales**: `a = 3`, `b = 5`
- **Impresión**: `print(a)` imprime `3`
- **Actualización**:
  - `tempA = a` asigna `tempA = 3`.
  - `a = b` actualiza `a` a `5`.
  - `b = tempA + b` actualiza `b` a `3 + 5 = 8`.
- **Nuevos Valores**: `a = 5`, `b = 8`

## Resumen de la Salida

El bucle genera la serie de Fibonacci como sigue:
```
0
1
1
2
3
```

## Consejos para Depurar Bucles

- **Utiliza `print`**: Imprime las variables en cada iteración para observar los cambios.
- **Herramientas de Depuración**: IDEs como PyCharm y VS Code tienen herramientas de depuración que permiten analizar el bucle paso a paso.
- **Verifica Condiciones y Actualizaciones**: Asegúrate de que las condiciones y asignaciones de variables sean correctas para evitar errores.

Al desglosar cada iteración, puedes comprender mejor cómo funciona el bucle y detectar cualquier problema en el flujo. ¡Buena suerte con la depuración! 🐍🐛
