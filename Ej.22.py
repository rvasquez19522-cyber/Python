def superposicio(llista1, llista2):
    """
    Retorna True si hi ha algun element en comú entre les dues llistes, 
    False en cas contrari.
    """
    for element in llista1:
        if element in llista2:
            return True
    return False

print(superposicio([1, 2, 3], [4, 5, 6]))   # False
print(superposicio([1, 2, 3], [3, 4, 5]))   # True
print(superposicio(["gato", "perro"], ["conejo", "gato"]))  # True
print(superposicio([10, 20, 30], [40, 50, 60]))  # False
