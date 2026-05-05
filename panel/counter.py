# | [ Dia 9 ]
# | ~/panel/counter.py
# | Panel visual encargado de mostrar los contadores
# |
# | Cada número representa cuántas veces fue
# | completada una tarea a lo largo de las semanas.
# |
# | Ejemplo:
# | 15
# | 08
# | 21

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

from manager.counter import CounterManager


class PanelCounter(QWidget):
    """
    Panel lateral que muestra los contadores
    globales de tareas completadas.

    Se conecta con CounterManager para:
    - Obtener los valores actuales
    - Crear los labels visuales
    - Actualizar el contenido en pantalla
    """

    def __init__(self):
        super().__init__()

        # Configuración del tamaño del panel
        self.setMaximumWidth(100)

        self.setSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Expanding
        )

        # Lógica del contador
        self.counter = CounterManager()

        # Lista encargada de guardar
        # todos los labels visuales
        self.labels = []

        # Datos principales del contador
        tasks = self.counter.get_counts()

        # Layout principal vertical
        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignLeft)

        # Crea un label por cada contador
        for task in tasks:
            label = QLabel(str(task))

            label.setAlignment(Qt.AlignCenter)

            # Guarda referencia del label
            self.labels.append(label)

            # Agrega el label al layout
            layout.addWidget(label)

        self.setLayout(layout)

    def update_counter(self):
        """
        Actualiza todos los valores mostrados
        en el panel.
        """

        tasks = self.counter.get_counts()

        # Recorre cada label y reemplaza
        # su contenido por el nuevo valor
        for i, value in enumerate(tasks):
            self.labels[i].setText(str(value))