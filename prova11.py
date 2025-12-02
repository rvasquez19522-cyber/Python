# Llegir 2 nombres
# Imprimir tots els nombres entre el menor i el major
def ordenar(x, y):
    # Prec: donat dos numeros
    # Post: retorna el menor i despres el major
    if x>y:
        return y, x
    elif y>x:
        return x, y
    else:
        return x, y

# Programa principal
v1 = int(input("Intro el 1r numero:"))
v2 = int(input("Intro el 2n numero:"))
v1, v2 = ordenar(v1, v2)
for e in range(v1, v2+1):
    if e%2==0:
        print(e)