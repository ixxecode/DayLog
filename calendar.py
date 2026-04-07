# | [ Dia 1 ]
# | ~/calendar.py
# | Archivo que contiene la logica del calendario interno.

class CalendarManager():
    def __init__(self):
        self.days = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
        self.index = 0
    
    # Obtener el dia actual
    def get_day(self):
        return self.days[self.index]
    
    # Avanzar el dia
    def next_day(self):
        if self.index < len(self.days) - 1:
            self.index += 1
    
    # Saber si es el ultimo dia
    def is_last_day(self):
        return self.index == len(self.days) - 1
    
    # Resetear semana
    def reset_week(self):
        self.index = 0