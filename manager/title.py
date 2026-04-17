# | [ Dia 6 ]
# | ~/manager/title.py
# | Archivo que lee el estado actual de la semana

from manager.state import StateManager
from manager.day import DayManager

class TitleManager():
    def __init__(self):

        # Guardo el estado y el dia
        self.state_manager = StateManager()
        self.day_manager = DayManager()

    def message(self):
        state = self.state_manager.get_state() # Guardo el estado actual
        day = self.day_manager.get_day() # Guardo el dia actual
        week = state["week"] # Obtengo la semana actual
        return f"Dia {day}\nSemana {week}"