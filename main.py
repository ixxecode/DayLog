# | [ Dia 7 ]
# | ~/main.py
# | Archivo que contiene la interfaz principal.

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSize 
import sys

from manager.state import StateManager
from panel.day import PanelDay
from panel.title import PanelTitle
from panel.task import PanelTask
from data.styles import DARK_THEME
from panel.counter import PanelCounter

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__()  
        self.setFixedSize(QSize(350, 200)) 
        self.setWindowTitle("DayLog v1.1")

        # Widget central
        central_widget = QWidget()
        central_layout = QVBoxLayout() #[vertical]
        central_widget.setLayout(central_layout) 

        # Panel Diario + Panel del titulo + estado actual + tareas + contador
        self.panel = PanelDay()
        self.title = PanelTitle()
        self.state = StateManager()
        self.task = PanelTask()
        self.counter = PanelCounter()

        # Boton de next y creo su layout [horizontal]
        self.next_button = QPushButton("Siguiente")
        layout_button = QHBoxLayout()
        layout_button.addWidget(self.next_button)

        # Layout del titulo + boton [vertical]
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.title)
        left_layout.addWidget(self.panel)
        left_layout.addLayout(layout_button)

        # Layout superior + panel diario [Horizontal]
        layout_principal = QHBoxLayout()
        layout_principal.addLayout(left_layout, 1)
        layout_principal.addWidget(self.task, 1)
        layout_principal.addWidget(self.counter, 0)

        # Conecto la señal del boton
        self.next_button.clicked.connect(self.next_day)

        # Agrego las cosas al layout central
        central_layout.addLayout(layout_principal)

        self.setCentralWidget(central_widget) 

    def next_day(self):
        state = self.state.get_state()

        week = state["week"]
        day = state["day"]

        self.task.save_tasks(week, day)
        self.state.next_day()
        self.task.clear_tasks()
        self.panel.update_panel()
        self.title.update_title()
        self.counter.update_counter()
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    app.setStyleSheet(DARK_THEME)
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec())