def potencies(exponent):
    """
    Retorna una llista dels 10 primers números elevats a la potència donada
    """
    return [num ** exponent for num in range(10)]

# Exemples d'ús:
print("Quadrats:", potencies(2))
print("Cubs:", potencies(3))
print("Potència de 4:", potencies(4))