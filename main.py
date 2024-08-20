from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False
        self.tasks = []

    def add_task(self, description, due_date):
        task = {
            'description': description,
            'due_date': due_date,
            'is_completed': False
        }
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена.")

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['is_completed'] = True
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

    def get_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task['is_completed']]
        print("Список текущих (не выполненных) задач:")
        for task in pending_tasks:
            due_date = task['due_date']
            print(f"Задача: {task['description']}. Срок: {due_date}")