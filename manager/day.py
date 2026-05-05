# | [ Dia 9 ]
# | ~/manager/day.py
# | Administrador encargado del calendario interno
# |
# | Maneja la navegación entre días utilizando
# | el índice guardado en StateManager.
# |
# | Ejemplo:
# | 0 -> Lunes
# | 1 -> Martes
# | ...
# | 6 -> Domingo

from manager.state import StateManager


class DayManager():
    """
    Maneja los días internos de DayLog.

    Se encarga de:
    - Obtener el día actual
    - Consultar el día anterior
    - Consultar el día siguiente
    - Detectar el último día de la semana
    """

    def __init__(self):
        # Lista base de días
        self.days = [
            "Lunes",
            "Martes",
            "Miercoles",
            "Jueves",
            "Viernes",
            "Sabado",
            "Domingo"
        ]

        # Estado global de DayLog
        self.state = StateManager()

    def _get_index(self):
        """
        [Interno]

        Obtiene el índice actual del día
        desde StateManager.

        Returns
        -------
        int
            Índice del día actual.
        """

        state = self.state.load()

        return state["day"]

    def get_day(self):
        """
        Devuelve el día actual.

        Returns
        -------
        str
            Nombre del día actual.
        """

        return self.days[self._get_index()]

    def previous_day(self):
        """
        Devuelve el día anterior al actual.

        Si el día actual es Lunes,
        vuelve automáticamente a Domingo.

        Returns
        -------
        str
            Nombre del día anterior.
        """

        index = self._get_index() - 1

        # Si el índice baja de 0,
        # vuelve al último día
        if index < 0:
            index = 6

        return self.days[index]

    def later_day(self):
        """
        Devuelve el día posterior al actual.

        Si el día actual es Domingo,
        vuelve automáticamente a Lunes.

        Returns
        -------
        str
            Nombre del siguiente día.
        """

        index = self._get_index() + 1

        # Si supera el último índice,
        # vuelve al inicio
        if index > 6:
            index = 0

        return self.days[index]

    def is_last_day(self):
        """
        Comprueba si el día actual
        es el último de la semana.

        Returns
        -------
        bool
            True si es Domingo.
        """

        return self._get_index() == len(self.days) - 1