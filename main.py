# | [ Dia 1 ]
# | ~/main.py
# | Archivo que contiene la interfaz principal.

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QSize 
import sys

from calendar import CalendarManager

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()  
        self.setFixedSize(QSize(300, 200)) 
        self.setWindowTitle("DayLog")

        # Widget central
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout) 

        # Label + Calendario
        self.calendar = CalendarManager()
        self.day = self.calendar.get_day()
        self.tittle = QLabel(f"{self.day}")

        # Botones de next, reset, y se crea su layout horizontal
        self.next_button = QPushButton("Next Day")
        self.reset_button = QPushButton("Reset Week")
        layout_button = QHBoxLayout()
        layout_button.addWidget(self.next_button)
        layout_button.addWidget(self.reset_button)

        # Conecto las señales de ambos botones
        self.next_button.clicked.connect(self.next_day)
        self.reset_button.clicked.connect(self.reset_week)

        # Agrego las cosas al layout central
        central_layout.addWidget(self.tittle)
        central_layout.addLayout(layout_button)

        self.setCentralWidget(central_widget) 
    
    # Actualiza el label
    def update_label(self):
        self.day = self.calendar.get_day()
        self.tittle.setText(self.day)

    # Reinicia la semana
    def reset_week(self):
        self.calendar.reset_week()
        self.update_label()

    # Avanza al dia siquiente
    def next_day(self):
        dom = self.calendar.is_last_day()
        if dom:
            self.reset_week()
        else:
            self.calendar.next_day()
            self.update_label()

if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_())