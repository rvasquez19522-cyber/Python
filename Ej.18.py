"""
Definir una funció que agafi un caràcter i 
retorni vertader si és una vocal i en cas contrari retorni fals. Prova-la amb diferents exemples.
"""



def ej18(c):
    v = "aeiouAEIOUáàèéìíòóúùÀÁÈÉÌÍÒÓPÙÚ"
    if c in v:
        return True
    else:
        return False
    
# Programa principal
c = input("Escriu un caràcter per a provar si és o no vocal:")
print(ej18(c))   