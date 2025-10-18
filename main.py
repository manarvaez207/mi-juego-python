# Juego: Adivina el Número
# Autor: Matthew Narvaez
# Desarrollado para la Evaluación en Contacto con el Docente
# Lenguaje: Python
# Herramienta: Visual Studio Code

import random
import time

def adivina_numero():
    print("╔════════════════════════════════╗")
    print("║     🎯  ADIVINA EL NÚMERO 🎯     ║")
    print("╚════════════════════════════════╝\n")

    print("Selecciona la dificultad:")
    print("1. Fácil (1 - 10)")
    print("2. Medio (1 - 50)")
    print("3. Difícil (1 - 100)")

    while True:
        try:
            nivel = int(input("Elige (1-3): "))
            if nivel in [1, 2, 3]:
                break
            else:
                print("Por favor, elige un número del 1 al 3.")
        except ValueError:
            print("Ingresa un número válido.")

    if nivel == 1:
        limite = 10
        intentos_max = 5
    elif nivel == 2:
        limite = 50
        intentos_max = 7
    else:
        limite = 100
        intentos_max = 10

    numero_secreto = random.randint(1, limite)
    intentos = 0

    print("\nEstoy pensando en un número...")
    time.sleep(1)

    while intentos < intentos_max:
        try:
            adivinanza = int(input(f"\nIntento {intentos + 1}/{intentos_max}: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("🔻 Demasiado bajo.")
            elif adivinanza > numero_secreto:
                print("🔺 Demasiado alto.")
            else:
                print(f"\n🎉 ¡Lo lograste en {intentos} intentos! 🎉")
                break
        except ValueError:
            print("Eso no es un número válido.")

    else:
        print(f"\n💀 Te quedaste sin intentos. El número era {numero_secreto}.")

    jugar_nuevamente = input("\n¿Quieres jugar otra vez? (si/no): ").lower()
    if jugar_nuevamente == "si":
        adivina_numero()
    else:
        print("\nGracias por jugar  ¡Hasta la próxima!\n")

if __name__ == "__main__":
    adivina_numero()

