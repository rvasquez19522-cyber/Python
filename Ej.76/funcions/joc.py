# funcions/joc.py
import random

def joc_mastermind():
    colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja', 'blanco']
    combinacion_secreta = random.sample(colores, 4)
    intentos = 0
    
    print("¡Bienvenido al juego Mastermind!")
    print("Adivina la combinación secreta de 4 colores. Los colores son:")
    print(colores)
    
    while True:
        intento = input(f"Intento {intentos + 1}: Introduce tu combinación (4 colores separados por espacios): ").split()
        
        if len(intento) != 4:
            print("Error: Debes introducir exactamente 4 colores.")
            continue
        
        intentos += 1
        respuesta = []
        for i in range(4):
            if intento[i] == combinacion_secreta[i]:
                respuesta.append("Correcto")
            elif intento[i] in combinacion_secreta:
                respuesta.append("Incorrecto")
            else:
                respuesta.append("No acertado")
        
        print("Resultado:", respuesta)
        
        if intento == combinacion_secreta:
            print(f"¡Felicidades! Has adivinado la combinación en {intentos} intentos.")
            break
