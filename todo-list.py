#to-do list app with save feature

FILENAME = "tasks.txt"

try:
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet! ")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    save_tasks()
    print(f"Added: {new_task}")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks()
        print(f"Deleted: {removed}.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def save_tasks():
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

while True:
    print("\n=== To-Do List Menu ===")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Bye! Your tasks are saved.")
        break
    else:
        print("Invalid choice. Try again.")
