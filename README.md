# DayLog [v0.5]

Aplicación personal para registrar tareas diarias, enfocada en simplicidad, control manual del tiempo y persistencia de datos.

## Descripción

DayLog es una herramienta simple para llevar seguimiento del progreso diario, organizada por días y semanas.

El sistema está diseñado para ser claro, mantenible y fácil de extender a futuro.

## Cambios recientes
- Se agregó el sistema de tareas diarias (estructura de booleanos)
- Implementación del guardado de tareas por día
- Persistencia de semanas
- Se definió el flujo principal de la aplicación:
- guardado → avance de día → limpieza → actualización de UI
- `MainWindow` consolida el rol de orquestador del sistema

## Componentes principales
- `StateManager` Maneja la persistencia del estado (día y semana)
- `DayManager` Proporciona la lógica relacionada al día actual
- `TaskManager` Maneja las tareas, su estado y persistencia
- `PanelDaily` Muestra el día anterior, actual y siguiente
- `PanelTitle` Muestra el título con día y semana
- `MainWindow` Coordina la interacción entre estado, datos y UI

## Estructura
```
.
├── main.py
├── panel_daily.py
├── panel_title.py
├── day_manager.py
├── state_manager.py
├── title_manager.py
├── task_manager.py
└── state.json
```

## Estado actual
- Persistencia de estado (día y semana)
- Sistema de tareas funcional
- Guardado por día y por semana
- Flujo de aplicación definido y estable
- UI básica pero clara
- Separación de responsabilidades

## Próximamente
- *Mejorar estructura interna*
- *Crear ejecutable de la aplicación*