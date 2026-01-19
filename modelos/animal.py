
# Clase base Animal
# Demuestra herencia, encapsulación y atributos comunes.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad   # Atributo encapsulado (privado)

    def obtener_edad(self):
        return self.__edad

    def hablar(self):
        # Método que será sobrescrito (polimorfismo)
        return "Este animal hace un sonido."
