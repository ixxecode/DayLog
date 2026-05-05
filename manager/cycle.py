# | [ Dia 9 ]
# | ~/manager/cycle.py
# | Administrador encargado de manejar los ciclos y semanas
# |
# | Cada ciclo funciona como una etapa independiente
# | dentro de DayLog.
# |
# | Ejemplo:
# | cycle_1/
# | cycle_2/
# |
# | Cada ciclo contiene sus propias semanas y
# | un archivo que guarda la semana actual.

from pathlib import Path
import json

from manager.state import StateManager


class CycleManager:
    """
    Maneja la estructura y navegación de ciclos.

    Se encarga de:
    - Obtener el ciclo actual
    - Crear carpetas necesarias
    - Controlar la semana activa
    - Avanzar entre semanas
    """

    def __init__(self):
        # Estado global de DayLog
        self.state = StateManager()

        # Carpeta principal:
        # ~/.daylog
        self.base_dir = Path.home() / ".daylog"

    def current_cycle(self) -> int:
        """
        Devuelve el número del ciclo actual.

        Returns
        -------
        int
            Número del ciclo activo.
        """

        state = self.state.load()

        return state["cycle"]

    def current_cycle_path(self) -> Path:
        """
        Devuelve la ruta del ciclo actual.

        Ejemplo:
        ~/.daylog/cycle_1

        Returns
        -------
        Path
            Ruta completa del ciclo activo.
        """

        cycle = self.current_cycle()

        return self.base_dir / f"cycle_{cycle}"

    def initialize_cycle(self):
        """
        Crea la estructura básica del ciclo actual
        si todavía no existe.

        Estructura creada:
        cycle_x/
        ├── weeks/
        └── state_week.json
        """

        cycle_path = self.current_cycle_path()

        weeks_path = cycle_path / "weeks"

        # Crea las carpetas necesarias
        cycle_path.mkdir(exist_ok=True)
        weeks_path.mkdir(exist_ok=True)

        # Archivo encargado de guardar
        # la semana actual del ciclo
        state_week = cycle_path / "state_week.json"

        # Si el archivo no existe,
        # inicia la semana en 1
        if not state_week.exists():
            with open(state_week, "w") as file:
                json.dump({"week": 1}, file, indent=4)

    def current_week(self) -> int:
        """
        Devuelve la semana actual del ciclo activo.

        Returns
        -------
        int
            Semana actual.
        """

        cycle_path = self.current_cycle_path()

        state_week = cycle_path / "state_week.json"

        with open(state_week, "r") as file:
            data = json.load(file)

        return data["week"]

    def current_weeks_path(self) -> Path:
        """
        Devuelve la carpeta weeks del ciclo actual.

        Ejemplo:
        ~/.daylog/cycle_1/weeks

        Returns
        -------
        Path
            Ruta de la carpeta weeks.
        """

        return self.current_cycle_path() / "weeks"

    def next_week(self):
        """
        Avanza a la siguiente semana del ciclo.

        Incrementa el valor guardado en:
        state_week.json
        """

        path = self.current_cycle_path() / "state_week.json"

        # Lee la semana actual
        with open(path, "r") as file:
            data = json.load(file)

        # Avanza una semana
        data["week"] += 1

        # Guarda el nuevo valor
        with open(path, "w") as file:
            json.dump(data, file, indent=4)