# | [ Dia 7 ]
# | ~/manager/counter.py
# | Archivo que maneja la logica del contador

import json
from pathlib import Path
from typing import List


class CounterManager():
    def __init__(self):
        # Path de la carpeta weeks + contador de tareas
        self.weeks_dir = Path.home() / ".daylog" / "weeks"
        self.counts = [0] * 6

    # [Interno] Metodo que lee la semana
    def _load_week(self, file_path: Path) -> List[List[bool]]:
        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    # [Interna] Metodo que se encarga de leer y guardar las tareas
    def _compute(self):
        self.counts = [0] * 6 # Reset de los contadores

        for file in self.weeks_dir.glob("week_*.json"):
            week = self._load_week(file)

            for day in week:
                for task_index in range(len(day)):
                    if day[task_index] is True:
                        self.counts[task_index] += 1

    # Metodo que ejecuta y devuelve el contenido de counts en una lista de enteros
    def get_counts(self) -> List[int]:
        self._compute()
        return self.counts