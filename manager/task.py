# | [ Dia 9 ]
# | ~/manager/task.py
# | Administrador encargado de guardar y cargar tareas
# |
# | Maneja las semanas y días pertenecientes
# | al ciclo actual.
# |
# | Cada semana se almacena como un archivo JSON:
# | week_1.json
# | week_2.json
# | etc...
# |
# | Estructura base:
# | [
# |     [],  <- Lunes
# |     [],  <- Martes
# |     [],  <- Miercoles
# |     [],  <- Jueves
# |     [],  <- Viernes
# |     [],  <- Sabado
# |     []   <- Domingo
# | ]

import json

from manager.cycle import CycleManager


class TaskManager:
    """
    Maneja el almacenamiento de tareas.

    Se encarga de:
    - Crear semanas vacías
    - Cargar semanas
    - Guardar semanas completas
    - Guardar tareas de días específicos
    - Obtener la semana actual
    """

    def __init__(self):
        # Administrador del ciclo actual
        self.cycle = CycleManager()

        # Ruta base del ciclo activo
        self.base_path = self.cycle.current_cycle_path()

        # Carpeta donde se guardan las semanas
        self.weeks_folder = self.base_path / "weeks"

    def _ensure_directory(self):
        """
        [Interno]

        Asegura que exista la estructura
        principal del ciclo actual.
        """

        self.base_path.mkdir(parents=True, exist_ok=True)

    def _get_week_path(self, week):
        """
        [Interno]

        Devuelve la ruta del archivo
        correspondiente a una semana.

        Ejemplo:
        week_1.json

        Parameters
        ----------
        week : int
            Número de semana.

        Returns
        -------
        Path
            Ruta del archivo semanal.
        """

        return self.weeks_folder / f"week_{week}.json"

    def _create_empty_week(self):
        """
        [Interno]

        Crea una estructura vacía
        para una semana completa.

        Returns
        -------
        list
            Lista con 7 días vacíos.
        """

        return [[], [], [], [], [], [], []]

    def load_week(self, week):
        """
        Carga una semana desde su archivo.

        Si la semana no existe,
        se crea automáticamente.

        Parameters
        ----------
        week : int
            Número de semana.

        Returns
        -------
        list
            Contenido completo de la semana.
        """

        self._ensure_directory()

        path = self._get_week_path(week)

        # Si la semana no existe,
        # crea una nueva estructura vacía
        if not path.exists():
            data = self._create_empty_week()

            path.write_text(json.dumps(data))

            return data

        return json.loads(path.read_text())

    def save_week(self, week, data):
        """
        Guarda una semana completa.

        Parameters
        ----------
        week : int
            Número de semana.

        data : list
            Datos completos de la semana.
        """

        path = self._get_week_path(week)

        path.write_text(json.dumps(data, indent=4))

    def save_day(self, week, day, tasks):
        """
        Guarda las tareas de un día específico.

        Parameters
        ----------
        week : int
            Semana a modificar.

        day : int
            Índice del día.

        tasks : list
            Lista de tareas del día.
        """

        # Carga la semana actual
        data = self.load_week(week)

        # Reemplaza únicamente el día indicado
        data[day] = tasks

        # Guarda nuevamente la semana
        self.save_week(week, data)

    def current_week(self):
        """
        Devuelve la semana actual del ciclo.

        Returns
        -------
        str
            Número de semana actual.
        """

        path = self.base_path / "state_week.json"

        with open(path, "r") as file:
            week = json.load(file)

        return str(week["week"])