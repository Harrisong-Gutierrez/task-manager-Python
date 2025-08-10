from datetime import datetime
from .task import Task, Priority

class TimedTask(Task):
    def __init__(self, description, due_date, priority=Priority.MEDIUM):
        super().__init__(description, priority)
        self.due_date = due_date
    
    def to_dict(self):
        data = super().to_dict()
        data['due_date'] = self.due_date.isoformat()
        data['type'] = 'timed'
        return data
    
    @classmethod
    def from_dict(cls, data):
        task = cls(
            data['description'],
            datetime.fromisoformat(data['due_date']),
            Priority(data['priority'])
        )
        task.id = data['id']
        task.created_at = datetime.fromisoformat(data['created_at'])
        task.completed = data['completed']
        return task

class RecurringTask(Task):
    def __init__(self, description, interval_days, priority=Priority.MEDIUM):
        super().__init__(description, priority)
        self.interval_days = interval_days
    
    def to_dict(self):
        data = super().to_dict()
        data['interval_days'] = self.interval_days
        data['type'] = 'recurring'
        return data
    
    @classmethod
    def from_dict(cls, data):
        task = cls(
            data['description'],
            data['interval_days'],
            Priority(data['priority'])
        )
        task.id = data['id']
        task.created_at = datetime.fromisoformat(data['created_at'])
        task.completed = data['completed']
        return task