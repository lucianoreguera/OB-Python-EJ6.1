import string


class Alumno:
    def __init__(self, nombre, nota) -> None:
        self.nombre: str = nombre
        self.nota: float = nota

    def print_data(self):
        return "Nombre: " + self.nombre + " - Nota: " + str(self.nota)

    def is_approved(self):
        if (self.nota < 6):
            return "No está aprobado"
        else:
            return "Aprobado, felicitaciones"


alumno_1 = Alumno('Max', 7)
print(alumno_1.print_data())
print(alumno_1.is_approved())

alumno_2 = Alumno('Homer', 4)
print(alumno_2.print_data())
print(alumno_2.is_approved())
