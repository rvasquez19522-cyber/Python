sumapositius=0
sumanegatius=0
nombrenumeros = 0
sortir='n'
while sortir !='s' :
    numero = float(input("Introdueix un número: "))
    nombrenumeros+=1
    if numero >= 0:
        sumapositius += numero
    else:
        sumanegatius += numero
    sortir=input("Vols sortir? (s/n): ")
print("""Suma de numeros positius: {}
         Suma de numeros negatius: {})
         Mitjana {}""".format(sumapositius, sumanegatius, (sumapositius +sumanegatius)/nombrenumeros))
    nombrenumeros += 1
