# | [ Dia 6 ]
# | ~/manager/state.py
# | Controlador principal del estado, se encarga de guardar el presente (dia y semana)

import json
from pathlib import Path


class StateManager:
    def __init__(self):
        self.base_dir = Path.home() / ".daylog"
        self.base_dir.mkdir(exist_ok=True)

        self.path = self.base_dir / "state.json"

        self._initialize()

    def _initialize(self):
        """
        Crea state.json si no existe.
        """

        if not self.path.exists():
            self.save({
                "cycle": 1,
                "day": 0
            })

    def load(self) -> dict:
        """
        Lee y devuelve el contenido de state.json
        """

        with open(self.path, "r") as file:
            return json.load(file)

    def save(self, data: dict):
        """
        Sobrescribe state.json
        """

        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)

    def update(self, **kwargs):
        """
        Actualiza claves específicas sin perder el resto.
        """

        data = self.load()

        data.update(kwargs)

        self.save(data)