
from modelos.animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # Sobrescritura del método hablar (polimorfismo)
    def hablar(self):
        return "Miau!"
