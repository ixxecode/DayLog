# DayLog [v0.4]

Aplicación personal para registrar tareas diarias, enfocada en simplicidad, control manual del tiempo y persistencia de datos.

---

## Descripción

DayLog es una herramienta simple para llevar seguimiento del progreso diario, organizada por días y semanas.  
El sistema está diseñado para ser claro, mantenible y fácil de extender a futuro.

---

## Cambios recientes

- Se agregó el sistema de título dinámico (`Dia X - Semana X`)
- Se separó la lógica del título en `TitleManager`
- Se movió la responsabilidad de `next_day` a `MainWindow` como orquestador de la app
- Se unificó la actualización de la UI (panel diario + título)

---

## Componentes principales

- **StateManager**  
  Maneja la persistencia del estado (día y semana)

- **DayManager**  
  Proporciona la lógica relacionada al día actual

- **PanelDaily**  
  Muestra el día anterior, actual y siguiente

- **PanelTitle**  
  Muestra el título con día y semana

- **MainWindow**  
  Coordina la interacción entre estado y UI

---

## Estructura
```
.
├── main.py
├── panel_daily.py
├── panel_title.py
├── day_manager.py
├── state_manager.py
├── title_manager.py
└── state.json
```

---

## Estado actual

- Persistencia funcional
- Navegación por días
- Sistema de semanas automático
- UI básica pero clara
- Separación de responsabilidades

---

## Próximamente

- Registro de tareas por día (booleanos)
- Estructura de semanas persistentes (archivos por semana)