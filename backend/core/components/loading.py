import time
import sys

def loading(message="Loading"):
    for i in range(4):
        for dots in range(1, 4):
            # Imprime el mensaje con los puntos
            sys.stdout.write(f"\r{message}{'.' * dots}  ")
            sys.stdout.flush()
            time.sleep(0.2)
    # Limpia la línea completamente imprimiendo más espacios y regresando el cursor
    print("\r" + " " * 80 + "\r", end="")

def typewriter(typewriter):
    for char in typewriter:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.002)  # Velocidad de escritura (más bajo = más rápido)