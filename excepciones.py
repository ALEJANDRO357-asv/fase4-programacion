
# EXCEPCIONES PERSONALIZADAS BASE

class SistemaError(Exception):
    def __init__(self, mensaje, codigo_error=None):
        self.mensaje = mensaje
        self.codigo_error = codigo_error
        super().__init__(self.mensaje)


# EXCEPCIONES DE CLIENTE

class ClienteError(SistemaError):
    pass


class DocumentoInvalidoError(ClienteError):
    def __init__(self, documento):
        super().__init__(
            f"Documento inválido: {documento}. Debe contener solo números.",
            codigo_error="CLI001"
        )


class CorreoInvalidoError(ClienteError):
    def __init__(self, correo):
        super().__init__(
            f"Correo electrónico inválido: {correo}. Debe contener '@' y un dominio válido.",
            codigo_error="CLI002"
        )


class NombreInvalidoError(ClienteError):
    def __init__(self, nombre):
        super().__init__(
            f"Nombre inválido: {nombre}. Debe contener al menos 3 caracteres.",
            codigo_error="CLI003"
        )


# EXCEPCIONES DE SERVICIO

class ServicioError(SistemaError):
    pass


class DuracionInvalidaError(ServicioError):
    def __init__(self, duracion, tipo):
        super().__init__(
            f"Duración inválida: {duracion} {tipo}. Debe ser mayor a 0.",
            codigo_error="SRV001"
        )


class CostoInvalidoError(ServicioError):
    def __init__(self, costo):
        super().__init__(
            f"Costo inválido: {costo}. Debe ser mayor a 0.",
            codigo_error="SRV002"
        )


class ServicioNoDisponibleError(ServicioError):
    def __init__(self, nombre_servicio):
        super().__init__(
            f"Servicio no disponible: {nombre_servicio}.",
            codigo_error="SRV003"
        )


# EXCEPCIONES DE RESERVA

class ReservaError(SistemaError):
    pass


class ReservaDuplicadaError(ReservaError):
    def __init__(self, cliente, servicio):
        super().__init__(
            f"El cliente {cliente} ya tiene una reserva activa para {servicio}.",
            codigo_error="RES001"
        )


class ReservaCanceladaError(ReservaError):
    def __init__(self, id_reserva):
        super().__init__(
            f"La reserva {id_reserva} ya ha sido cancelada y no puede modificarse.",
            codigo_error="RES002"
        )


class ReservaNoEncontradaError(ReservaError):
    def __init__(self, id_reserva):
        super().__init__(
            f"Reserva no encontrada: {id_reserva}.",
            codigo_error="RES003"
        )


# EXCEPCIONES DE CÁLCULO

class CalculoError(SistemaError):
    pass


class DescuentoInvalidoError(CalculoError):
    def __init__(self, descuento):
        super().__init__(
            f"Descuento inválido: {descuento}%. Debe estar entre 0 y 100.",
            codigo_error="CAL001"
        )


class ImpuestoInvalidoError(CalculoError):
    def __init__(self, impuesto):
        super().__init__(
            f"Impuesto inválido: {impuesto}%. Debe estar entre 0 y 100.",
            codigo_error="CAL002"
        )


# EXCEPCIONES DE DATOS

class DatosError(SistemaError):
    pass


class CampoVacioError(DatosError):
    def __init__(self, campo):
        super().__init__(
            f"El campo '{campo}' es obligatorio y no puede estar vacío.",
            codigo_error="DAT001"
        )


class TipoDatoInvalidoError(DatosError):
    def __init__(self, campo, tipo_esperado, tipo_recibido):
        super().__init__(
            f"El campo '{campo}' espera tipo {tipo_esperado}, pero recibió {tipo_recibido}.",
            codigo_error="DAT002"
        )
