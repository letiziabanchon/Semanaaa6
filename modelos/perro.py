
from modelos.animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    # Sobrescritura del método hablar (polimorfismo)
    def hablar(self):
        return "Guau guau!"
