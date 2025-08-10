import json
from pathlib import Path
from datetime import datetime
from ..models.task import Task
from ..models.task_types import TimedTask, RecurringTask

class TaskManager:
    def __init__(self, file_path='data/tasks.json'):
        self.file_path = Path(file_path)
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
    
    def mark_as_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_completed()
                self.save_tasks()
                return True
        return False
    
    def get_tasks(self, sort_by='priority'):
        tasks = self.tasks.copy()
        
        if sort_by == 'priority':
            tasks.sort(key=lambda x: (-x.priority.value, x.created_at))
        elif sort_by == 'date':
            tasks.sort(key=lambda x: x.created_at)
        elif sort_by == 'status':
            tasks.sort(key=lambda x: (x.completed, x.created_at))
        
        return tasks
    
    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        self.file_path.parent.mkdir(exist_ok=True)
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_tasks(self):
        if not self.file_path.exists():
            self.tasks = []
            return
        
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        
        self.tasks = []
        for item in data:
            if item.get('type') == 'timed':
                self.tasks.append(TimedTask.from_dict(item))
            elif item.get('type') == 'recurring':
                self.tasks.append(RecurringTask.from_dict(item))
            else:
                self.tasks.append(Task.from_dict(item))