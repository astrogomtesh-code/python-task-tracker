import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r") as f:
                return json.load(f)
        except:
            print("Corrupted file. Starting fresh.")
            return []
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i+1}. {task['title']} [{status}]")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

tasks = load_tasks()

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark as done")
    print("5. Quit")

    try:
        choice = int(input("Choose: "))
    except:
        print("Enter a number.")
        continue

    match choice:
        case 1:
            add_task(tasks)
        case 2:
            show_tasks(tasks)
        case 3:
            delete_task(tasks)
        case 4:
            mark_done(tasks)
        case 5:
            break
        case _:
            print("Invalid choice.")


print("press enter to exit....")
        
         

