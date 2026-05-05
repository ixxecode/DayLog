# | [ Dia 9 ]
# | ~/panel/task.py
# | Panel visual encargado de manejar las tareas diarias
# |
# | Cada tarea se representa mediante un QCheckBox.
# |
# | Ejemplo:
# | [ ] Programar
# | [x] Leer
# | [ ] Estudiar

from PySide6.QtWidgets import QWidget, QCheckBox, QVBoxLayout

from manager.task import TaskManager


class PanelTask(QWidget):
    """
    Panel encargado de mostrar y controlar
    las tareas diarias.

    Se conecta con TaskManager para:
    - Guardar tareas
    - Obtener estados actuales
    - Limpiar tareas visualmente
    """

    def __init__(self):
        super().__init__()

        # Administrador de tareas
        self.task_manager = TaskManager()

        # Lista principal de tareas
        tasks = [
            "Programar",
            "Leer",
            "Estudiar",
            "Dibujar",
            "Ejercicio",
            "Linux"
        ]

        # Lista donde se guardan
        # todos los checkboxes
        self.checkboxes = []

        # Layout principal vertical
        layout = QVBoxLayout()

        # Crea un checkbox por cada tarea
        for task in tasks:
            checkbox = QCheckBox(task)

            # Guarda referencia del checkbox
            self.checkboxes.append(checkbox)

            # Agrega el checkbox al layout
            layout.addWidget(checkbox)

        self.setLayout(layout)

    def get_states(self):
        """
        Obtiene el estado actual de todas las tareas.

        Returns
        -------
        list
            Lista de booleanos:
            True  -> completada
            False -> pendiente
        """

        states = []

        # Recorre todos los checkboxes
        for checkbox in self.checkboxes:
            states.append(checkbox.isChecked())

        return states

    def save_tasks(self, week, day):
        """
        Guarda las tareas del día indicado.

        Parameters
        ----------
        week : int
            Semana actual.

        day : int
            Índice del día actual.
        """

        states = self.get_states()

        self.task_manager.save_day(week, day, states)

    def clear_tasks(self):
        """
        Reinicia visualmente todas las tareas.

        Desmarca todos los checkboxes.
        """

        for checkbox in self.checkboxes:
            checkbox.setChecked(False)