# | [Dia 4]
# | ~/week_manager.py
# | Archivo que lee el estado actual de la semana

from state_manager import StateManager
from day_manager import DayManager

class TitleManager():
    def __init__(self):

        # Guardo el estado y el dia
        self.state_manager = StateManager()
        self.day_manager = DayManager()

    def message(self):
        state = self.state_manager.get_state() # Guardo el estado actual
        day = self.day_manager.get_day() # Guardo el dia actual
        week = state["week"] # Obtengo la semana actual
        return f"Dia {day} - Semana {week}"