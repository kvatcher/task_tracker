from jsonmanager import TaskManager
from cli import CLI
import os
import json

path = os.path.dirname(os.path.abspath(__file__))

print(path)
#Verifies if file exists, in the case that it doesn't, creates one.
try:
   with open(f'{path}\\tasks.json','r') as tasks_file:
    pass
except FileNotFoundError as error:
    with open(f'{path}\\tasks.json','w') as tasks_file:
        json.dump({},tasks_file)
    print("File created")


def main():
    task_manager = TaskManager(f'{path}\\tasks.json')
    cli = CLI(task_manager)
    cli.cmdloop("Task Manager CLI. Type 'help' for commands.")

if __name__ == "__main__":
    main()