
# 🔄 Ejercicios para Aprender y Fortalecer el Uso de Estructuras de Control de Flujo en Python

Las estructuras de control de flujo son fundamentales en la programación para tomar decisiones y repetir acciones. A continuación, encontrarás ejercicios diseñados para que practiques y fortalezcas tus habilidades en el uso de estas estructuras en Python. ¡Vamos a poner manos a la obra! 🚀

## 📚 Ejercicio Ejemplo

### **Ejercicio 1: Adivina el Número**

Escribe un programa que elija un número aleatorio entre 1 y 10. El programa debe permitir al usuario adivinar el número y darle pistas si su respuesta es mayor o menor al número secreto. El programa se detiene cuando el usuario acierta.

#### **Solución**
```python
import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
adivinado = False

while not adivinado:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    if adivinanza == numero_secreto:
        print("¡Felicidades! Has adivinado el número 🎉")
        adivinado = True
    elif adivinanza < numero_secreto:
        print("El número es mayor 📈")
    else:
        print("El número es menor 📉")
```
### **Explicación**:
1. **Bucle `while`**: El programa sigue ejecutándose mientras el usuario no haya adivinado el número.
2. **Condicionales `if`, `elif`, `else`**: Se usan para verificar si el número adivinado es correcto, mayor o menor al número secreto, dando así retroalimentación al usuario.

## 🎯 Ejercicios Propuestos

### **Ejercicio 2: Calculadora de Notas**
Crea un programa que pida al usuario su calificación (entre 0 y 100). Dependiendo del valor ingresado, el programa debe mostrar si el estudiante ha aprobado (60 o más) o ha reprobado (menos de 60). Usa condicionales para determinar el resultado.

### **Ejercicio 3: Números Pares e Impares**
Escribe un programa que recorra los números del 1 al 20 e imprima si cada número es par o impar. Usa un bucle `for` para recorrer los números y condicionales para determinar si un número es par o impar.

### **Ejercicio 4: Menú de Opciones**
Crea un programa que muestre un menú de opciones simples (por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") y permita al usuario seleccionar una opción. Dependiendo de la opción, el programa debe ejecutar una acción específica o salir del bucle si el usuario elige "Salir". Usa un bucle `while` para mostrar el menú hasta que el usuario decida salir.

## 🎉 ¡A Practicar!
Con estos ejercicios, puedes poner en práctica el uso de estructuras de control como condicionales (`if`, `else`) y bucles (`for`, `while`). ¡Explora las posibilidades y diviértete programando en Python! 🌟🐍
