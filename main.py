# | [ Dia 4 ]
# | ~/main.py
# | Archivo que contiene la interfaz principal.

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSize 
import sys

from state_manager import StateManager
from panel_daily import PanelDaily
from panel_title import PanelTitle

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()  
        self.setFixedSize(QSize(300, 150)) 
        self.setWindowTitle("DayLog")

        # Widget central
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout) 

        # Panel Diario + Panel del titulo + estado actual
        self.panel = PanelDaily()
        self.title = PanelTitle()
        self.state = StateManager()

        # Boton de next y creo su layout horizontal
        self.next_button = QPushButton("Next Day")
        layout_button = QHBoxLayout()
        layout_button.addWidget(self.next_button)

        # Conecto la señal del boton
        self.next_button.clicked.connect(self.next_day)

        # Agrego las cosas al layout central
        central_layout.addWidget(self.title)
        central_layout.addWidget(self.panel)
        central_layout.addLayout(layout_button)

        self.setCentralWidget(central_widget) 

    def next_day(self):
        self.state.next_day()
        self.panel.update_panel()
        self.title.update_title()
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_())