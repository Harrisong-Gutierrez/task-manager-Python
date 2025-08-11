from flask import Flask
import os
from pathlib import Path
from .persistence.task_manager import TaskManager


base_dir = Path(__file__).parent  
template_dir = base_dir / 'templates' 

app = Flask(__name__, 
           template_folder=str(template_dir),
           static_folder=str(base_dir / 'templates' / 'static'))  

app.config['SECRET_KEY'] = os.urandom(24)  

current_dir = Path(__file__).parent
task_manager = TaskManager(file_path=str(current_dir.parent / 'data' / 'tasks.json'))


from . import routes