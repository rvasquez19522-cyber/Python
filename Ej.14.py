def menu_principal():
    opcio=0
    while opcio<1 or opcio>3:
        opcio = int(input(""" Elegexi una opcio:
                      1. Calculadora decimal
                      2. Calculadora real (floats
                      3. Sortir \n"""))
    if opcio>0 and opcio<4:
        return opcio
    else:
        print("L'opcio seleccionada no és correcte, torni-ho a provar!!\n")
def menu_calculadora():
    opcio=0
    while opcio<1 or opcio>5:
        opcio=int(input("""Elegeixi una opció:
                    1. Suma
                    2. Resta
                    3. Multiplicació
                    4. Divisió
                    5. Sortir
                    """))
    if opcio>0 and opcio<6:
        return opcio
    else:
        print("L'opcio selecciona no és correcte, torni-ho a provar!!\n")

def calculadora_decimal(opcio):
    if opcio>0 and opcio<5:
        a = float(input("introdueixi el primer número: "))
        b = float(input("Introdueixi el segon número: "))
    match(opcio):
        case 1:
            #Suma
            print("Estic fent la suma! \n")
            c = a + b
            print("El resultat de suma {} + {} és {}".format(a, b, c))
        case 2:
            #Resta
            print("Estic fent la Resta! \n")
            c = a - b
            print("El resultat de restar {} - {} és {}".format(a, b, c))
        case 3:
            #Multiplicacio
            print("Estic fent la Multiplicacio! \n")
            c = a * b
            print("El resultat de Multiplicacio {} * {} és {}".format(a, b, c))
        case 4:
            #Divisió
            print("Estic fent la multiplicació! \n")
            c = a // b
            print("El resultat de Divisió {} / {} és {}".format(a, b, c))
        case _:
            print("opció no valida! Torni-ho a provar! \n")
def calculadora_real(opcio):
    if opcio>0 and opcio<5:
     a = float(input("Introdueixi el primer número: "))
    b = float(input("Introdueixi el segon número: "))
    match(opcio):
        case 1:
            #Suma
            print("Estic fent la suma! \n")
            c = a + b
            print("El resultat de sumar {} / {} és {}".format(a, b, c))
        case 2:
            #Resta
            print("Estic fent la Resta! \n")
            c = a - b
            print("El resultat de Restar {} / {} és {}".format(a, b, c))
        case 3:
            #Multiplicacio
            print("Estic fent la Multiplicacio! \n")
            c = a * b
            print("El resultat de Multiplicacio {} / {} és {}".format(a, b, c))
        case 4:
            #Divisió
            print("Estic fent la multiplicació! \n")
            c = a // b
            print("El resultat de Dividir {} / {} és {}".format(a, b, c))
        case _:
            print("opció no valida! Torni-ho a provar! \n")

# Programa Principal
op = 1
while op!=0:
    op = menu_principal()
    if op==1:
        # Calculadora decimal
        print("Estic passant per la calculadora decimal \n")
        calculadora_decimal(menu_calculadora())
    elif op==2:
        # Calculadora real
        print("Estic passant per la calculadora real! \n")
        calculadora_real(menu_calculadora())
    elif op==3:
        # Canvis de base
        print("Estic passant per la calculadora de canvis de base! \n")
    else:
        print("Gràcies per a utilizar la meva calculadora, fins un altre dia! \n")
        op=0

