# | [Dia 5]
# | ~/panel_task.py
# | Archivo que maneja la interfaz del panel de tareas

from PySide6.QtWidgets import QWidget, QCheckBox, QVBoxLayout

from task_manager import TaskManager

class PanelTask(QWidget):
    def __init__(self):
        super().__init__()

        # logica de las tareas
        self.task_manager = TaskManager()

        # Lista de tareas + Lista de checkboxes
        tasks = ["Programar", "Leer", "Estudiar", "Dibujar", "Ejercicio", "Linux"]
        self.checkboxes = []

        # Layout principal
        layout = QVBoxLayout()

        for task in tasks:
            checkbox = QCheckBox(task)
            self.checkboxes.append(checkbox)
            layout.addWidget(checkbox)

        self.setLayout(layout)

    def get_states(self):
        states = []

        for checkbox in self.checkboxes:
            states.append(checkbox.isChecked())

        return states

    def save_tasks(self, week, day):
        states = self.get_states()
        self.task_manager.save_day(week, day, states)

    def clear_tasks(self):
        for checkbox in self.checkboxes:
            checkbox.setChecked(False)