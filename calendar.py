# | [ Dia 2 ]
# | ~/calendar.py
# | Archivo que contiene la logica del calendario interno.

class CalendarManager():
    def __init__(self):
        self.days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.index = 0
    
    # Obtener el dia actual
    def get_day(self):
        return self.days[self.index]
    
    def previous_day(self):
        day = self.index - 1
        if day == -1:
            day = 6
            return self.days[day]
        else:
            return self.days[day]
    
    def later_day(self):
        day = self.index + 1
        if day == 7:
            day = 0
            return self.days[day]
        else:
            return self.days[day]
    
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