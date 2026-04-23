# | [ Dia 7 ]
# | ~/panel/counter.py
# | Archivo que maneja el panel del contador

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

from manager.counter import CounterManager

class PanelCounter(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de tamaño del panel
        self.setMaximumWidth(100)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        # Logica del contador
        self.counter = CounterManager()

        # Lista para guardar los labels
        self.labels = []

        # Lista que contiene los datos principales
        tasks = self.counter.get_counts()

        # Layout principal
        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignLeft)

        for task in tasks:
            label = QLabel(str(task))
            label.setAlignment(Qt.AlignCenter)
            self.labels.append(label)
            layout.addWidget(label)
        
        self.setLayout(layout)

    def update_counter(self):
        tasks = self.counter.get_counts()

        for i, value in enumerate(tasks):
            self.labels[i].setText(str(value))