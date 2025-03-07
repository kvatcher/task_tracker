import json
import os
import datetime

path = os.path.dirname(os.path.realpath(__file__))

#Verifies if file exists, in the case that it doesn't, creates one.
try:
   with open(f'{path}\\tasks.json','r') as tasks_file:
       print("File exists")

except FileNotFoundError as error:
    with open(f'{path}\\tasks.json','w') as tasks_file:
        json.dump({},tasks_file)
    print("File created")

def create_task(id, desc, status, createdAt, updatedAt):
    new_task = {id : [desc, status, createdAt, updatedAt]}
    with open(f'{path}\\tasks.json','r') as tasks_file:
            tasks_dict = json.load(tasks_file)
    tasks_dict.update(new_task)
    with open(f'{path}\\tasks.json','w') as tasks_file:
            json.dump(tasks_dict, tasks_file, indent=1)
  
def update_task (search_id, desc):
    try:
        with open(f'{path}\\tasks.json','r') as tasks_file:
            tasks_dict = json.load(tasks_file)
        update_time = datetime.datetime.now()
        olddesc = tasks_dict[search_id][0]
        tasks_dict [search_id][0] = desc
        tasks_dict [search_id][3] = update_time.strftime("%d/%m/%Y, %H:%M:%S")
        with open(f'{path}\\tasks.json','w') as tasks_file:
            json.dump(tasks_dict, tasks_file, indent=1)
        return olddesc
    except KeyError as error:
        print("Key doesn't exist! Insert a correct number")
        menu()

def delete_task (search_id):
    try:
        with open(f'{path}\\tasks.json','r') as tasks_file:
            tasks_dict = json.load(tasks_file)
        tasks_dict.pop(search_id)
        with open(f'{path}\\tasks.json','w') as tasks_file:
            json.dump(tasks_dict, tasks_file, indent=1)
    except KeyError as error:
        print("Key doesn't exist! Insert a correct number")
        menu()
def mark_in_progress(search_id):
    try:
        with open(f'{path}\\tasks.json','r') as tasks_file:
            tasks_dict = json.load(tasks_file)
        update_time = datetime.datetime.now()
        tasks_dict [search_id][3] = update_time.strftime("%d/%m/%Y, %H:%M:%S")
        tasks_dict [search_id][1] = "In progress"
        with open(f'{path}\\tasks.json','w') as tasks_file:
            json.dump(tasks_dict, tasks_file, indent=1)
        print(f"Succesfully changed task {search_id} to 'in progress'")
    except KeyError as error:
        print("Key doesn't exist! Insert a correct number")
        menu()

def mark_as_done(search_id):
    try:
        with open(f'{path}\\tasks.json','r') as tasks_file:
            tasks_dict = json.load(tasks_file)
        update_time = datetime.datetime.now()
        tasks_dict [search_id][3] = update_time.strftime("%d/%m/%Y, %H:%M:%S")
        tasks_dict [search_id][1] = "Done!"
        with open(f'{path}\\tasks.json','w') as tasks_file:
            json.dump(tasks_dict, tasks_file, indent=1)
        print(f"Task {search_id} is done!")
    except KeyError as error:
        print("Key doesn't exist! Insert a correct number")
        menu()

def list_tasks(option=1):
    with open(f'{path}\\tasks.json','r') as tasks_file:
        tasks_dict = json.load(tasks_file)
    if option == 1:
        for i in tasks_dict:
            print(f"{i} : {tasks_dict[i][0]} \n Status: {tasks_dict[i][1]} \n Created at: {tasks_dict[i][2]} \n Last update: {tasks_dict[i][3]}")
    elif option == 2 or option  == "todo":
        for i in tasks_dict:
            if tasks_dict[i][1] == "To do":
                print(f"{i} : {tasks_dict[i][0]} \n Created at: {tasks_dict[i][2]} \n Last update: {tasks_dict[i][3]}")
    elif option == 3 or option == "in-progress":
        for i in tasks_dict:
            if tasks_dict[i][1] == "In progress":
                print(f"{i} : {tasks_dict[i][0]} \n Created at: {tasks_dict[i][2]} \n Last update: {tasks_dict[i][3]}")
    elif option == 4 or option  == "done":
        for i in tasks_dict:
            if tasks_dict[i][1] == "Done!":                                
                print(f"{i} : {tasks_dict[i][0]} \n Created at: {tasks_dict[i][2]} \n Last update: {tasks_dict[i][3]}")

