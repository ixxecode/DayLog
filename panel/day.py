# | [ Dia 9 ]
# | ~/panel/day.py
# | Panel visual encargado de mostrar los días
# |
# | El panel enseña:
# | - Día anterior
# | - Día actual
# | - Día siguiente
# |
# | Ejemplo:
# | Lunes
# | Martes
# | Miercoles

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

from manager.day import DayManager
from manager.state import StateManager


class PanelDay(QWidget):
    """
    Panel encargado de representar visualmente
    la navegación entre días.

    Se conecta con DayManager para:
    - Obtener el día actual
    - Obtener el día anterior
    - Obtener el siguiente día
    """

    def __init__(self):
        super().__init__()

        # Administrador de días
        self.day = DayManager()

        # Estado global de DayLog
        self.state = StateManager()

        # Obtiene todos los días necesarios
        days = self._get_days()

        # Labels principales
        self.previous_title = QLabel(days["previous"])
        self.actual_title = QLabel(days["actual"])
        self.later_title = QLabel(days["later"])

        # Nombres utilizados por QSS/stylesheets
        self.setObjectName("daysContainer")

        self.previous_title.setObjectName("dayMuted")
        self.actual_title.setObjectName("dayActive")
        self.later_title.setObjectName("dayMuted")

        # Centrado de texto
        self.previous_title.setAlignment(Qt.AlignCenter)
        self.actual_title.setAlignment(Qt.AlignCenter)
        self.later_title.setAlignment(Qt.AlignCenter)

        # Permite aplicar estilos visuales
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Layout principal vertical
        layout = QVBoxLayout()

        layout.setContentsMargins(5, 5, 5, 5)

        layout.setSpacing(0)

        layout.addWidget(self.previous_title)
        layout.addWidget(self.actual_title)
        layout.addWidget(self.later_title)

        # Guarda el layout final
        self.setLayout(layout)

    def _get_days(self):
        """
        [Interno]

        Obtiene los días necesarios para el panel.

        Returns
        -------
        dict
            Diccionario con:
            - previous
            - actual
            - later
        """

        return {
            "previous": self.day.previous_day(),
            "actual": self.day.get_day(),
            "later": self.day.later_day()
        }

    def update_panel(self):
        """
        Actualiza todos los textos visibles
        del panel diario.
        """

        days = self._get_days()

        self.previous_title.setText(days["previous"])
        self.actual_title.setText(days["actual"])
        self.later_title.setText(days["later"])