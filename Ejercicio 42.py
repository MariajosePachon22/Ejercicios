#42.Simular el juego de piedra, papel o tijeras.
import random
opciones = ["piedra", "papel", "tijeras"]
eleccion_usuario = input("Elige piedra, papel o tijeras: ").lower()
eleccion_computadora = random.choice(opciones)
print("Computadora eligió:", eleccion_computadora)
if eleccion_usuario == eleccion_computadora:
    print("Empate.")
elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or \
     (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
     (eleccion_usuario == "tijeras" and eleccion_computadora == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste.")
