def menu():
    #Takes id of last inserted task
    with open(f'{path}\\tasks.json','r') as tasks_file:
        tasks_dict = json.load(tasks_file)
        last_id = len(tasks_dict)

    print("""
        1. Create task
        2. Update task
        3. Delete task
        4. List tasks
        5. Mark in progress
        6. Mark as done""")
    choice = None
    while not choice:
        try:
            choice = int(input("Choose an option: (1) (2) (3) (4) (5) (6)  "))
            if choice == 1:
                description = input("What is the task about? ")
                status = "To do"
                createdAtNow = datetime.datetime.now()
                create_task(last_id,description,status,str(createdAtNow.strftime("%d/%m/%Y, %H:%M:%S")),"None")
                print(f"New task created: {description} with the ID {last_id}.")
                menu()
            elif choice == 2:
                try:
                    with open(f'{path}\\tasks.json','r') as tasks_file:
                        tasks_dict = json.load(tasks_file)
                    if tasks_dict == {}:
                        print("The json file is empty!")
                        raise EOFError
                    for i in tasks_dict:
                        print(i, tasks_dict[i][0])
                    searchid = input("Choose a task by ID to be updated. Type anything other than a number to cancel the operation.")
                    newdesc = input("New description: ")
                    olddata = update_task(searchid,newdesc)
                    print(f"Task {searchid} updated from '{olddata}' to '{newdesc}'")
                except EOFError as error:
                    menu()
                menu()
            elif choice == 3:
                try:
                    with open(f'{path}\\tasks.json','r') as tasks_file:
                        tasks_dict = json.load(tasks_file)
                    if tasks_dict == {}:
                        print("The json file is empty!")
                        raise EOFError
                    for i in tasks_dict:
                        print(i, tasks_dict[i][0])
                    delete_id = input("Select the task to be deleted. Type anything other than a number to cancel the operation. ")
                    delete_task (delete_id)
                except EOFError as error:
                    menu()
                
                menu()
            elif choice == 4:
                print("""
                    1. Whole list of tasks
                    2. To-do
                    3. In progress
                    4. Completed tasks
                      """)
                opt = (input("Choose an option from the list. Type anything outside of the menu to cancel. "))
                if opt in ("1","2","3","4"):
                    print("Debug 1")
                    list_tasks(int(opt))
                else:
                    menu()
                menu()
            elif choice == 5:
                try:
                    with open(f'{path}\\tasks.json','r') as tasks_file:
                        tasks_dict = json.load(tasks_file)
                    if tasks_dict == {}:
                        print("The json file is empty!")
                        raise EOFError
                    for i in tasks_dict:
                        print(i, tasks_dict[i][0])
                    mark_id = input("Select the task to mark as in-progress. Type anything other than a number to cancel the operation. ")
                    mark_in_progress(mark_id)
                except EOFError as error:
                    menu()
                menu()
            elif choice == 6:
                try:
                    with open(f'{path}\\tasks.json','r') as tasks_file:
                        tasks_dict = json.load(tasks_file)
                    if tasks_dict == {}:
                        print("The json file is empty!")
                        raise EOFError
                    for i in tasks_dict:
                        print(i, tasks_dict[i][0])
                    mark_id = input("Select the task to mark as done. Type anything other than a number to cancel the operation. ")
                    mark_as_done(mark_id)
                except EOFError as error:
                    menu()
            menu()

        except ValueError:
            print("You must type a correct number.")

if __name__ == '__main__':
    menu()

