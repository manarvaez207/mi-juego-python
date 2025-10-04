# Juego: Adivina el Número
# Autor: Matthew Narvaez
# Desarrollado para el Aprendizaje Autónomo 2
# Lenguaje: Python
# Herramienta: Visual Studio Code

import random  # Importamos la librería para generar números aleatorios

print("Bienvenido al juego: Adivina el Número")
print("Estoy pensando en un número entre 1 y 100...")

# Generamos el número aleatorio que el jugador debe adivinar
numero_secreto = random.randint(1, 100)

# Inicializamos variables
intentos = 0
adivinado = False

# Bucle principal del juego: se repite hasta que el usuario adivine
while not adivinado:
    try:
        # Solicitamos al usuario que ingrese un número
        entrada = input(" Ingresa tu número: ")
        numero = int(entrada)  # Convertimos la entrada en entero
        intentos += 1  # Sumamos un intento

        # Verificamos si el número es menor, mayor o igual al secreto
        if numero < numero_secreto:
            print("🔻 Muy bajo, intenta nuevamente.\n")
        elif numero > numero_secreto:
            print("🔺 Muy alto, intenta nuevamente.\n")
        else:
            print(f" ¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            adivinado = True  # Salimos del bucle

    except ValueError:
        # Capturamos errores si el usuario ingresa algo que no sea número
        print(" Error: Debes ingresar un número entero válido.\n")

# Mensaje final
print(" Gracias por jugar. ¡Hasta la próxima!")
