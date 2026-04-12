# DayLog [v0.3]

Aplicación personal para registrar tareas diarias, enfocada en simplicidad, control manual del tiempo y persistencia de datos.

## Estructura actual

### main.py
Contiene la ventana principal de la aplicación.

- Crea la `MainWindow`
- Integra el componente `PanelDaily`
- Incluye botón para avanzar el día
- Conecta la interfaz con la lógica del panel

---

### panel_daily.py
Componente de interfaz que representa el estado diario.

- Muestra:
  - Día anterior
  - Día actual
  - Día siguiente
- Resalta visualmente el día actual
- Se encarga de:
  - Actualizar la UI cuando cambia el estado
  - Gestionar la interacción con el estado (`StateManager`)
- Actúa como puente entre la lógica (`DayManager`) y la interfaz

---

### day_manager.py
Encargado de la lógica del día actual.

- Maneja una semana de 7 días (Lunes a Domingo)
- Obtiene el día actual desde `StateManager`
- Proporciona:
  - Día actual (`get_day`)
  - Día anterior (`previous_day`)
  - Día siguiente (`later_day`)
- Determina si es el último día de la semana

---

### state_manager.py
Controlador principal del estado persistente.

- Guarda y lee datos desde `state.json`
- Mantiene:
  - Día actual (`day`)
  - Semana actual (`week`)
- Se encarga de:
  - Avanzar el día (`next_day`)
  - Incrementar la semana automáticamente al completar un ciclo
- Centraliza la persistencia para evitar reinicios al cerrar la app

---

### state.json
Archivo de almacenamiento persistente.

Ejemplo:

```json
{
    "week": 0,
    "day": 2
}
```

### Estado del proyecto

#### Actualmente la aplicación:

- Mantiene el estado entre ejecuciones (persistencia)
- Muestra el día actual junto con el anterior y el siguiente
- Permite avanzar día a día
- Incrementa automáticamente la semana al completar 7 días
- Tiene separación clara entre:
  - Estado (StateManager)
  - Lógica (DayManager)
  - Interfaz (PanelDaily)

### Notas

Este proyecto está diseñado como una herramienta personal, priorizando claridad, control y evolución progresiva.

#### La implementación actual sienta las bases para futuras funcionalidades como:

- Sistema completo de semanas
- Registro de tareas por día
- Análisis de hábitos