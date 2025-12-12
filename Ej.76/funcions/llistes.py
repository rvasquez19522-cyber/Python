# funcions/llistes.py
import random

def llistes_numeros_aleatoris():
    # Generar una lista de 10 números aleatorios entre 1 y 100
    numeros = [random.randint(1, 100) for _ in range(10)]
    
    # Mostrar la lista original
    print(f'Lista original: {numeros}')
    
    # Ordenar la lista
    numeros.sort()
    print(f'Lista ordenada: {numeros}')
    
    # Calcular la suma y la media
    suma = sum(numeros)
    media = suma / len(numeros)
    print(f'Suma: {suma}')
    print(f'Media: {media}')
