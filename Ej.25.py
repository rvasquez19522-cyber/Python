import random

def crear_punts(n, rang_x, rang_y):
    """
    Crea una llista de n punts aleatoris dins els rangs especificats.
    
    Args:
        n: nombre de punts
        rang_x: tupla (min, max) per coordenades x
        rang_y: tupla (min, max) per coordenades y
    
    Returns:
        Dues llistes amb les coordenades x i y
    """
    punts_x = [random.uniform(rang_x[0], rang_x[1]) for _ in range(n)]
    punts_y = [random.uniform(rang_y[0], rang_y[1]) for _ in range(n)]
    return punts_x, punts_y

def dibuixar_imatge_simple():
    """
    Dibuixa una imatge simple amb punts aleatoris generats amb la funció crear_punts().
    Es mostra per consola com una 'imatge' de punts.
    """
    # Generar punts aleatoris
    n = 50  # Nombre de punts a generar
    x, y = crear_punts(n, (0, 10), (0, 10))  # Generem punts entre 0 i 10 per a les coordenades X i Y

    # Mostrar els punts a la consola
    for i in range(n):
        # Generar una "imatge" simplificada amb punts en la consola
        print(f'Punt {i + 1}: ({x[i]:.2f}, {y[i]:.2f})')

# Cridar la funció per dibuixar la imatge
dibuixar_imatge_simple()
