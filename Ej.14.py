def menu_principal():
    while True:
        opcio = int(input("""Elegeixi una opció:
                            1. Calculadora decimal
                            2. Calculadora real (floats)
                            3. Canvi de base (binària, octal, decimal, hexadecimal)
                            4. Sortir\n"""))
        if opcio in [1, 2, 3, 4]:
            return opcio
        else:
            print("L'opció seleccionada no és correcta, torni-ho a provar!!\n")

def menu_calculadora():
    while True:
        opcio = int(input("""Elegeixi una opció:
                            1. Suma
                            2. Resta
                            3. Multiplicació
                            4. Divisió
                            5. Sortir\n"""))
        if opcio in [1, 2, 3, 4, 5]:
            return opcio
        else:
            print("L'opció seleccionada no és correcta, torni-ho a provar!!\n")

def calcular(opcio, tipus):
    a = float(input("Introdueixi el primer número: "))
    b = float(input("Introdueixi el segon número: "))

    if tipus == "decimal":
        operacions = {
            1: (a + b, "suma"),
            2: (a - b, "resta"),
            3: (a * b, "multiplicació"),
            4: (a / b if b != 0 else "Error: Divisió per zero!", "divisió")
        }
    else:  # real
        operacions = {
            1: (a + b, "suma"),
            2: (a - b, "resta"),
            3: (a * b, "multiplicació"),
            4: (a / b if b != 0 else "Error: Divisió per zero!", "divisió")
        }

    resultat, operacio = operacions.get(opcio, ("Opció no vàlida!", ""))
    print(f"Estic fent la {operacio}! \nEl resultat de {operacio} {a} i {b} és {resultat}")

# Funció per a canviar entre bases
def canviar_base():
    print("Elegeixi una opció de base:")
    print("1. Binari a Decimal")
    print("2. Octal a Decimal")
    print("3. Hexadecimal a Decimal")
    print("4. Decimal a Binari")
    print("5. Decimal a Octal")
    print("6. Decimal a Hexadecimal")
    opcio = int(input("Selecciona una opció (1-6): "))

    if opcio == 1:
        num = input("Introdueix el número binari: ")
        try:
            print(f"{num} en binari és {int(num, 2)} en decimal.")
        except ValueError:
            print("Error: El número introduït no és binari.")
    elif opcio == 2:
        num = input("Introdueix el número octal: ")
        try:
            print(f"{num} en octal és {int(num, 8)} en decimal.")
        except ValueError:
            print("Error: El número introduït no és octal.")
    elif opcio == 3:
        num = input("Introdueix el número hexadecimal: ")
        try:
            print(f"{num} en hexadecimal és {int(num, 16)} en decimal.")
        except ValueError:
            print("Error: El número introduït no és hexadecimal.")
    elif opcio == 4:
        num = int(input("Introdueix el número decimal: "))
        print(f"{num} en decimal és {bin(num)[2:]} en binari.")
    elif opcio == 5:
        num = int(input("Introdueix el número decimal: "))
        print(f"{num} en decimal és {oct(num)[2:]} en octal.")
    elif opcio == 6:
        num = int(input("Introdueix el número decimal: "))
        print(f"{num} en decimal és {hex(num)[2:]} en hexadecimal.")
    else:
        print("Opció no vàlida!")

# Programa Principal
while True:
    op = menu_principal()
    if op == 1:
        print("Calculadora decimal activada!")
        calcular(menu_calculadora(), "decimal")
    elif op == 2:
        print("Calculadora real activada!")
        calcular(menu_calculadora(), "real")
    elif op == 3:
        print("Canvi de base activat!")
        canviar_base()
    else:
        print("Gràcies per utilitzar la calculadora. Fins un altre dia!")
        break
