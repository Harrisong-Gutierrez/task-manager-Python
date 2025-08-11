from datetime import datetime
from ..persistence.task_manager import TaskManager
from ..models.task import Task, Priority
from ..models.task_types import TimedTask, RecurringTask
from src.utils.validators import validate_date, validate_positive_int

class CLI:
    def __init__(self):
        self.task_manager = TaskManager()
    
    def run(self):
        while True:
            print("\nGestor de Tareas")
            print("1. Agregar tarea")
            print("2. Marcar tarea como completada")
            print("3. Listar tareas")
            print("4. Salir")
            
            choice = input("Seleccione una opción: ")
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.mark_completed()
            elif choice == '3':
                self.list_tasks()
            elif choice == '4':
                break
            else:
                print("Opción no válida. Intente nuevamente.")
    
    def add_task(self):
        print("\nTipos de tarea:")
        print("1. Tarea normal")
        print("2. Tarea con fecha límite")
        print("3. Tarea recurrente")
        
        task_type = input("Seleccione el tipo de tarea: ")
        
        description = input("Descripción de la tarea: ")
        if not description:
            print("La descripción no puede estar vacía.")
            return
        
        print("Prioridades:")
        print("1. Baja")
        print("2. Media")
        print("3. Alta")
        priority_choice = input("Seleccione la prioridad (1-3): ")
        
        try:
            priority = Priority(int(priority_choice))
        except (ValueError, KeyError):
            print("Prioridad no válida. Se usará prioridad Media.")
            priority = Priority.MEDIUM
        
        if task_type == '1':
            task = Task(description, priority)
        elif task_type == '2':
            due_date_str = input("Fecha límite (YYYY-MM-DD): ")
            try:
                due_date = validate_date(due_date_str)
                task = TimedTask(description, due_date, priority)
            except ValueError as e:
                print(f"Error: {e}")
            return   
        
        elif task_type == '3':
            interval_str = input("Intervalo en días: ")
            try:
                interval = validate_positive_int(interval_str)
                task = RecurringTask(description, interval, priority)
            except ValueError as e:
                print(f"Error: {e}")
                return
        else:
            print("Tipo de tarea no válido.")
            return
        
        self.task_manager.add_task(task)
        print("Tarea agregada exitosamente.")
    
    def mark_completed(self):
        tasks = self.task_manager.get_tasks()
        if not tasks:
            print("No hay tareas para mostrar.")
            return
        
        self._print_tasks(tasks)
        task_id = input("Ingrese el ID de la tarea a marcar como completada: ")
        
        if self.task_manager.mark_as_completed(task_id):
            print("Tarea marcada como completada.")
        else:
            print("ID de tarea no válido.")
    
    def list_tasks(self):
        print("\nOpciones de ordenamiento:")
        print("1. Por prioridad")
        print("2. Por fecha de creación")
        print("3. Por estado")
        
        sort_choice = input("Seleccione el criterio de ordenamiento: ")
        
        if sort_choice == '1':
            tasks = self.task_manager.get_tasks(sort_by='priority')
        elif sort_choice == '2':
            tasks = self.task_manager.get_tasks(sort_by='date')
        elif sort_choice == '3':
            tasks = self.task_manager.get_tasks(sort_by='status')
        else:
            print("Opción no válida. Se usará orden por prioridad.")
            tasks = self.task_manager.get_tasks(sort_by='priority')
        
        if not tasks:
            print("No hay tareas para mostrar.")
            return
        
        self._print_tasks(tasks)
    
    def _print_tasks(self, tasks):
        for task in tasks:
            status = "✓" if task.completed else "✗"
            priority = {1: "Baja", 2: "Media", 3: "Alta"}[task.priority.value]
            
            print(f"\nID: {task.id}")
            print(f"Descripción: {task.description}")
            print(f"Prioridad: {priority}")
            print(f"Estado: {status}")
            print(f"Creada: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
            
            if isinstance(task, TimedTask):
                print(f"Fecha límite: {task.due_date.strftime('%Y-%m-%d')}")
            elif isinstance(task, RecurringTask):
                print(f"Intervalo: cada {task.interval_days} días")