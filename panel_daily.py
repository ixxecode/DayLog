# | [Dia 4]
# | ~/panel_daily.py
# | Archivo que contiene la logica del panel diario

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from day_manager import DayManager
from state_manager import StateManager

class PanelDaily(QWidget):
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

        # Creando distincion de dia actual con los demas
        self.previous_title.setStyleSheet("Color: #8e8292")
        self.later_title.setStyleSheet("Color: #8e8292")

        # Layout principal
        layout = QVBoxLayout()

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