# | [ Dia 9 ]
# | ~/manager/title.py
# | Generador del titulo principal mostrado en pantalla
# |
# | Combina el día actual y la semana activa
# | para construir el encabezado utilizado
# | dentro de DayLog.
# |
# | Ejemplo:
# | Dia Martes
# | Semana 3

from manager.day import DayManager
from manager.cycle import CycleManager


class TitleManager():
    """
    Maneja el texto principal mostrado
    en la interfaz de DayLog.

    Se encarga de combinar:
    - Día actual
    - Semana actual
    """

    def __init__(self):
        # Administrador de días
        self.day = DayManager()

        # Administrador de ciclos/semanas
        self.cycle = CycleManager()

    def message(self):
        """
        Genera el título principal.

        Returns
        -------
        str
            Texto con el día y semana actual.
        """

        # Obtiene el día actual
        day = self.day.get_day()

        # Obtiene la semana actual
        week = self.cycle.current_week()

        return f"Dia {day}\nSemana {week}"