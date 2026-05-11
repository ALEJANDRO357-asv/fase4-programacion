"""
Sistema Integral de Gestión de Clientes, Servicios y Reservas
Software FJ - Fase 4 UNAD

Este módulo contiene todas las clases del sistema con validaciones robustas,
manejo avanzado de excepciones, métodos sobrecargados y principios POO.
"""

from abc import ABC, abstractmethod
from excepciones import *
from logger import *


# =========================================
# CLASE ABSTRACTA BASE PERSONA
# =========================================

class Persona(ABC):
    """
    Clase abstracta base que representa una persona en el sistema.
    Implementa abstracción y encapsulación.
    """

    def __init__(self, nombre, documento):
        """
        Inicializa una persona con validaciones.

        Args:
            nombre (str): Nombre de la persona
            documento (str): Documento de identificación

        Raises:
            CampoVacioError: Si algún campo está vacío
            NombreInvalidoError: Si el nombre es muy corto
            DocumentoInvalidoError: Si el documento no es válido
        """
        try:
            # Validar campos no vacíos
            if not nombre or not nombre.strip():
                raise CampoVacioError("nombre")

            if not documento or not documento.strip():
                raise CampoVacioError("documento")

            # Validar nombre
            if len(nombre.strip()) < 3:
                raise NombreInvalidoError(nombre)

            # Validar documento
            if not documento.isdigit():
                raise DocumentoInvalidoError(documento)

            self._nombre = nombre.strip()
            self._documento = documento.strip()

            registrar_evento(
                f"Persona creada: {self._nombre}",
                f"Documento: {self._documento}"
            )

        except (CampoVacioError, NombreInvalidoError, DocumentoInvalidoError) as error:
            registrar_error(error, "Constructor de Persona")
            raise

    @property
    def nombre(self):
        """Getter para el nombre"""
        return self._nombre

    @property
    def documento(self):
        """Getter para el documento"""
        return self._documento

    @abstractmethod
    def mostrar_datos(self):
        """Método abstracto para mostrar datos (polimorfismo)"""
        pass


# =========================================
# CLASE CLIENTE
# =========================================

class Cliente(Persona):
    """
    Clase que representa un cliente del sistema.
    Hereda de Persona e implementa validaciones adicionales.
    """

    def __init__(self, nombre, documento, correo, telefono=""):
        """
        Inicializa un cliente con validaciones robustas.

        Args:
            nombre (str): Nombre del cliente
            documento (str): Documento de identificación
            correo (str): Correo electrónico
            telefono (str): Teléfono (opcional)

        Raises:
            CorreoInvalidoError: Si el correo no es válido
        """
        try:
            # Primero inicializar la clase padre
            super().__init__(nombre, documento)

            # Validar correo
            if not correo or not correo.strip():
                raise CampoVacioError("correo")

            if "@" not in correo or "." not in correo.split("@")[-1]:
                raise CorreoInvalidoError(correo)

            # Encapsular datos privados
            self.__correo = correo.strip()
            self.__telefono = telefono.strip() if telefono else "No proporcionado"

            registrar_evento(
                f"Cliente registrado: {self.nombre}",
                f"Correo: {self.__correo}, Teléfono: {self.__telefono}"
            )

        except (CampoVacioError, CorreoInvalidoError) as error:
            registrar_error(error, f"Constructor de Cliente - {nombre}")
            raise

    @property
    def correo(self):
        """Getter para el correo"""
        return self.__correo

    @property
    def telefono(self):
        """Getter para el teléfono"""
        return self.__telefono

    def mostrar_datos(self):
        """
        Muestra los datos del cliente (implementación del método abstracto).
        """
        print(f"\n{'='*50}")
        print(f"DATOS DEL CLIENTE")
        print(f"{'='*50}")
        print(f"Nombre:    {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Correo:    {self.__correo}")
        print(f"Teléfono:  {self.__telefono}")
        print(f"{'='*50}")


# =========================================
# CLASE ABSTRACTA SERVICIO
# =========================================

