# | [ Dia 6 ]
# | ~/manager/day.py
# | Archivo que contiene la logica del calendario interno.

from manager.state import StateManager

class DayManager():
    def __init__(self):
        self.days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.state = StateManager()
    
    # [Interna] Permite obtener el indice desde StateManager
    def _get_index(self):
        state = self.state.get_state()
        return state["day"]
    
    # Obtener el dia actual
    def get_day(self):
        return self.days[self._get_index()]
    
    # Obtener el dia previo al actual
    def previous_day(self):
        index = self._get_index() - 1
        if index < 0:
            index = 6
        return self.days[index]

    # Obtener el dia posterior al actual
    def later_day(self):
        index = self._get_index() + 1
        if index > 6:
            index = 0
        return self.days[index]
    
    # Saber si es el ultimo dia
    def is_last_day(self):
        return self._get_index() == len(self.days) - 1