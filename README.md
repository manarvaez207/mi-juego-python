# Juego: Adivina el Número

## Autor:
- **Matthew Narváez**  

## Objetivo del programa
Desarrollar un juego interactivo en Python que permita al usuario **adivinar un número secreto** generado aleatoriamente por la computadora.  
El objetivo es que el jugador use la lógica y la deducción para encontrar el número en la menor cantidad de intentos posible.

## Descripción general
El programa genera un **número aleatorio entre 1 y 100**, y el jugador debe intentar adivinarlo.  
Después de cada intento, el sistema le indica si el número ingresado es **mayor o menor** que el número secreto.  
El juego termina cuando el jugador acierta, mostrando el número correcto y la cantidad de intentos usados.

## Principales funcionalidades del código

1. **Selección de dificultad:**  
   El jugador puede elegir entre tres niveles:
   - Fácil → números del 1 al 10 (5 intentos)  
   - Medio → números del 1 al 50 (7 intentos)  
   - Difícil → números del 1 al 100 (10 intentos)

2. **Generación aleatoria del número secreto:**  
   El programa utiliza el módulo `random` para seleccionar un número de forma automática dentro del rango del nivel elegido.

3. **Control de intentos:**  
   Se lleva un conteo de los intentos realizados y se limita según la dificultad seleccionada.

4. **Validación de datos:**  
   El código usa `try` y `except` para detectar errores cuando el jugador no ingresa un número válido.

5. **Mensajes de ayuda:**  
   Durante el juego, el programa informa si el número ingresado es **más alto o más bajo** que el número secreto.

6. **Finalización del juego:**  
   - Si el jugador adivina el número, se muestra un mensaje de victoria   
   - Si se agotan los intentos, el juego revela el número secreto   
   - Al finalizar, el jugador puede decidir si desea **volver a jugar o salir**.

7. **Diseño visual amigable:**  
   Se incluye un encabezado decorativo con símbolos y pausas controladas con `time.sleep()` para mejorar la experiencia del usuario.

---

## Herramientas utilizadas
- **Lenguaje:** Python 3.11+  
- **Entorno:** Visual Studio Code  
- **Librerías:**  
  - `random` → para generar números aleatorios  
  - `time` → para controlar el tiempo de espera en mensajes  

---

## Ejemplo de ejecución
ADIVINA EL NÚMERO
Selecciona la dificultad:

Fácil (1 - 10)

Medio (1 - 50)

Difícil (1 - 100)
Elige (1-3): 2

Estoy pensando en un número...
Intento 1/7: 25
Demasiado bajo.
Intento 2/7: 40
Demasiado alto.
Intento 3/7: 32
¡Lo lograste en 3 intentos! 


## Fecha de entrega
**16 de octubre de 2025**

## Diagrama de flujo  
El diagrama representa el proceso desde la generación del número hasta la comparación con el intento del jugador y la salida final.

Inicio → Generar número → Pedir intento → Comparar → Mayor/Menor → ¿Adivinó? → Fin

---

## Comentarios finales
Este proyecto demuestra la aplicación práctica de estructuras condicionales, bucles y validaciones de datos en Python.  
Fue elaborado como parte del curso de **Introducción a la Programación** bajo el conocimiento de la **Ing. LILIAN MARLENE AMAN RAMOS**.

---

### Universidad UIDE - Ingeniería en Ciberseguridad  
> Guayaquil, Ecuador