class Servicio(ABC):
    """
    Clase abstracta base para todos los servicios del sistema.
    Implementa abstracción y polimorfismo.
    """

    def __init__(self, nombre, costo_base, disponible=True):
        """
        Inicializa un servicio con validaciones.

        Args:
            nombre (str): Nombre del servicio
            costo_base (float): Costo base del servicio
            disponible (bool): Si el servicio está disponible

        Raises:
            CampoVacioError: Si el nombre está vacío
            CostoInvalidoError: Si el costo es inválido
        """
        try:
            # Validar nombre
            if not nombre or not nombre.strip():
                raise CampoVacioError("nombre del servicio")

            # Validar costo
            if not isinstance(costo_base, (int, float)) or costo_base <= 0:
                raise CostoInvalidoError(costo_base)

            self._nombre = nombre.strip()
            self._costo_base = float(costo_base)
            self._disponible = disponible

            registrar_evento(
                f"Servicio creado: {self._nombre}",
                f"Costo base: ${self._costo_base:,.2f}"
            )

        except (CampoVacioError, CostoInvalidoError, TipoDatoInvalidoError) as error:
            registrar_error(error, "Constructor de Servicio")
            raise

    @property
    def nombre(self):
        """Getter para el nombre"""
        return self._nombre

    @property
    def costo_base(self):
        """Getter para el costo base"""
        return self._costo_base

    @property
    def disponible(self):
        """Getter para disponibilidad"""
        return self._disponible

    def marcar_no_disponible(self):
        """Marca el servicio como no disponible"""
        self._disponible = False
        registrar_evento(f"Servicio {self._nombre} marcado como NO disponible")

    def marcar_disponible(self):
        """Marca el servicio como disponible"""
        self._disponible = True
        registrar_evento(f"Servicio {self._nombre} marcado como disponible")

    @abstractmethod
    def calcular_costo(self, descuento=0, impuesto=19):
        """
        Método abstracto para calcular el costo (polimorfismo).
        Debe ser implementado por las clases derivadas.

        Args:
            descuento (float): Descuento a aplicar (0-100)
            impuesto (float): Impuesto a aplicar (porcentaje)

        Returns:
            float: Costo total calculado
        """
        pass

    @abstractmethod
    def describir(self):
        """Método abstracto para describir el servicio"""
        pass


# =========================================
# SERVICIO: RESERVA DE SALA
# =========================================

class ReservaSala(Servicio):
    """
    Servicio de reserva de salas.
    Implementa herencia y sobrecarga de métodos.
    """

    def __init__(self, nombre, costo_base, horas, capacidad=10, disponible=True):
        """
        Inicializa una reserva de sala.

        Args:
            nombre (str): Nombre de la sala
            costo_base (float): Costo por hora
            horas (int): Número de horas de reserva
            capacidad (int): Capacidad de personas
            disponible (bool): Si está disponible

        Raises:
            DuracionInvalidaError: Si las horas son inválidas
        """
        try:
            if not isinstance(horas, (int, float)) or horas <= 0:
                raise DuracionInvalidaError(horas, "horas")

            super().__init__(nombre, costo_base, disponible)

            self._horas = float(horas)
            self._capacidad = capacidad

            registrar_evento(
                f"Reserva de Sala configurada: {nombre}",
                f"Horas: {horas}, Capacidad: {capacidad} personas"
            )

        except DuracionInvalidaError as error:
            registrar_error(error, "Constructor de ReservaSala")
            raise

    @property
    def horas(self):
        """Getter para las horas"""
        return self._horas

    @property
    def capacidad(self):
        """Getter para la capacidad"""
        return self._capacidad

    # Sobrecarga de métodos: múltiples formas de calcular costo
    def calcular_costo(self, descuento=0, impuesto=19):
        """
        Calcula el costo total de la reserva de sala.

        Args:
            descuento (float): Descuento a aplicar (0-100)
            impuesto (float): Impuesto a aplicar (porcentaje)

        Returns:
            float: Costo total con descuento e impuesto

        Raises:
            DescuentoInvalidoError: Si el descuento es inválido
            ImpuestoInvalidoError: Si el impuesto es inválido
        """
        try:
            # Validar descuento
            if not isinstance(descuento, (int, float)) or descuento < 0 or descuento > 100:
                raise DescuentoInvalidoError(descuento)

            # Validar impuesto
            if not isinstance(impuesto, (int, float)) or impuesto < 0 or impuesto > 100:
                raise ImpuestoInvalidoError(impuesto)

            # Calcular costo base
            costo = self._costo_base * self._horas

            # Aplicar descuento
            if descuento > 0:
                costo = costo * (1 - descuento / 100)

            # Aplicar impuesto
            costo = costo * (1 + impuesto / 100)

            return round(costo, 2)

        except (DescuentoInvalidoError, ImpuestoInvalidoError) as error:
            registrar_error(error, f"Cálculo de costo - {self.nombre}")
            raise

    def calcular_costo_simple(self):
        """
        Calcula el costo simple sin descuentos ni impuestos.

        Returns:
            float: Costo base * horas
        """
        return round(self._costo_base * self._horas, 2)

    def describir(self):
        """Describe el servicio de reserva de sala"""
        return (f"Reserva de Sala: {self.nombre} | "
                f"Costo por hora: ${self._costo_base:,.2f} | "
                f"Duración: {self._horas} horas | "
                f"Capacidad: {self._capacidad} personas")


