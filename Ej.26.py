def gran_llista(llista):
    """Retorna el número més gran d'una llista"""
    mes_gran = llista[0]
    for num in llista:
        if num > mes_gran:
            mes_gran = num
    return mes_gran

# Exemple d'ús
print(gran_llista([3, 4, 2, 3, 10]))  # 10
print(gran_llista([100, 50, 25]))     # 100
print(gran_llista([-5, -2, -10]))     # -2
print(gran_llista([7]))               # 7
