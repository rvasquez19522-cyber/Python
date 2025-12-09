import re

def lenp(frase):
    # Elimina caràcters especials (punctuació) utilitzant una expressió regular
    frase_sense_puntuacio = re.sub(r'[^\w\s]', '', frase)
    
    # Separa la frase en paraules
    paraules = frase_sense_puntuacio.split()
    
    # Utilitza map per obtenir la longitud de cada paraula
    longituds = list(map(len, paraules))
    
    return longituds

frase = "Hola món, com estàs?"
resultat = lenp(frase)
print(resultat)
