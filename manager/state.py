# | [ Dia 9 ]
# | ~/manager/state.py
# | Administrador principal del estado global de DayLog
# |
# | Este archivo representa el "presente" de la aplicación.
# |
# | Se encarga de guardar información importante como:
# | - Ciclo actual
# | - Día actual
# |
# | Toda esta información se almacena en:
# | ~/.daylog/state.json

import json
from pathlib import Path


class StateManager:
    """
    Maneja el estado principal de DayLog.

    Se encarga de:
    - Crear state.json
    - Leer el estado actual
    - Guardar cambios
    - Actualizar valores específicos
    - Avanzar entre días
    """

    def __init__(self):
        # Carpeta principal de DayLog
        self.base_dir = Path.home() / ".daylog"

        # Crea la carpeta si no existe
        self.base_dir.mkdir(exist_ok=True)

        # Archivo principal del estado
        self.path = self.base_dir / "state.json"

        # Inicializa el archivo base
        self._initialize()

    def _initialize(self):
        """
        [Interno]

        Crea state.json si todavía no existe.

        Estado inicial:
        {
            "cycle": 1,
            "day": 0
        }
        """

        if not self.path.exists():
            self.save({
                "cycle": 1,
                "day": 0
            })

    def load(self) -> dict:
        """
        Lee y devuelve el contenido de state.json.

        Returns
        -------
        dict
            Estado actual de DayLog.
        """

        with open(self.path, "r") as file:
            return json.load(file)

    def save(self, data: dict):
        """
        Sobrescribe completamente state.json.

        Parameters
        ----------
        data : dict
            Nuevo contenido a guardar.
        """

        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)

    def update(self, **kwargs):
        """
        Actualiza claves específicas sin perder
        el resto del contenido.

        Ejemplo:
        update(day=3)

        Parameters
        ----------
        **kwargs
            Claves y valores a actualizar.
        """

        # Carga el estado actual
        data = self.load()

        # Actualiza únicamente
        # las claves indicadas
        data.update(kwargs)

        # Guarda el nuevo estado
        self.save(data)

    def next_day(self):
        """
        Avanza al siguiente día.

        Si el día actual supera Domingo,
        vuelve automáticamente a Lunes.

        Returns
        -------
        int
            Nuevo índice del día actual.
        """

        data = self.load()

        day = data["day"]

        # Avanza un día
        day += 1

        # Reinicia la semana
        # al superar Domingo
        if day > 6:
            day = 0

        # Guarda el nuevo día
        self.update(day=day)

        return day