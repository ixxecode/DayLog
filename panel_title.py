# | [Dia 4]
# | ~/panel_title.py
# | Archivo que crea la intefaz del titulo principal

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from title_manager import TitleManager

class PanelTitle(QWidget):
    def __init__(self):
        super().__init__()

        # Guardamos TitleManager abreciado como "tm"
        self.tm = TitleManager()

        # Creamos el titulo
        self.title = QLabel(self.tm.message())

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.title)

        # Guardamos el layout
        self.setLayout(layout)
    
    # Actualiza el titulo
    def update_title(self):
        self.title.setText(self.tm.message())