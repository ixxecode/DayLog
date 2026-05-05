# | [ Dia 9 ]
# | ~/manager/update.py
# | Administrador encargado del avance diario y semanal
# |
# | Controla el cierre de un día dentro de DayLog:
# | - Guarda las tareas actuales
# | - Avanza el día
# | - Detecta cambios de semana
# |
# | Ejemplo:
# | Domingo -> Lunes
# | Al volver a Lunes, también avanza la semana.

from manager.state import StateManager
from manager.task import TaskManager
from manager.cycle import CycleManager


class UpdateManager:
    """
    Maneja el avance interno de DayLog.

    Se encarga de:
    - Guardar tareas del día actual
    - Avanzar al siguiente día
    - Detectar el cambio de semana
    """

    def __init__(self):
        # Estado global de DayLog
        self.state = StateManager()

        # Administrador de tareas
        self.task = TaskManager()

        # Administrador de ciclos/semanas
        self.cycle = CycleManager()

    def next_day(self, tasks):
        """
        Guarda las tareas actuales y avanza el día.

        Si el nuevo día vuelve a Lunes,
        también avanza la semana.

        Parameters
        ----------
        tasks : list
            Lista de tareas del día actual.
        """

        # Obtiene el estado actual
        state = self.state.load()

        # Semana activa
        week = self.task.current_week()

        # Día actual
        day = state["day"]

        # Guarda las tareas del día actual
        self.task.save_day(week, day, tasks)

        # Avanza al siguiente día
        new_day = self.state.next_day()

        # Si vuelve a Lunes,
        # avanza la semana
        if new_day == 0:
            self.cycle.next_week()