# =========================================
# SERVICIO: ALQUILER DE EQUIPO
# =========================================

class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos.
    Implementa herencia y sobrecarga de métodos.
    """

    def __init__(self, nombre, costo_base, dias, tipo_equipo="General", disponible=True):
        """
        Inicializa un alquiler de equipo.

        Args:
            nombre (str): Nombre del equipo
            costo_base (float): Costo por día
            dias (int): Número de días de alquiler
            tipo_equipo (str): Tipo de equipo
            disponible (bool): Si está disponible

        Raises:
            DuracionInvalidaError: Si los días son inválidos
        """
        try:
            if not isinstance(dias, (int, float)) or dias <= 0:
                raise DuracionInvalidaError(dias, "días")

            super().__init__(nombre, costo_base, disponible)

            self._dias = float(dias)
            self._tipo_equipo = tipo_equipo

            registrar_evento(
                f"Alquiler de Equipo configurado: {nombre}",
                f"Días: {dias}, Tipo: {tipo_equipo}"
            )

        except DuracionInvalidaError as error:
            registrar_error(error, "Constructor de AlquilerEquipo")
            raise

    @property
    def dias(self):
        """Getter para los días"""
        return self._dias

    @property
    def tipo_equipo(self):
        """Getter para el tipo de equipo"""
        return self._tipo_equipo

    def calcular_costo(self, descuento=0, impuesto=19):
        """
        Calcula el costo total del alquiler de equipo.

        Args:
            descuento (float): Descuento a aplicar (0-100)
            impuesto (float): Impuesto a aplicar (porcentaje)

        Returns:
            float: Costo total con descuento e impuesto

        Raises:
            DescuentoInvalidoError: Si el descuento es inválido
            ImpuestoInvalidoError: Si el impuesto es inválido
        """
        try:
            # Validar parámetros
            if not isinstance(descuento, (int, float)) or descuento < 0 or descuento > 100:
                raise DescuentoInvalidoError(descuento)

            if not isinstance(impuesto, (int, float)) or impuesto < 0 or impuesto > 100:
                raise ImpuestoInvalidoError(impuesto)

            # Calcular costo base
            costo = self._costo_base * self._dias

            # Descuento por días largos (más de 7 días)
            if self._dias > 7:
                descuento = max(descuento, 10)  # Mínimo 10% de descuento

            # Aplicar descuento
            if descuento > 0:
                costo = costo * (1 - descuento / 100)

            # Aplicar impuesto
            costo = costo * (1 + impuesto / 100)

            return round(costo, 2)

        except (DescuentoInvalidoError, ImpuestoInvalidoError) as error:
            registrar_error(error, f"Cálculo de costo - {self.nombre}")
            raise

    def calcular_costo_semanal(self):
        """
        Calcula el costo con tarifa semanal especial.

        Returns:
            float: Costo con descuento semanal
        """
        semanas = self._dias / 7
        costo = self._costo_base * semanas * 6  # 6 días por semana
        return round(costo * 1.19, 2)  # Con IVA

    def describir(self):
        """Describe el servicio de alquiler de equipo"""
        return (f"Alquiler de Equipo: {self.nombre} | "
                f"Tipo: {self._tipo_equipo} | "
                f"Costo por día: ${self._costo_base:,.2f} | "
                f"Duración: {self._dias} días")


# =========================================
# SERVICIO: ASESORÍA ESPECIALIZADA
# =========================================

class Asesoria(Servicio):
    """
    Servicio de asesoría especializada.
    Implementa herencia y sobrecarga de métodos.
    """

    def __init__(self, nombre, costo_base, sesiones, duracion_sesion=1, especialidad="General", disponible=True):
        """
        Inicializa una asesoría.

        Args:
            nombre (str): Nombre de la asesoría
            costo_base (float): Costo por sesión
            sesiones (int): Número de sesiones
            duracion_sesion (float): Duración de cada sesión en horas
            especialidad (str): Área de especialidad
            disponible (bool): Si está disponible

        Raises:
            DuracionInvalidaError: Si las sesiones son inválidas
        """
        try:
            if not isinstance(sesiones, (int, float)) or sesiones <= 0:
                raise DuracionInvalidaError(sesiones, "sesiones")

            if not isinstance(duracion_sesion, (int, float)) or duracion_sesion <= 0:
                raise DuracionInvalidaError(duracion_sesion, "horas por sesión")

            super().__init__(nombre, costo_base, disponible)

            self._sesiones = int(sesiones)
            self._duracion_sesion = float(duracion_sesion)
            self._especialidad = especialidad

            registrar_evento(
                f"Asesoría configurada: {nombre}",
                f"Sesiones: {sesiones}, Duración: {duracion_sesion}h, Especialidad: {especialidad}"
            )

        except DuracionInvalidaError as error:
            registrar_error(error, "Constructor de Asesoria")
            raise

    @property
    def sesiones(self):
        """Getter para las sesiones"""
        return self._sesiones

    @property
    def duracion_sesion(self):
        """Getter para la duración de sesión"""
        return self._duracion_sesion

    @property
    def especialidad(self):
        """Getter para la especialidad"""
        return self._especialidad

    def calcular_costo(self, descuento=0, impuesto=19):
        """
        Calcula el costo total de la asesoría.

        Args:
            descuento (float): Descuento a aplicar (0-100)
            impuesto (float): Impuesto a aplicar (porcentaje)

        Returns:
            float: Costo total con descuento e impuesto

        Raises:
            DescuentoInvalidoError: Si el descuento es inválido
            ImpuestoInvalidoError: Si el impuesto es inválido
        """
        try:
            # Validar parámetros
            if not isinstance(descuento, (int, float)) or descuento < 0 or descuento > 100:
                raise DescuentoInvalidoError(descuento)

            if not isinstance(impuesto, (int, float)) or impuesto < 0 or impuesto > 100:
                raise ImpuestoInvalidoError(impuesto)

            # Calcular costo base
            costo = self._costo_base * self._sesiones

            # Descuento por paquetes grandes (más de 5 sesiones)
            if self._sesiones >= 5:
                descuento = max(descuento, 15)  # Mínimo 15% de descuento

            # Aplicar descuento
            if descuento > 0:
                costo = costo * (1 - descuento / 100)

            # Aplicar impuesto
            costo = costo * (1 + impuesto / 100)

            return round(costo, 2)

        except (DescuentoInvalidoError, ImpuestoInvalidoError) as error:
            registrar_error(error, f"Cálculo de costo - {self.nombre}")
            raise

    def calcular_costo_por_hora(self):
        """
        Calcula el costo total basado en horas totales.

        Returns:
            float: Costo por hora * horas totales (con IVA)
        """
        horas_totales = self._sesiones * self._duracion_sesion
        costo_por_hora = self._costo_base / self._duracion_sesion
        return round(costo_por_hora * horas_totales * 1.19, 2)

    def describir(self):
        """Describe el servicio de asesoría"""
        horas_totales = self._sesiones * self._duracion_sesion
        return (f"Asesoría: {self.nombre} | "
                f"Especialidad: {self._especialidad} | "
                f"Costo por sesión: ${self._costo_base:,.2f} | "
                f"Sesiones: {self._sesiones} ({horas_totales}h totales)")


# =========================================
# CLASE RESERVA
# =========================================

class Reserva:
    """
    Clase que representa una reserva en el sistema.
    Integra cliente, servicio y maneja estados con excepciones robustas.
    """

    _contador_id = 1000  # Contador estático para IDs únicos

    def __init__(self, cliente, servicio):
        """
        Inicializa una reserva.

        Args:
            cliente (Cliente): Cliente que hace la reserva
            servicio (Servicio): Servicio a reservar

        Raises:
            TipoDatoInvalidoError: Si los tipos no son correctos
            ServicioNoDisponibleError: Si el servicio no está disponible
        """
        try:
            # Validar tipos
            if not isinstance(cliente, Cliente):
                raise TipoDatoInvalidoError("cliente", "Cliente", type(cliente).__name__)

            if not isinstance(servicio, Servicio):
                raise TipoDatoInvalidoError("servicio", "Servicio", type(servicio).__name__)

            # Validar disponibilidad
            if not servicio.disponible:
                raise ServicioNoDisponibleError(servicio.nombre)

            # Generar ID único
            Reserva._contador_id += 1
            self._id = f"RES-{Reserva._contador_id}"

            self._cliente = cliente
            self._servicio = servicio
            self._estado = "Pendiente"
            self._costo_final = 0

            registrar_evento(
                f"Reserva creada: {self._id}",
                f"Cliente: {cliente.nombre}, Servicio: {servicio.nombre}"
            )

        except (TipoDatoInvalidoError, ServicioNoDisponibleError) as error:
            registrar_error(error, "Constructor de Reserva")
            raise

    @property
    def id(self):
        """Getter para el ID"""
        return self._id

    @property
    def cliente(self):
        """Getter para el cliente"""
        return self._cliente

    @property
    def servicio(self):
        """Getter para el servicio"""
        return self._servicio

    @property
    def estado(self):
        """Getter para el estado"""
        return self._estado

    @property
    def costo_final(self):
        """Getter para el costo final"""
        return self._costo_final

    def confirmar(self, descuento=0, impuesto=19):
        """
        Confirma la reserva y calcula el costo final.

        Args:
            descuento (float): Descuento a aplicar
            impuesto (float): Impuesto a aplicar

        Raises:
            ReservaCanceladaError: Si la reserva ya fue cancelada
        """
        try:
            if self._estado == "Cancelada":
                raise ReservaCanceladaError(self._id)

            # Calcular costo final
            self._costo_final = self._servicio.calcular_costo(descuento, impuesto)
            self._estado = "Confirmada"

            registrar_evento(
                f"Reserva confirmada: {self._id}",
                f"Costo final: ${self._costo_final:,.2f}"
            )

            print(f"\n✓ Reserva {self._id} CONFIRMADA exitosamente")
            print(f"  Costo final: ${self._costo_final:,.2f}")

        except ReservaCanceladaError as error:
            registrar_error(error, f"Confirmar reserva {self._id}")
            raise
        except Exception as error:
            registrar_error(error, f"Confirmar reserva {self._id}")
            print(f"✗ Error al confirmar reserva: {error}")
            raise

    def cancelar(self):
        """
        Cancela la reserva.

        Raises:
            ReservaCanceladaError: Si la reserva ya fue cancelada
        """
        try:
            if self._estado == "Cancelada":
                raise ReservaCanceladaError(self._id)

            self._estado = "Cancelada"
            self._costo_final = 0

            registrar_evento(f"Reserva cancelada: {self._id}")

            print(f"\n✓ Reserva {self._id} CANCELADA exitosamente")

        except ReservaCanceladaError as error:
            registrar_error(error, f"Cancelar reserva {self._id}")
            raise

    def procesar(self):
        """
        Procesa la reserva (simula el procesamiento).

        Raises:
            ReservaCanceladaError: Si la reserva fue cancelada
        """
        try:
            if self._estado == "Cancelada":
                raise ReservaCanceladaError(self._id)

            if self._estado == "Pendiente":
                print(f"\n⚠ Reserva {self._id} está pendiente. Debe confirmarla primero.")
                return

            self._estado = "Procesada"

            registrar_evento(f"Reserva procesada: {self._id}")

            print(f"\n✓ Reserva {self._id} PROCESADA exitosamente")

        except ReservaCanceladaError as error:
            registrar_error(error, f"Procesar reserva {self._id}")
            raise

    def mostrar_reserva(self):
        """Muestra los detalles de la reserva"""
        print(f"\n{'='*70}")
        print(f"RESERVA: {self._id}")
        print(f"{'='*70}")
        print(f"Cliente:      {self._cliente.nombre} ({self._cliente.documento})")
        print(f"Servicio:     {self._servicio.describir()}")
        print(f"Estado:       {self._estado}")
        if self._costo_final > 0:
            print(f"Costo Final:  ${self._costo_final:,.2f}")
        print(f"{'='*70}")
