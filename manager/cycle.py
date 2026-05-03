# | [ Dia 8 ]
# | ~/manager/cycle.py
# | Archivo que maneja la logica de los ciclos

from pathlib import Path
import json

from manager.state import StateManager


class CycleManager:
    def __init__(self):
        self.state = StateManager()

        self.base_dir = Path.home() / ".daylog"

    def current_cycle(self) -> int:
        state = self.state.load()

        return state["cycle"]

    def current_cycle_path(self) -> Path:
        cycle = self.current_cycle()

        return self.base_dir / f"cycle_{cycle}"

    def initialize_cycle(self):
        """
        Crea la estructura del ciclo actual si no existe.
        """

        cycle_path = self.current_cycle_path()

        weeks_path = cycle_path / "weeks"

        cycle_path.mkdir(exist_ok=True)
        weeks_path.mkdir(exist_ok=True)

        state_week = cycle_path / "state_week.json"

        if not state_week.exists():
            with open(state_week, "w") as file:
                json.dump({"week": 1}, file, indent=4)

    def current_week(self) -> int:
        """
        Devuelve la semana actual del ciclo activo.
        """

        cycle_path = self.current_cycle_path()

        state_week = cycle_path / "state_week.json"

        with open(state_week, "r") as file:
            data = json.load(file)

        return data["week"]
    
    def current_weeks_path(self) -> Path:
        """
        Devuelve la carpeta weeks del ciclo actual.
        """

        return self.current_cycle_path() / "weeks"
    
    def next_week(self):
        path = self.current_cycle_path() / "state_week.json"

        with open(path, "r") as file:
            data = json.load(file)

        data["week"] += 1

        with open(path, "w") as file:
            json.dump(data, file, indent=4)