from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_datos(self):
        pass


class Cliente(Persona):

    def __init__(self, nombre, documento, correo):

        if "@" not in correo:
            raise ValueError("Correo inválido")

        super().__init__(nombre, documento)

        self.__correo = correo

    def mostrar_datos(self):
        print(f"Cliente: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Correo: {self.__correo}")


try:

    cliente1 = Cliente(
        "Alejandro",
        "123",
        "correo@gmail.com"
    )

    cliente1.mostrar_datos()

except ValueError as error:
    print(error)
