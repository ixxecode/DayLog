# | [Dia 2]
# | ~/panel_daily.py
# | Archivo que contiene la logica del panel diario

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from calendar import CalendarManager

class PanelDaily(QWidget):
    def __init__(self):
        super().__init__()

        # Calendario
        self.calendar = CalendarManager()

        # Vairables de dia actual, dia previo, y dia posterior (modificables)
        self.previous_day = self.calendar.previous_day()
        self.actual_day = self.calendar.get_day()
        self.later_day = self.calendar.later_day()

        # Titulos de los dias usando las variables
        self.previous_tittle = QLabel(self.previous_day)
        self.actual_tittle = QLabel(self.actual_day)
        self.later_tittle = QLabel(self.later_day)

        # Creando distincion de dia actual con los demas
        self.previous_tittle.setStyleSheet("Color: #8e8292")
        self.later_tittle.setStyleSheet("Color: #8e8292")

        # Layout principal
        layout = QVBoxLayout()

        layout.addWidget(self.previous_tittle)
        layout.addWidget(self.actual_tittle)
        layout.addWidget(self.later_tittle)

        # Guardamos el layout
        self.setLayout(layout)
    
    # Actualiza el panel
    def update_panel(self):
        self.previous_day = self.calendar.previous_day()
        self.actual_day = self.calendar.get_day()
        self.later_day = self.calendar.later_day()

        self.previous_tittle.setText(self.previous_day)
        self.actual_tittle.setText(self.actual_day)
        self.later_tittle.setText(self.later_day)

    # Resete al semana
    def reset_week(self):
        self.calendar.reset_week()
        self.update_panel()
    
    # Avanza el dia
    def next_day(self):
        dom = self.calendar.is_last_day()
        if dom:
            self.reset_week()
        else:
            self.calendar.next_day()
            self.update_panel()