# Sistema Integral de Gestión de Clientes, Servicios y Reservas

**Software FJ - Fase 4 UNAD**

Sistema desarrollado como parte del componente práctico de la Fase 4 del curso de Programación (213023) de la Universidad Nacional Abierta y a Distancia (UNAD).

## Descripción

Sistema integral orientado a objetos para la gestión de clientes, servicios y reservas de la empresa Software FJ. El sistema implementa principios avanzados de Programación Orientada a Objetos (POO) y manejo robusto de excepciones.

## Características Principales

### 1. Programación Orientada a Objetos
- ✓ **Abstracción**: Clases abstractas `Persona` y `Servicio`
- ✓ **Herencia**: `Cliente` hereda de `Persona`; servicios especializados heredan de `Servicio`
- ✓ **Polimorfismo**: Métodos abstractos implementados en clases derivadas
- ✓ **Encapsulación**: Atributos privados con getters y validaciones

### 2. Manejo Avanzado de Excepciones
- Excepciones personalizadas con códigos de error
- Uso de bloques `try/except`, `try/except/else`, `try/except/finally`
- Encadenamiento de excepciones
- Validaciones exhaustivas en todas las operaciones

### 3. Sistema de Logging Robusto
- Registro de eventos en tiempo real
- Timestamps en todos los registros
- Tres archivos de log especializados:
  - `sistema_logs.txt`: Logs generales
  - `sistema_errores.txt`: Errores detallados
  - `sistema_eventos.txt`: Eventos exitosos

### 4. Métodos Sobrecargados
- Múltiples formas de calcular costos
- Opciones de descuentos e impuestos
- Cálculos especializados por tipo de servicio

## Estructura del Proyecto

```
fase4-programacion/
│
├── excepciones.py          # Excepciones personalizadas del sistema
├── logger.py               # Sistema de logging con timestamps
├── sistema.py              # Clases principales (Persona, Cliente, Servicio, Reserva)
├── gestor.py               # Gestor del sistema (CRUD y operaciones)
├── programa_principal.py   # Programa principal con 20+ operaciones de prueba
├── cliente.py              # (Archivo anterior de compañeros)
├── Main.py                 # (Archivo anterior de compañeros)
├── README.md               # Este archivo
│
└── Logs generados (al ejecutar):
    ├── sistema_logs.txt
    ├── sistema_errores.txt
    └── sistema_eventos.txt
```

## Instalación y Ejecución

### Requisitos
- Python 3.8 o superior
- No requiere bibliotecas externas

### Ejecución

```bash
# Ejecutar el programa principal
python programa_principal.py
```

El sistema ejecutará automáticamente más de 20 operaciones de prueba con casos válidos e inválidos.

## Autores

Grupo de estudiantes UNAD - Curso Programación 213023
- Fase 4 - Componente Práctico
- Mayo 2026
