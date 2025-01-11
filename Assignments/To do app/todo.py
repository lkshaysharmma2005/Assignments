import os

# File to store tasks
tasks_file = "tasks.txt"

# Ensure the tasks file exists
if not os.path.exists(tasks_file):
    with open(tasks_file, "w") as f:
        pass

def load_tasks():
    """Load tasks from the file."""
    with open(tasks_file, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(tasks_file, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("\nNo tasks to display.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task."""
    task = input("Enter the task: ").strip()
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def mark_task_done():
    """Mark a task as done."""
    tasks = load_tasks()
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] += " [DONE]"
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    """Delete a task."""
    tasks = load_tasks()
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                save_tasks(tasks)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the app."""
    while True:
        print("\nTo-Do App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tasks(load_tasks())
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
