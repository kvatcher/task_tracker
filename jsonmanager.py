import os
import json
import datetime
from tasks import Task


class TaskManager ():
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self._load_tasks()
    def _load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                tasks_data = json.load(file)
                return tasks_data
        except json.JSONDecodeError:
            print("Json file could not be opened.")
            return False

    def _save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=1)

    def create_task(self, description):
        task_id = str(len(self.tasks) + 1)
        self.tasks [task_id] = {
            "description" : description,
            "status" : "To do",
            "created_at" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at" : None
        }
        self._save_tasks()
        return task_id
    
    def update_task(self, task_id, new_description):
        try:
            if task_id in self.tasks:
                self.tasks[task_id]["description"] = new_description
                self.tasks[task_id]["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._save_tasks()
                return True, new_description
        except KeyError:
            print("Task was not found.")
            return False
        
    def delete_task(self, task_id):
        try:
            if task_id in self.tasks:
                self.tasks.pop(task_id)
                return True
        except KeyError:
            print("Task was not found.")
            return False

    def mark_in_progress(self, task_id):
        try:
            if task_id in self.tasks:
                self.tasks[task_id]["status"] = "In progress"
                self.tasks[task_id]["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._save_tasks()
                return True
        except KeyError:
            print("Task was not found. ")
            return False
        
    def mark_as_done(self, task_id):
        try:
            if task_id in self.tasks:
                self.tasks[task_id]["status"] = "Done!"
                self.tasks[task_id]["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._save_tasks()
                return True
        except KeyError:
            print("Task was not found. ")
            return False

    def list_tasks(self, *args):
        if not self.tasks:
            print("There are no tasks available.")
            return
        if not args or args == '':
            for task_id, task in self.tasks.items():
                print(f"{task_id} : {task['description']}\n Status: {task['status']}\nCreated at: {task['created_at']}\nLast update: {task['updated_at']}")
        elif args[0] == "in-progress":
            for task_id, task in self.tasks.items():
                if task['status'] == "In progress":
                    print(f"{task_id} : {task['description']}\nCreated at: {task['created_at']}\nLast update: {task['updated_at']}")
        elif args[0] == "done":
            for task_id, task in self.tasks.items():
                    if task['status'] == "Done!":
                        print(f"{task_id} : {task['description']}\nCreated at: {task['created_at']}\nLast update: {task['updated_at']}")
        elif args[0] == "todo":
            for task_id, task in self.tasks.items():
                    if task['status'] == "To do":
                        print(f"{task_id} : {task['description']}\nCreated at: {task['created_at']}\nLast update: {task['updated_at']}")

            