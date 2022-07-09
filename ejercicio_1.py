import string


class Vehiculo:
    color: string
    puertas: int
    ruedas: int

    def __init__(self, color, puertas, ruedas) -> None:
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas


class Coche(Vehiculo):
    velocidad: float
    cilindradas: int

    def __init__(self, color, puertas, ruedas, velocidad, cilindradas) -> None:
        super().__init__(color, puertas, ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas


coche = Coche("Rojo", 4, 4, 165, 1400)
print("Color: " + str(coche.color))
print("Puertas: " + str(coche.puertas))
print("Ruedas: " + str(coche.ruedas))
print("Velocidad: " + str(coche.velocidad))
print("Cilindrada: " + str(coche.cilindradas))