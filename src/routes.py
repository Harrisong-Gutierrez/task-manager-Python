from flask import Flask, render_template, request, redirect, url_for

from datetime import datetime
from models.task import Task
from models.task_types import TimedTask, RecurringTask
from persistence import task_manager  

app = Flask(__name__)

@app.route('/')
def index():
    # tasks = task_manager.get_tasks(sort_by='priority')
    return render_template('index.html', tasks=[])

# @app.route('/add', methods=['GET', 'POST'])
# def add_task():
#     if request.method == 'POST':
#         description = request.form['description']
#         priority = int(request.form['priority'])
        
#         if 'due_date' in request.form:  
#             due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d').date()
#             task = TimedTask(description, due_date, priority)
#         else:
#             task = Task(description, priority)
        
#         task_manager.add_task(task)
#         return redirect(url_for('index'))
    
#     return render_template('add_task.html')

if __name__ == "__main__":
    app.run(debug=True)