def paraules_per_lletra(llista_paraules, lletra):
    """
    Retorna una llista amb les paraules que comencen per la lletra donada.
    
    Args:
        llista_paraules: llista de paraules (strings)
        lletra: lletra inicial a buscar (string)
    
    Returns:
        llista de paraules que comencen per la lletra donada
    """
    return list(filter(lambda paraula: paraula.lower().startswith(lletra.lower()), llista_paraules))


# Exemple d'ús
paraules = ["maria", "manta", "peu", "mà"]
resultat = paraules_per_lletra(paraules, 'p')
print(resultat)  # ['peu']

# Més exemples
print(paraules_per_lletra(paraules, 'm'))  # ['maria', 'manta', 'mà']
print(paraules_per_lletra(paraules, 'a'))  # []
print(paraules_per_lletra(paraules, 'M'))  # ['maria', 'manta', 'mà'] (case insensitive)