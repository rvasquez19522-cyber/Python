# Exercici 72: Llegir els noms des de Ex72.txt i posar-los en una llista

# Obrir el fitxer Ex72.txt i llegir el seu contingut
with open("Ex72.txt", "r") as fitxer:
    llista_noms = fitxer.read().splitlines()  # Llegim el contingut i separem per línies

# Imprimir la llista de noms
print(llista_noms)
