# | [ Dia 9 ]
# | ~/manager/counter.py
# | Administrador encargado de contar tareas completadas
# |
# | Recorre todas las semanas guardadas en ~/.daylog/weeks
# | y suma cuántas veces fue completada cada tarea.
# |
# | Ejemplo:
# | Si la tarea "Estudiar" aparece en la posición 0,
# | el contador guardará cuántos True existen en ese índice.

import json
from pathlib import Path
from typing import List


class CounterManager():
    """
    Maneja el conteo global de tareas completadas.

    Revisa cada archivo semanal y acumula la cantidad
    de tareas marcadas como True.
    """

    def __init__(self):
        # Carpeta donde se almacenan las semanas
        self.weeks_dir = Path.home() / ".daylog" / "weeks"

        # Lista de contadores:
        # [0, 0, 0, 0, 0, 0]
        #
        # Cada posición representa una tarea distinta.
        self.counts = [0] * 6

    def _load_week(self, file_path: Path) -> List[List[bool]]:
        """
        [Interno]

        Abre y devuelve el contenido de una semana.

        Parameters
        ----------
        file_path : Path
            Ruta del archivo JSON semanal.

        Returns
        -------
        List[List[bool]]
            Semana convertida en listas de booleanos.
        """

        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _compute(self):
        """
        [Interno]

        Recorre todas las semanas guardadas y actualiza
        los contadores de tareas completadas.
        """

        # Reinicia los contadores antes de recalcular
        self.counts = [0] * 6

        # Busca todos los archivos:
        # week_1.json
        # week_2.json
        # etc...
        for file in self.weeks_dir.glob("week_*.json"):
            week = self._load_week(file)

            # Recorre cada día de la semana
            for day in week:

                # Recorre cada tarea del día
                for task_index in range(len(day)):

                    # Si la tarea fue completada:
                    if day[task_index] is True:
                        self.counts[task_index] += 1

    def get_counts(self) -> List[int]:
        """
        Ejecuta el cálculo y devuelve los contadores.

        Returns
        -------
        List[int]
            Lista con la cantidad total de tareas completadas.
        """

        self._compute()
        return self.counts