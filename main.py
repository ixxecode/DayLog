# | [ Dia 9 ]
# | ~/main.py
# | Archivo principal de DayLog.
# |
# | Desde aquí se construye toda la interfaz:
# | - Título principal
# | - Panel de días
# | - Tareas
# | - Contador
# | - Botón de avance
# |
# | También se conecta la lógica encargada
# | de actualizar el estado interno del programa.

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton
)

from PySide6.QtCore import QSize

import sys

from panel.day import PanelDay
from panel.title import PanelTitle
from panel.task import PanelTask
from panel.counter import PanelCounter

from manager.update import UpdateManager
from manager.cycle import CycleManager

from data.styles import DARK_THEME


class MainWindow(QMainWindow):
    """
    Ventana principal de DayLog.

    Se encarga de:
    - Construir la interfaz
    - Organizar los paneles
    - Conectar botones y lógica
    - Actualizar el estado visual
    """

    def __init__(self):
        super().__init__()

        # Configuración principal de la ventana
        self.setFixedSize(QSize(350, 200))
        self.setWindowTitle("DayLog v1.1")

        # Inicializa la estructura del ciclo actual
        self.cycle = CycleManager()
        self.cycle.initialize_cycle()

        # =========================
        # Widget y layout principal
        # =========================

        central_widget = QWidget()

        central_layout = QVBoxLayout()

        central_widget.setLayout(central_layout)

        # =========================
        # Paneles y lógica principal
        # =========================

        self.panel = PanelDay()
        self.title = PanelTitle()
        self.task = PanelTask()
        self.counter = PanelCounter()

        # Administrador encargado
        # del avance diario/semanal
        self.update_manager = UpdateManager()

        # =========================
        # Botón de avance
        # =========================

        self.next_button = QPushButton("Siguiente")

        layout_button = QHBoxLayout()

        layout_button.addWidget(self.next_button)

        # =========================
        # Layout izquierdo
        # =========================

        left_layout = QVBoxLayout()

        left_layout.addWidget(self.title)
        left_layout.addWidget(self.panel)
        left_layout.addLayout(layout_button)

        # =========================
        # Layout principal horizontal
        # =========================

        layout_principal = QHBoxLayout()

        layout_principal.addLayout(left_layout, 1)
        layout_principal.addWidget(self.task, 1)
        layout_principal.addWidget(self.counter, 0)

        # =========================
        # Señales
        # =========================

        self.next_button.clicked.connect(self.next_day)

        # =========================
        # Layout final
        # =========================

        central_layout.addLayout(layout_principal)

        self.setCentralWidget(central_widget)

    def next_day(self):
        """
        Guarda las tareas actuales y actualiza
        toda la interfaz al avanzar de día.
        """

        # Obtiene el estado actual de las tareas
        tasks = self.task.get_states()

        # Actualiza el estado interno
        self.update_manager.next_day(tasks)

        # Actualiza todos los paneles visuales
        self.task.clear_tasks()
        self.panel.update_panel()
        self.title.update_title()
        self.counter.update_counter()


# =========================
# Inicio de la aplicación
# =========================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Aplicar tema visual
    app.setStyleSheet(DARK_THEME)

    # Crear ventana principal
    window = MainWindow()

    window.show()

    sys.exit(app.exec())