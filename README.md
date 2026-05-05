# DayLog

Aplicación personal para registrar tareas diarias, enfocada en simplicidad, control manual del tiempo y persistencia de datos.

DayLog funciona como un pequeño sistema de seguimiento diario:

* tareas por día
* avance semanal
* persistencia local
* ciclos independientes de progreso

Toda la información se guarda localmente dentro de `~/.daylog`.

---

## Características

* Interfaz simple basada en PySide6
* Sistema de tareas diarias con checkboxes
* Persistencia automática en archivos JSON
* Navegación interna por días y semanas
* Contador global de tareas completadas
* Arquitectura separada entre UI, lógica y persistencia
* Sistema de ciclos independientes (`cycle_X`)

---

## Arquitectura

```bash
DayLog/
├── main.py              # Punto de entrada principal (v1.3.1)
├── panel/               # Componentes visuales (UI)
├── manager/             # Lógica y persistencia
├── data/                # Recursos internos
├── assets/              # Recursos multimedia
├── build/               # Builds y ejecutables
└── daylog               # <<< Ejecutable Linux (v1.1)
```

### Persistencia interna

```bash
~/.daylog/
├── state.json
├── cycle_1/
│   ├── state_week.json
│   └── weeks/
│       ├── week_1.json
│       └── week_2.json
```

* `state.json` guarda el estado global
* `state_week.json` controla la semana actual del ciclo
* `week_X.json` almacena las tareas diarias

---

## Historial de versiones

### [1.3.1] [Actual]

Mejoras generales de documentación y comentarios internos para mantener una estructura más clara, consistente y fácil de mantener.

### [1.3]

Integración completa del sistema de ciclos, automatización del flujo semanal y reorganización de persistencia interna.

### [1.2]

Primera implementación de arquitectura basada en ciclos (`cycle_X`) y separación del estado interno.

### [1.1]

Implementación del contador visual de tareas y mejoras de organización interna.

### [1.0]

Primera versión funcional de DayLog.

---

## Cómo ejecutar

Actualmente el ejecutable (`daylog`) aún no incluye todos los cambios internos de las versiones recientes.

Para ejecutar la versión actual:

```bash
python main.py
```

---

## Tecnologías utilizadas

* Python 3
* PySide6
* JSON
* pathlib
