# | [ Dia 6 ]
# | ~/manager/task.py
# | Maneja la logica del dia actual y guarda las tareas

import json
from pathlib import Path


class TaskManager:
    def __init__(self):
        # Carpeta persistente del usuario
        base_dir = Path.home() / ".daylog"

        # Carpeta weeks dentro de .daylog
        self.base_path = base_dir / "weeks"
    
    # [Interna] Asegura que exista la carpeta de weeks
    def _ensure_directory(self):
        self.base_path.mkdir(parents=True, exist_ok=True)

    # [Interna] Devuelve el path del archivo de una semana
    def _get_week_path(self, week):
        return self.base_path / f"week_{week}.json"

    # [Interna] Crea la estructura vacia de una semana (7 dias)
    def _create_empty_week(self):
        return [[], [], [], [], [], [], []]
    
    # Carga una semana desde el archivo o la crea si no existe
    def load_week(self, week):
        self._ensure_directory()

        path = self._get_week_path(week)

        if not path.exists():
            data = self._create_empty_week()
            path.write_text(json.dumps(data))
            return data

        return json.loads(path.read_text())
    
    # Guarda una semana completa en su archivo correspondiente
    def save_week(self, week, data):
        path = self._get_week_path(week)
        path.write_text(json.dumps(data, indent=4))
    
    # Guarda las tareas de un dia especifico dentro de una semana
    def save_day(self, week, day, tasks):
        data = self.load_week(week)
        data[day] = tasks
        self.save_week(week, data)