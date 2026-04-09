# DayLog [v0.2]

Aplicación personal para registrar tareas diarias, enfocada en simplicidad y control manual del tiempo.

## Estructura actual

### main.py
Contiene la ventana principal de la aplicación.

- Crea la `MainWindow`
- Integra el componente `PanelDaily`
- Incluye botones para avanzar el día y reiniciar la semana
- Conecta la interfaz con la lógica del panel

### calendar.py
Contiene la lógica del calendario interno.

- Maneja una semana de 7 días (Lunes a Domingo)
- Controla el día actual mediante un índice
- Permite avanzar de día (`next_day`)
- Permite reiniciar la semana (`reset_week`)
- Proporciona:
  - Día actual (`get_day`)
  - Día anterior (`previous_day`)
  - Día siguiente (`later_day`)

### panel_daily.py
Componente de interfaz que representa el estado diario.

- Muestra:
  - Día anterior
  - Día actual
  - Día siguiente
- Resalta visualmente el día actual
- Se encarga de:
  - Actualizar la UI cuando cambia el estado
  - Gestionar la interacción con el calendario
- Actúa como puente entre la lógica (`CalendarManager`) y la interfaz

## Estado del proyecto

Actualmente la aplicación:

- Muestra el día actual junto con el anterior y el siguiente
- Permite avanzar día a día
- Reinicia la semana al llegar al final
- Tiene un componente dedicado (`PanelDaily`) que centraliza la lógica visual del día

## Notas

Este proyecto está diseñado como una herramienta personal, priorizando claridad, control y experimentación sobre complejidad o perfección.