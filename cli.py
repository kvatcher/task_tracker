from jsonmanager import TaskManager
import cmd


class CLI(cmd.Cmd):
    prompt = "taskr > "
    def __init__(self,task_manager):
        super().__init__()
        self.task_manager = task_manager
        self.commands = {
            'mark-in-progress' : self.do_mark_in_progress,
            'mark-as-done' : self.do_mark_as_done
        }

    def do_exit(self, arg):
        """Exit the CLI: exit"""
        print("Exiting...")
        return True
    
    def do_createtask(self, arg):
        """Create a new task: createtask <description>"""
        if not arg:
            print("Usage: createtask <description>")
        else:
            task_id = self.task_manager.create_task(arg)
            print(f"Task created with ID: {task_id}")

    def do_delete(self, arg):
        """Delete a task: delete <task_id>"""
        if not arg:
            print("Usage: delete <task_id>")
        else:
            if self.task_manager.delete_task(arg):
                print(f"Task {arg} deleted.")
            else:
                print(f"Task {arg} not found.")

    def do_update(self, arg):
        """Update a task with a new description: update <task_id> <new description>"""
        args = arg.split()
        if len(args) < 2:
            print("Error: Usage: update <task_id> <new description>")
            return
        
        task_id, new_description = args[0], args[1:]
        old_description = self.task_manager.tasks[task_id]["description"]
        new_description = " ".join(new_description)
        if self.task_manager.update_task(task_id, new_description):
            print(f"Successfully updated from {old_description} to {new_description}")
        

    def do_mark_in_progress(self, arg):
        """Mark a task as 'in progress': mark-in-progress <task_id> """
        if not arg:
            print("Usage: mark-in-progress <task id>")
        else:
            if self.task_manager.mark_in_progress(arg):
                print(f"Task {arg} set as In progress.")
            else:
                print(f"Task {arg} not found.")

    def do_mark_as_done(self, arg):
        """Mark a task as 'Done!': mark-done <task_id> """
        if not arg:
            print("Usage: mark-as-done <task id>")
        else:
            if self.task_manager.mark_as_done(arg):
                print(f"Task {arg} set as Done!.")
            else:
                print(f"Task {arg} not found.")                

    def do_listtasks(self, arg):
        """List all tasks: listtasks
            List to do tasks: listtasks todo
            List in progress tasks: listtasks in-progress
            List done tasks: listtasks done"""
        if not arg:
            self.task_manager.list_tasks()
        elif arg == "todo":
            self.task_manager.list_tasks("todo")
        elif arg == "in-progress":
            self.task_manager.list_tasks("in-progress")
        elif arg == "done":
            self.task_manager.list_tasks("done")

    def default(self, line):
        command = line.split()[0]
        if command in self.commands:
            self.commands[command]
        else:   
            print("Unknown command. Type 'help' for available commands.")

