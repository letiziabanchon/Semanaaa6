
from modelos.perro import Perro
from modelos.gato import Gato
from servicios.sistema_animales import describir_animal

# Crear instancias de clases derivadas
perro1 = Perro("Rocky", 3, "Labrador")
gato1 = Gato("Michi", 2, "Blanco")

# Mostrar funcionamiento
describir_animal(perro1)
describir_animal(gato1)
