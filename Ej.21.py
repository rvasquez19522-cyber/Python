def es_palindrom(paraula):
    """
    Retorna True si la paraula és un palíndrom, False en cas contrari.
    """
    paraula = paraula.lower()  # Convertim a minúscules per no distingir entre majúscules i minúscules
    return paraula == paraula[::-1]  # Comprovem si la paraula és igual al seu revers

# Proves
paraules_test = ["radar", "ara", "civic", "rallar", "tapat", "simis", "refer", "hola", "python"]

print("Proves de palíndroms:")
print("-" * 30)
for paraula in paraules_test:
    resultat = es_palindrom(paraula)
    print(f"{paraula:10} -> {resultat}")