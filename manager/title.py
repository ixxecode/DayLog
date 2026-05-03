# | [ Dia 8 ]
# | ~/manager/title.py
# | Archivo que lee el estado actual de la semana

from manager.day import DayManager
from manager.cycle import CycleManager

class TitleManager():
    def __init__(self):
        # Obtenemos el dia y ciclo (para acceder a la semana)
        self.day = DayManager()
        self.cycle = CycleManager()

    def message(self):
        day = self.day.get_day() # Obtener el dia actual
        week = self.cycle.current_week() # Obtener la semana actual
        return f"Dia {day}\nSemana {week}"