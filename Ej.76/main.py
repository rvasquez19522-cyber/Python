# main.py
from funcions.llistes import llistes_numeros_aleatoris
from funcions.fitxers import gestionar_llista_compra
from funcions.joc import joc_mastermind
from funcions.animals import probar_animals
from funcions.scraping import scraping_pagina
from funcions.web import app  # Flask

def menu():
    print("Elige una opción:")
    print("1. Trabajar con listas y números aleatorios")
    print("2. Gestionar lista de la compra")
    print("3. Jugar a Mastermind")
    print("4. Trabajar con clases (Ejemplo: Animales)")
    print("5. Realizar scraping de una página web")
    print("6. Crear un servidor web con Flask")

    opcion = int(input("Opción: "))

    if opcion == 1:
        llistes_numeros_aleatoris()
    elif opcion == 2:
        gestionar_llista_compra()
    elif opcion == 3:
        joc_mastermind()
    elif opcion == 4:
        probar_animals()
    elif opcion == 5:
        scraping_pagina()
    elif opcion == 6:
        app.run(debug=True)  # Ejecutar el servidor web Flask
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu()
