# funcions/animals.py

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Cada animal debe hablar de una manera distinta.")

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

def probar_animals():
    animales = [Perro("Rex"), Gato("Tom")]
    
    for animal in animales:
        print(f"{animal.nombre} dice: {animal.hablar()}")
