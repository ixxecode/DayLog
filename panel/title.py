# | [ Dia 6 ]
# | ~/panel/title.py
# | Archivo que crea la intefaz del titulo principal

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

from manager.title import TitleManager

class PanelTitle(QWidget):
    def __init__(self):
        super().__init__()

        # Guardamos TitleManager abreciado como "tm"
        self.tm = TitleManager()

        # Creamos el titulo
        self.title = QLabel(self.tm.message())

        self.title.setAlignment(Qt.AlignCenter)

        # Nombres para los estilos
        self.setObjectName("titleContainer")
        self.title.setObjectName("titleLabel")

        # Permite usar los estilos
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(4)  
        layout.addWidget(self.title)

        # Guardamos el layout
        self.setLayout(layout)
    
    # Actualiza el titulo
    def update_title(self):
        self.title.setText(self.tm.message())