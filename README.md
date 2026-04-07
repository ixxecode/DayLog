# DayLog [v0.1]

Aplicación simple para registrar tareas diarias.

## Estructura actual

### main.py
Contiene la interfaz principal de la aplicación usando PySide6.

- Crea la ventana (`MainWindow`)
- Muestra el día actual en un `QLabel`
- Incluye botones para avanzar el día y reiniciar la semana
- Conecta la interfaz con la lógica del calendario

### calendar.py
Contiene la lógica del calendario interno.

- Maneja una semana de 7 días (Lun a Dom)
- Controla el día actual mediante un índice
- Permite avanzar de día (`next_day`)
- Permite reiniciar la semana (`reset_week`)
- Proporciona el día actual (`get_day`)

## Estado del proyecto

Actualmente la aplicación:
- Muestra el día actual
- Permite avanzar día a día
- Reinicia la semana al llegar al final