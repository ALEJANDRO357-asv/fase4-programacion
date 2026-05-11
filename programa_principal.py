from gestor import GestorSistema
from sistema import *
from excepciones import *
from logger import *


# FUNCION PRINCIPAL

def main():
    """Función principal que ejecuta el sistema completo."""

    print("\n" + "="*80)
    print("INICIANDO SISTEMA INTEGRAL DE GESTIÓN")
    print("Software FJ - Fase 4 UNAD")
    print("="*80 + "\n")

    # Crear instancia del gestor
    gestor = GestorSistema()

    print("\n" + "="*80)
    print("BLOQUE 1: REGISTRO DE CLIENTES (Casos Válidos e Inválidos)")
    print("="*80)

    # OPERACIÓN 1: Cliente válido
    print("\n[OPERACIÓN 1] Registrando cliente válido...")
    try:
        cliente1 = gestor.registrar_cliente(
            nombre="María González",
            documento="1234567890",
            correo="maria.gonzalez@email.com",
            telefono="3001234567"
        )
    except Exception as error:
        print(f"Error capturado: {error}")

    # OPERACIÓN 2: Cliente con documento inválido
    print("\n[OPERACIÓN 2] Intentando registrar cliente con documento inválido...")
    try:
        cliente2 = gestor.registrar_cliente(
            nombre="Pedro Pérez",
            documento="ABC123",  # Inválido: contiene letras
            correo="pedro.perez@email.com"
        )
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 3: Cliente con correo inválido
    print("\n[OPERACIÓN 3] Intentando registrar cliente con correo inválido...")
    try:
        cliente3 = gestor.registrar_cliente(
            nombre="Ana Martínez",
            documento="9876543210",
            correo="correo_invalido"  # Falta @ y dominio
        )
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 4: Cliente con nombre muy corto
    print("\n[OPERACIÓN 4] Intentando registrar cliente con nombre inválido...")
    try:
        cliente4 = gestor.registrar_cliente(
            nombre="Ab",  # Solo 2 caracteres
            documento="5555555555",
            correo="ab@email.com"
        )
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 5: Otro cliente válido
    print("\n[OPERACIÓN 5] Registrando segundo cliente válido...")
    try:
        cliente5 = gestor.registrar_cliente(
            nombre="Carlos Rodríguez",
            documento="1111222233",
            correo="carlos.rodriguez@email.com",
            telefono="3109876543"
        )
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 6: Cliente duplicado
    print("\n[OPERACIÓN 6] Intentando registrar cliente duplicado...")
    try:
        cliente6 = gestor.registrar_cliente(
            nombre="María González",
            documento="1234567890",  # Documento duplicado
            correo="maria2@email.com"
        )
    except Exception as error:
        print(f"Error capturado: {error}")

    # Lista de clientes registrados
    gestor.listar_clientes()

    print("\n" + "="*80)
    print("BLOQUE 2: REGISTRO DE SERVICIOS (Casos Válidos e Inválidos)")
    print("="*80)


    # OPERACIÓN 7: Servicio ReservaSala válido
    print("\n[OPERACIÓN 7] Registrando servicio de Reserva de Sala...")
    try:
        servicio1 = ReservaSala(
            nombre="Sala de Conferencias A",
            costo_base=50000,
            horas=3,
            capacidad=20
        )
        gestor.registrar_servicio(servicio1)
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 8: Servicio con horas negativas
    print("\n[OPERACIÓN 8] Intentando crear servicio con duración negativa...")
    try:
        servicio2 = ReservaSala(
            nombre="Sala VIP",
            costo_base=80000,
            horas=-5,  # Inválido: negativo
            capacidad=10
        )
        gestor.registrar_servicio(servicio2)
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 9: Servicio AlquilerEquipo válido
    print("\n[OPERACIÓN 9] Registrando servicio de Alquiler de Equipo...")
    try:
        servicio3 = AlquilerEquipo(
            nombre="Proyector HD",
            costo_base=30000,
            dias=5,
            tipo_equipo="Audiovisual"
        )
        gestor.registrar_servicio(servicio3)
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 10: Servicio con costo inválido
    print("\n[OPERACIÓN 10] Intentando crear servicio con costo negativo...")
    try:
        servicio4 = AlquilerEquipo(
            nombre="Laptop",
            costo_base=-20000,  # Inválido: negativo
            dias=3,
            tipo_equipo="Computación"
        )
        gestor.registrar_servicio(servicio4)
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 11: Servicio Asesoría válido
    print("\n[OPERACIÓN 11] Registrando servicio de Asesoría...")
    try:
        servicio5 = Asesoria(
            nombre="Asesoría en Python",
            costo_base=100000,
            sesiones=6,
            duracion_sesion=2,
            especialidad="Programación"
        )
        gestor.registrar_servicio(servicio5)
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 12: Servicio con sesiones cero
    print("\n[OPERACIÓN 12] Intentando crear asesoría con cero sesiones...")
    try:
        servicio6 = Asesoria(
            nombre="Asesoría en Java",
            costo_base=90000,
            sesiones=0,  # Inválido: cero sesiones
            duracion_sesion=1.5,
            especialidad="Programación"
        )
        gestor.registrar_servicio(servicio6)
    except Exception as error:
        print(f"Error capturado: {error}")

    # Lista servicios registrados
    gestor.listar_servicios()

    print("\n" + "="*80)
    print("BLOQUE 3: CREACIÓN Y GESTIÓN DE RESERVAS")
    print("="*80)

    # Obtener clientes y servicios para las reservas
    cliente_maria = gestor.buscar_cliente_por_documento("1234567890")
    cliente_carlos = gestor.buscar_cliente_por_documento("1111222233")
    servicio_sala = gestor.buscar_servicio_por_nombre("Sala de Conferencias A")
    servicio_proyector = gestor.buscar_servicio_por_nombre("Proyector HD")
    servicio_asesoria = gestor.buscar_servicio_por_nombre("Asesoría en Python")


    # OPERACIÓN 13: Crear reserva válida
    print("\n[OPERACIÓN 13] Creando reserva de sala...")
    try:
        if cliente_maria and servicio_sala:
            reserva1 = gestor.crear_reserva(cliente_maria, servicio_sala)
            if reserva1:
                reserva1.confirmar(descuento=10, impuesto=19)
                reserva1.mostrar_reserva()
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 14: Crear otra reserva válida
    print("\n[OPERACIÓN 14] Creando reserva de equipo...")
    try:
        if cliente_carlos and servicio_proyector:
            reserva2 = gestor.crear_reserva(cliente_carlos, servicio_proyector)
            if reserva2:
                reserva2.confirmar(descuento=5, impuesto=19)
                reserva2.mostrar_reserva()
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 15: Crear y cancelar reserva
    print("\n[OPERACIÓN 15] Creando y cancelando reserva...")
    try:
        if cliente_maria and servicio_asesoria:
            reserva3 = gestor.crear_reserva(cliente_maria, servicio_asesoria)
            if reserva3:
                reserva3.confirmar(descuento=15, impuesto=19)
                reserva3.mostrar_reserva()
                reserva3.cancelar()
                reserva3.mostrar_reserva()
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 16: Intentar confirmar reserva cancelada
    print("\n[OPERACIÓN 16] Intentando confirmar reserva cancelada...")
    try:
        if cliente_carlos and servicio_sala:
            reserva4 = gestor.crear_reserva(cliente_carlos, servicio_sala)
            if reserva4:
                reserva4.cancelar()
                reserva4.confirmar()  # Debe lanzar excepción
    except Exception as error:
        print(f"Error capturado y manejado: {error}")

    print("\n" + "="*80)
    print("BLOQUE 4: PRUEBAS DE CÁLCULOS CON PARÁMETROS INVÁLIDOS")
    print("="*80)


    # OPERACIÓN 17: Descuento inválido (mayor a 100)
    print("\n[OPERACIÓN 17] Intentando aplicar descuento inválido...")
    try:
        if cliente_maria and servicio_proyector:
            reserva5 = gestor.crear_reserva(cliente_maria, servicio_proyector)
            if reserva5:
                reserva5.confirmar(descuento=150, impuesto=19)  # Descuento inválido
    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 18: Impuesto negativo
    print("\n[OPERACIÓN 18] Intentando aplicar impuesto negativo...")
    try:
        if cliente_carlos and servicio_asesoria:
            reserva6 = gestor.crear_reserva(cliente_carlos, servicio_asesoria)
            if reserva6:
                reserva6.confirmar(descuento=10, impuesto=-5)  # Impuesto inválido
    except Exception as error:
        print(f"Error capturado: {error}")

    print("\n" + "="*80)
    print("BLOQUE 5: PRUEBAS DE MÉTODOS SOBRECARGADOS")
    print("="*80)


    # OPERACIÓN 19: Probar diferentes cálculos de costo
    print("\n[OPERACIÓN 19] Probando métodos sobrecargados de cálculo...")
    try:
        if servicio_sala:
            print(f"\nServicio: {servicio_sala.nombre}")
            print(f"Costo simple: ${servicio_sala.calcular_costo_simple():,.2f}")
            print(f"Costo con 10% desc: ${servicio_sala.calcular_costo(descuento=10):,.2f}")
            print(f"Costo con IVA 19%: ${servicio_sala.calcular_costo(impuesto=19):,.2f}")
            print(f"Costo con desc 20% e IVA 19%: ${servicio_sala.calcular_costo(20, 19):,.2f}")

        if servicio_proyector:
            print(f"\nServicio: {servicio_proyector.nombre}")
            print(f"Costo normal: ${servicio_proyector.calcular_costo():,.2f}")
            print(f"Costo semanal: ${servicio_proyector.calcular_costo_semanal():,.2f}")

        if servicio_asesoria:
            print(f"\nServicio: {servicio_asesoria.nombre}")
            print(f"Costo por sesión: ${servicio_asesoria.calcular_costo():,.2f}")
            print(f"Costo por hora: ${servicio_asesoria.calcular_costo_por_hora():,.2f}")

    except Exception as error:
        print(f"Error capturado: {error}")


    # OPERACIÓN 20: Procesar reserva confirmada
    print("\n[OPERACIÓN 20] Procesando reserva confirmada...")
    try:
        reserva_buscar = gestor.buscar_reserva_por_id("RES-1001")
        if reserva_buscar:
            reserva_buscar.procesar()
            reserva_buscar.mostrar_reserva()
    except Exception as error:
        print(f"Error capturado: {error}")

    print("\n" + "="*80)
    print("BLOQUE 6: REPORTES Y ESTADÍSTICAS FINALES")
    print("="*80)

    # Listados finales
    gestor.listar_clientes()
    gestor.listar_servicios()
    gestor.listar_reservas()

    # Mostrar estadísticas
    gestor.mostrar_estadisticas()

    # Mostrar resumen de logs
    mostrar_resumen_logs()

    print("\n" + "="*80)
    print("SISTEMA FINALIZADO EXITOSAMENTE")
    print("="*80)
    print("\nEl sistema ha ejecutado más de 20 operaciones con casos válidos e inválidos,")
    print("demostrando manejo robusto de excepciones y estabilidad completa.")
    print("\nRevise los archivos de logs generados:")
    print("  - sistema_logs.txt")
    print("  - sistema_errores.txt")
    print("  - sistema_eventos.txt")
    print("="*80 + "\n")


# PUNTO DE ENTRADA
if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
        registrar_evento("Programa interrumpido por el usuario")

    except Exception as error:
        print(f"\n\nError crítico no manejado: {error}")
        registrar_error(error, "Función main() - Error crítico")

    finally:
        print("\n[FIN DEL PROGRAMA]")
        registrar_evento("Programa finalizado")
