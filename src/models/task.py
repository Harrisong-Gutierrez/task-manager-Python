import uuid
from datetime import datetime
from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    def __init__(self, description, priority=Priority.MEDIUM):
        self.id = str(uuid.uuid4())
        self.description = description
        self.priority = priority
        self.created_at = datetime.now()
        self.completed = False
    
    def mark_as_completed(self):
        self.completed = True
    
    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'priority': self.priority.value,
            'created_at': self.created_at.isoformat(),
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data['description'], Priority(data['priority']))
        task.id = data['id']
        task.created_at = datetime.fromisoformat(data['created_at'])
        task.completed = data['completed']
        return task