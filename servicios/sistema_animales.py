
# Servicio que trabaja con los objetos del sistema

def describir_animal(animal):
    print(f"Nombre: {animal.nombre}")
    print(f"Edad: {animal.obtener_edad()} años")
    print(f"Habla así: {animal.hablar()}")
    print("-------------------------")
