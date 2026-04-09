# | [ Dia 2 ]
# | ~/main.py
# | Archivo que contiene la interfaz principal.

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSize 
import sys

from panel_daily import PanelDaily

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()  
        self.setFixedSize(QSize(300, 150)) 
        self.setWindowTitle("DayLog")

        # Widget central
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout) 

        # Panel Diario
        self.panel = PanelDaily()

        # Botones de next, reset, y se crea su layout horizontal
        self.next_button = QPushButton("Next Day")
        self.reset_button = QPushButton("Reset Week")
        layout_button = QHBoxLayout()
        layout_button.addWidget(self.next_button)
        layout_button.addWidget(self.reset_button)

        # Conecto las señales de ambos botones
        self.next_button.clicked.connect(self.panel.next_day)
        self.reset_button.clicked.connect(self.panel.reset_week)

        # Agrego las cosas al layout central
        central_layout.addWidget(self.panel)
        central_layout.addLayout(layout_button)

        self.setCentralWidget(central_widget) 
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_())