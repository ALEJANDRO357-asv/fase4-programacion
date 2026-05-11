from sistema import *
from excepciones import *
from logger import *


# CLASE GESTOR DEL SISTEMA

class GestorSistema:

    def __init__(self):

        self._clientes = []
        self._servicios = []
        self._reservas = []

        inicializar_logs()

        registrar_evento("Sistema iniciado", "GestorSistema creado")

        print("\n" + "="*80)
        print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
        print("="*80)

    # GESTIÓN DE CLIENTES

    def registrar_cliente(self, nombre, documento, correo, telefono=""):
        try:
            if self.buscar_cliente_por_documento(documento):
                raise ClienteError(
                    f"Ya existe un cliente con documento {documento}",
                    codigo_error="CLI004"
                )

            cliente = Cliente(nombre, documento, correo, telefono)
            self._clientes.append(cliente)

            registrar_operacion(
                "Registro de Cliente",
                exito=True,
                mensaje=f"{nombre} ({documento})"
            )

            print(f"\n✓ Cliente registrado exitosamente: {nombre}")

            return cliente

        except (ClienteError, CampoVacioError, DocumentoInvalidoError,
                CorreoInvalidoError, NombreInvalidoError) as error:
            registrar_operacion(
                "Registro de Cliente",
                exito=False,
                mensaje=str(error)
            )
            print(f"\n✗ Error al registrar cliente: {error}")
            return None

        except Exception as error:
            registrar_error(error, "GestorSistema.registrar_cliente")
            print(f"\n✗ Error inesperado al registrar cliente: {error}")
            return None

    def buscar_cliente_por_documento(self, documento):
        try:
            for cliente in self._clientes:
                if cliente.documento == documento:
                    return cliente
            return None

        except Exception as error:
            registrar_error(error, "GestorSistema.buscar_cliente_por_documento")
            return None

    def listar_clientes(self):
        try:
            if not self._clientes:
                print("\nNo hay clientes registrados.")
                return

            print(f"\n{'='*80}")
            print(f"CLIENTES REGISTRADOS ({len(self._clientes)})")
            print(f"{'='*80}")

            for i, cliente in enumerate(self._clientes, 1):
                print(f"{i}. {cliente.nombre} - Doc: {cliente.documento} - "
                      f"Correo: {cliente.correo}")

            print(f"{'='*80}")

        except Exception as error:
            registrar_error(error, "GestorSistema.listar_clientes")
            print(f"Error al listar clientes: {error}")

    # GESTIÓN DE SERVICIOS

    def registrar_servicio(self, servicio):
        try:
            if not isinstance(servicio, Servicio):
                raise TipoDatoInvalidoError(
                    "servicio",
                    "Servicio",
                    type(servicio).__name__
                )

            self._servicios.append(servicio)

            registrar_operacion(
                "Registro de Servicio",
                exito=True,
                mensaje=f"{servicio.nombre}"
            )

            print(f"\n✓ Servicio registrado exitosamente: {servicio.nombre}")

            return True

        except (TipoDatoInvalidoError, ServicioError) as error:
            registrar_operacion(
                "Registro de Servicio",
                exito=False,
                mensaje=str(error)
            )
            print(f"\n✗ Error al registrar servicio: {error}")
            return False

        except Exception as error:
            registrar_error(error, "GestorSistema.registrar_servicio")
            print(f"\n✗ Error inesperado al registrar servicio: {error}")
            return False

    def buscar_servicio_por_nombre(self, nombre):
        try:
            for servicio in self._servicios:
                if servicio.nombre.lower() == nombre.lower():
                    return servicio
            return None

        except Exception as error:
            registrar_error(error, "GestorSistema.buscar_servicio_por_nombre")
            return None

    def listar_servicios(self):
        try:
            if not self._servicios:
                print("\nNo hay servicios registrados.")
                return

            print(f"\n{'='*80}")
            print(f"SERVICIOS REGISTRADOS ({len(self._servicios)})")
            print(f"{'='*80}")

            for i, servicio in enumerate(self._servicios, 1):
                disponible = "Sí" if servicio.disponible else "No"
                print(f"{i}. {servicio.describir()}")
                print(f"   Disponible: {disponible}")

            print(f"{'='*80}")

        except Exception as error:
            registrar_error(error, "GestorSistema.listar_servicios")
            print(f"Error al listar servicios: {error}")

    # GESTIÓN DE RESERVAS

    def crear_reserva(self, cliente, servicio):
        try:
            reserva = Reserva(cliente, servicio)
            self._reservas.append(reserva)

            registrar_operacion(
                "Creación de Reserva",
                exito=True,
                mensaje=f"ID: {reserva.id}"
            )

            print(f"\n✓ Reserva creada exitosamente: {reserva.id}")

            return reserva

        except (ReservaError, TipoDatoInvalidoError, ServicioNoDisponibleError) as error:
            registrar_operacion(
                "Creación de Reserva",
                exito=False,
                mensaje=str(error)
            )
            print(f"\n✗ Error al crear reserva: {error}")
            return None

        except Exception as error:
            registrar_error(error, "GestorSistema.crear_reserva")
            print(f"\n✗ Error inesperado al crear reserva: {error}")
            return None

    def buscar_reserva_por_id(self, id_reserva):
        try:
            for reserva in self._reservas:
                if reserva.id == id_reserva:
                    return reserva

            raise ReservaNoEncontradaError(id_reserva)

        except ReservaNoEncontradaError as error:
            registrar_error(error, "GestorSistema.buscar_reserva_por_id")
            print(f"\n✗ {error}")
            return None

        except Exception as error:
            registrar_error(error, "GestorSistema.buscar_reserva_por_id")
            return None

    def listar_reservas(self):
        try:
            if not self._reservas:
                print("\nNo hay reservas registradas.")
                return

            print(f"\n{'='*80}")
            print(f"RESERVAS REGISTRADAS ({len(self._reservas)})")
            print(f"{'='*80}")

            for i, reserva in enumerate(self._reservas, 1):
                print(f"{i}. ID: {reserva.id} | Cliente: {reserva.cliente.nombre} | "
                      f"Servicio: {reserva.servicio.nombre} | Estado: {reserva.estado}")

            print(f"{'='*80}")

        except Exception as error:
            registrar_error(error, "GestorSistema.listar_reservas")
            print(f"Error al listar reservas: {error}")

    def listar_reservas_por_estado(self, estado):
        try:
            reservas_filtradas = [r for r in self._reservas if r.estado == estado]

            if not reservas_filtradas:
                print(f"\nNo hay reservas con estado: {estado}")
                return

            print(f"\n{'='*80}")
            print(f"RESERVAS CON ESTADO: {estado} ({len(reservas_filtradas)})")
            print(f"{'='*80}")

            for i, reserva in enumerate(reservas_filtradas, 1):
                print(f"{i}. ID: {reserva.id} | Cliente: {reserva.cliente.nombre} | "
                      f"Servicio: {reserva.servicio.nombre}")

            print(f"{'='*80}")

        except Exception as error:
            registrar_error(error, "GestorSistema.listar_reservas_por_estado")
            print(f"Error al listar reservas: {error}")

    # ESTADÍSTICAS Y REPORTES

    def mostrar_estadisticas(self):
        try:
            print(f"\n{'='*80}")
            print("ESTADÍSTICAS DEL SISTEMA")
            print(f"{'='*80}")
            print(f"Total de Clientes:    {len(self._clientes)}")
            print(f"Total de Servicios:   {len(self._servicios)}")
            print(f"Total de Reservas:    {len(self._reservas)}")

            estados = {}
            for reserva in self._reservas:
                estados[reserva.estado] = estados.get(reserva.estado, 0) + 1

            if estados:
                print("\nReservas por Estado:")
                for estado, cantidad in estados.items():
                    print(f"  - {estado}: {cantidad}")

            ingresos = sum(r.costo_final for r in self._reservas if r.estado == "Confirmada")
            print(f"\nIngresos Totales (Confirmadas): ${ingresos:,.2f}")

            print(f"{'='*80}")

        except Exception as error:
            registrar_error(error, "GestorSistema.mostrar_estadisticas")
            print(f"Error al mostrar estadísticas: {error}")

    # GETTERS

    @property
    def clientes(self):
        return self._clientes.copy()

    @property
    def servicios(self):
        return self._servicios.copy()

    @property
    def reservas(self):
        return self._reservas.copy()
