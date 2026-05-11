import datetime
import os

# CONFIGURACIÓN DE LOGGING

ARCHIVO_LOGS = "sistema_logs.txt"
ARCHIVO_ERRORES = "sistema_errores.txt"
ARCHIVO_EVENTOS = "sistema_eventos.txt"

# FUNCIONES DE LOGGING

def obtener_timestamp():
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")


def inicializar_logs():
    try:
        # Encabezado para archivo general de logs
        if not os.path.exists(ARCHIVO_LOGS):
            with open(ARCHIVO_LOGS, "w", encoding="utf-8") as archivo:
                archivo.write("=" * 80 + "\n")
                archivo.write("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ\n")
                archivo.write("Archivo de Logs Generales\n")
                archivo.write(f"Creado: {obtener_timestamp()}\n")
                archivo.write("=" * 80 + "\n\n")

        # Encabezado para archivo de errores
        if not os.path.exists(ARCHIVO_ERRORES):
            with open(ARCHIVO_ERRORES, "w", encoding="utf-8") as archivo:
                archivo.write("=" * 80 + "\n")
                archivo.write("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ\n")
                archivo.write("Archivo de Errores\n")
                archivo.write(f"Creado: {obtener_timestamp()}\n")
                archivo.write("=" * 80 + "\n\n")

        # Encabezado para archivo de eventos
        if not os.path.exists(ARCHIVO_EVENTOS):
            with open(ARCHIVO_EVENTOS, "w", encoding="utf-8") as archivo:
                archivo.write("=" * 80 + "\n")
                archivo.write("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ\n")
                archivo.write("Archivo de Eventos\n")
                archivo.write(f"Creado: {obtener_timestamp()}\n")
                archivo.write("=" * 80 + "\n\n")

    except IOError as error:
        print(f"Error al inicializar archivos de logs: {error}")


def registrar_log(mensaje, nivel="INFO"):
    try:
        with open(ARCHIVO_LOGS, "a", encoding="utf-8") as archivo:
            linea = f"{obtener_timestamp()} [{nivel}] {mensaje}\n"
            archivo.write(linea)
    except IOError as error:
        print(f"Error al registrar log: {error}")


def registrar_error(error, contexto=""):
    try:
        with open(ARCHIVO_ERRORES, "a", encoding="utf-8") as archivo:
            archivo.write(f"{obtener_timestamp()} ERROR\n")
            archivo.write(f"Tipo: {type(error).__name__}\n")
            archivo.write(f"Mensaje: {str(error)}\n")

            # Si es una excepción personalizada con código de error
            if hasattr(error, 'codigo_error') and error.codigo_error:
                archivo.write(f"Código: {error.codigo_error}\n")

            if contexto:
                archivo.write(f"Contexto: {contexto}\n")

            archivo.write("-" * 80 + "\n\n")

        # Rregistrar en el log general
        registrar_log(f"ERROR - {type(error).__name__}: {str(error)}", nivel="ERROR")

    except IOError as io_error:
        print(f"Error al registrar error en log: {io_error}")


def registrar_evento(evento, detalles=""):
    try:
        with open(ARCHIVO_EVENTOS, "a", encoding="utf-8") as archivo:
            archivo.write(f"{obtener_timestamp()} {evento}\n")
            if detalles:
                archivo.write(f"Detalles: {detalles}\n")
            archivo.write("-" * 40 + "\n")

        # Registrar en el log general
        registrar_log(evento, nivel="INFO")

    except IOError as error:
        print(f"Error al registrar evento: {error}")


def registrar_operacion(operacion, exito=True, mensaje=""):
    try:
        estado = "EXITOSA" if exito else "FALLIDA"
        nivel = "INFO" if exito else "WARNING"

        log_mensaje = f"Operación {operacion}: {estado}"
        if mensaje:
            log_mensaje += f" - {mensaje}"

        registrar_log(log_mensaje, nivel=nivel)

    except Exception as error:
        print(f"Error al registrar operación: {error}")


def limpiar_logs():
    try:
        for archivo in [ARCHIVO_LOGS, ARCHIVO_ERRORES, ARCHIVO_EVENTOS]:
            if os.path.exists(archivo):
                os.remove(archivo)
        print("Archivos de logs limpiados exitosamente")
    except Exception as error:
        print(f"Error al limpiar logs: {error}")


def mostrar_resumen_logs():
    try:
        print("\n" + "=" * 80)
        print("RESUMEN DE LOGS DEL SISTEMA")
        print("=" * 80)

        # Contar líneas de cada archivo
        archivos = [
            (ARCHIVO_LOGS, "Logs Generales"),
            (ARCHIVO_ERRORES, "Errores Registrados"),
            (ARCHIVO_EVENTOS, "Eventos Registrados")
        ]

        for archivo, nombre in archivos:
            if os.path.exists(archivo):
                with open(archivo, "r", encoding="utf-8") as f:
                    lineas = f.readlines()
                    print(f"{nombre}: {len(lineas)} líneas")
            else:
                print(f"{nombre}: Archivo no existe")

        print("=" * 80 + "\n")

    except Exception as error:
        print(f"Error al mostrar resumen de logs: {error}")
