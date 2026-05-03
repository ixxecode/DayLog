# DayLog

Aplicación personal para registrar tareas diarias, enfocada en simplicidad, control manual del tiempo y persistencia de datos.

## Historial de versiones

### [1.3] Integración del sistema de ciclos

* Integración del sistema de ciclos dentro del flujo principal de la aplicación
* Inicialización automática de la estructura persistente al iniciar `main.py`
* Eliminación de la dependencia de `test.py` para crear la estructura interna
* Implementación del avance automático de semanas al finalizar un ciclo semanal
* Creación automática de nuevos archivos `week_X.json`
* Refactorización parcial de la lógica de actualización mediante `UpdateManager`
* Separación más clara entre UI, persistencia y coordinación interna
* Adaptación de `TaskManager` para trabajar con rutas dinámicas según el ciclo actual
* Reorganización interna de persistencia usando:

  * `state.json` para estado global
  * `state_week.json` para progreso interno de cada ciclo

### [1.2] Implementación inicial del sistema de ciclos

* Se agregó una nueva arquitectura basada en ciclos (`cycle_X`)
* Separación entre estado global y estado interno de cada ciclo
* Implementación inicial de `CycleManager`
* Creación automática de carpetas persistentes dentro de `~/.daylog`
* Implementación de `state_week.json` para almacenar la semana actual de cada ciclo
* Separación de responsabilidades entre manejo de estado (`StateManager`) y manejo de ciclos (`CycleManager`)
* Preparación de la estructura para futuras funciones de edición de tareas

### [1.1.1] Correcciones al launcher

* Se corrigió la ruta del launcher (`./build/dist/main` -> `./build/dist/daylog`)
* Se agregó una advertencia en el launcher en forma de comentario con la etiqueta `AVISO`

#### > AVISO <

* Si se cambia el nombre del ejecutable, es necesario actualizar manualmente la ruta en el launcher (`./build/dist/...`)
* El error ocurre cuando el nombre del archivo en `dist` no coincide con el definido en el script

### [1.1]

* Implementación de un contador visual de tareas
* Separación clara entre lógica de conteo (`CounterManager`) y UI (`PanelCounter`)
* Refinamiento del layout para soportar el nuevo panel
* Ajustes menores en estructura para mantener consistencia

## Estructura

```bash
DayLog/
├── main.py              # Archivo principal (v1.3)
├── panel/               # UI
├── manager/             # Lógica de negocio
├── assets/              # Recursos y documentación
├── build/               # Artefactos de build (PyInstaller)
└── daylog               # Ejecutable (v1.1)
```

## Cómo ejecutar

Actualmente el ejecutable (`daylog`) aún no incluye los cambios internos implementados en la versión 1.3.

Para ejecutar correctamente la versión actual:

1. Abrir una terminal dentro de la carpeta del proyecto

2. Ejecutar la aplicación desde `main.py`:

```bash
python main.py
```