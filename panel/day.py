# | [ Dia 6 ]
# | ~/panel/day.py
# | Archivo que contiene la logica del panel diario

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

from manager.day import DayManager
from manager.state import StateManager

class PanelDay(QWidget):
    def __init__(self):
        super().__init__()

        # Dia + Estado
        self.day = DayManager()
        self.state = StateManager()

        # Titulos de los dias usando las variables
        days = self._get_days()
        self.previous_title = QLabel(days["previous"])
        self.actual_title = QLabel(days["actual"])
        self.later_title = QLabel(days["later"])

        # Nombres para los estilos
        self.setObjectName("daysContainer")
        self.previous_title.setObjectName("dayMuted")
        self.actual_title.setObjectName("dayActive")
        self.later_title.setObjectName("dayMuted")

        # Centrar los dias
        self.previous_title.setAlignment(Qt.AlignCenter)
        self.actual_title.setAlignment(Qt.AlignCenter)
        self.later_title.setAlignment(Qt.AlignCenter)

        # Permite usar los estilos
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(0)  
        layout.addWidget(self.previous_title)
        layout.addWidget(self.actual_title)
        layout.addWidget(self.later_title)

        # Guardamos el layout
        self.setLayout(layout)
    
    # Obtener los dias y guardarlos en un diccionario
    def _get_days(self):
        return {
            "previous": self.day.previous_day(),
            "actual": self.day.get_day(),
            "later": self.day.later_day()
        }

    # Actualiza el panel
    def update_panel(self):
        days = self._get_days()

        self.previous_title.setText(days["previous"])
        self.actual_title.setText(days["actual"])
        self.later_title.setText(days["later"])