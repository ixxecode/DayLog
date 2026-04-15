# | [Dia 5]
# | ~/task_manager.py
# | Maneja la logica del dia actual y guarda las tareas

import json
import os


class TaskManager:
    def __init__(self):
        self.base_path = "weeks"
    
    def _ensure_directory(self):
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def _get_week_path(self, week):
        return os.path.join(self.base_path, f"week_{week}.json")

    def _create_empty_week(self):
        return [[], [], [], [], [], [], []]
    
    def load_week(self, week):
        self._ensure_directory()

        path = self._get_week_path(week)

        if not os.path.exists(path):
            data = self._create_empty_week()

            with open(path, "w") as file:
                json.dump(data, file)

            return data

        with open(path, "r") as file:
            return json.load(file)
    
    def save_week(self, week, data):
        path = self._get_week_path(week)

        with open(path, "w") as file:
            json.dump(data, file, indent=4)
    
    def save_day(self, week, day, tasks):
        data = self.load_week(week)

        data[day] = tasks

        self.save_week(week, data)