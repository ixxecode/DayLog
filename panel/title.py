# | [ Dia 9 ]
# | ~/panel/title.py
# | Panel visual encargado del titulo principal
# |
# | Muestra el estado actual de DayLog:
# | - Día actual
# | - Semana actual
# |
# | Ejemplo:
# | Dia Martes
# | Semana 2

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

from manager.title import TitleManager


class PanelTitle(QWidget):
    """
    Panel encargado de mostrar el título principal
    de la aplicación.

    Se conecta con TitleManager para:
    - Obtener el texto actual
    - Actualizar el contenido mostrado
    """

    def __init__(self):
        super().__init__()

        # Administrador del título
        self.tm = TitleManager()

        # Label principal del título
        self.title = QLabel(self.tm.message())

        self.title.setAlignment(Qt.AlignCenter)

        # Nombres utilizados por QSS/stylesheets
        self.setObjectName("titleContainer")
        self.title.setObjectName("titleLabel")

        # Permite aplicar estilos visuales
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Layout principal vertical
        layout = QVBoxLayout()

        layout.setContentsMargins(5, 5, 5, 5)

        layout.setSpacing(4)

        layout.addWidget(self.title)

        # Guarda el layout final
        self.setLayout(layout)

    def update_title(self):
        """
        Actualiza el contenido del título principal.
        """

        self.title.setText(self.tm.message())