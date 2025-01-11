import os

tasks = []

def display_menu():
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Mark Task as Complete")
    print("4. Delete a Task")
    print("5. Save Tasks to File")
    print("6. Load Tasks from File")
    print("7. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['completed'] else "✗"
        print(f"{i}. {task['name']} [{status}]")

def add_task():
    task_name = input("\nEnter the task name: ")
    tasks.append({'name': task_name, 'completed': False})
    print("Task added successfully!")

def mark_task_complete():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("\nEnter the task number to mark as complete: "))
        tasks[task_number - 1]['completed'] = True
        print("Task marked as complete!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        tasks.pop(task_number - 1)
        print("Task deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            status = "1" if task['completed'] else "0"
            file.write(f"{task['name']}|{status}\n")
    print("Tasks saved to file!")

def load_tasks_from_file():
    global tasks
    if not os.path.exists("tasks.txt"):
        print("No saved tasks found!")
        return
    with open("tasks.txt", "r") as file:
        tasks = []
        for line in file:
            name, status = line.strip().split("|")
            tasks.append({'name': name, 'completed': status == "1"})
    print("Tasks loaded from file!")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                save_tasks_to_file()
            elif choice == 6:
                load_tasks_from_file()
            elif choice == 7:
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
