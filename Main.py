from abc import ABC, abstractmethod


# -------------------------
# CLASE ABSTRACTA PERSONA
# -------------------------

class Persona(ABC):

    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_datos(self):
        pass


# -------------------------
# CLASE CLIENTE
# -------------------------

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


# -------------------------
# CLASE ABSTRACTA SERVICIO
# -------------------------

class Servicio(ABC):

    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass


# -------------------------
# SERVICIO RESERVA SALA
# -------------------------

class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, horas):

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")

        super().__init__(nombre, costo_base)

        self.horas = horas

    def calcular_costo(self):

        return self.costo_base * self.horas


# -------------------------
# SERVICIO ALQUILER EQUIPO
# -------------------------

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, dias):

        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")

        super().__init__(nombre, costo_base)

        self.dias = dias

    def calcular_costo(self):

        return self.costo_base * self.dias


# -------------------------
# SERVICIO ASESORIA
# -------------------------

class Asesoria(Servicio):

    def __init__(self, nombre, costo_base, sesiones):

        if sesiones <= 0:
            raise ValueError("Las sesiones deben ser mayores a 0")

        super().__init__(nombre, costo_base)

        self.sesiones = sesiones

    def calcular_costo(self):

        return self.costo_base * self.sesiones


# -------------------------
# CLASE RESERVA
# -------------------------

class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):

        self.estado = "Confirmada"

        print("Reserva confirmada")

    def cancelar(self):

        self.estado = "Cancelada"

        print("Reserva cancelada")

    def mostrar_reserva(self):

        print("\n----- RESERVA -----")

        self.cliente.mostrar_datos()

        print(f"Servicio: {self.servicio.nombre}")
        print(f"Costo total: {self.servicio.calcular_costo()}")
        print(f"Estado: {self.estado}")


# -------------------------
# PRUEBAS DEL SISTEMA
# -------------------------

try:

    cliente1 = Cliente(
        "Alejandro",
        "123456",
        "correo@gmail.com"
    )

    servicio1 = ReservaSala(
        "Sala de juntas",
        50000,
        2
    )

    reserva1 = Reserva(
        cliente1,
        servicio1
    )

    reserva1.confirmar()

    reserva1.mostrar_reserva()

except ValueError as error:

    print("Error:", error)

finally:

    print("\nPrograma finalizado")
