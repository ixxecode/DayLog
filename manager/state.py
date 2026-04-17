# | [ Dia 6 ]
# | ~/manager/state.py
# | Controlador principal del estado, se encarga de guardar el presente (dia y semana)

import json
from pathlib import Path

class StateManager():
    def __init__(self):
        # Carpeta persistente del usuario
        base_dir = Path.home() / ".daylog"
        base_dir.mkdir(exist_ok=True) 

        # Path de state.json
        self._path = base_dir / "state.json"

        if not self._path.exists():
            self._save({"week": 0, "day": 0})
    
    # [Interna] Permite leer el path
    def _load(self):
        with open(self._path, "r") as f:
            return json.load(f)

    # [Interna] Permite guardar la informacion "data" en el path
    def _save(self, data):
        with open(self._path, "w") as f:
            json.dump(data, f, indent=4)
    
    # Obteniendo la informacion de state.json y guardandola en un diccionario
    def get_state(self) -> dict:
        return self._load()

    # Avanza el dia y en caso de llegar al limite reinicia y incrementa la semana
    def next_day(self):
        data = self._load()

        day = data["day"]
        week = data["week"]

        day += 1

        if day > 6:
            day = 0
            week += 1

        self._save({
            "week": week,
            "day": day
        })

        return week, day