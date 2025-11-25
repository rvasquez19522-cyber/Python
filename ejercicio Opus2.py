"""
Llegir el número de frases i ses frases
A cada frase substituir les consonants per una Majúscula
Imprimis ses frases modificades
"""

def llegir_frases(n):
# Prec: donat un número
# Post: retorna una llista de n-element llegits del teclat
    llista =  list()
    for i in range(n):
        llista.append(input(""))
    return llista

def escriure:frases(llista):
# Prec: donada una llista d'element
# Post: imprimeix cada element de la llista
    for e in llista:
        print(e)

def convertir_majuscules(s):
    vocal="aeiouAEIOU"
    llista = list(s)
    for i,e in enumerate(llista):
        if e not in vocal:
            llista[i]=e.upper()
    return "".join(llista)


#Programa principal
n = int(input(""))
llista=llegir_frases(n)
for i,e in enumerate(llista):
    llista[i]convertir_majuscules(e)
escriure_frases(llista)