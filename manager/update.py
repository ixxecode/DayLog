# | [ Dia 8 ]
# | ~/manager/update.py
# | Archivo que maneja el avance diario/semanal del programa

from manager.state import StateManager
from manager.task import TaskManager
from manager.cycle import CycleManager


class UpdateManager:
    def __init__(self):
        self.state = StateManager()
        self.task = TaskManager()
        self.cycle = CycleManager()

    def next_day(self, tasks):
        """
        Guarda las tareas y avanza el día.
        """

        state = self.state.load()

        week = self.task.current_week()
        day = state["day"]

        # Guardar tareas del día actual
        self.task.save_day(week, day, tasks)

        # Avanzar día
        new_day = self.state.next_day()

        # Si vuelve a lunes, avanzar semana
        if new_day == 0:
            self.cycle.next_week()