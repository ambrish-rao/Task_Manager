import datetime as dt
import json

# List to store tasks
tasks = []

# Add a task
def add_task(title, description, priority='low', deadline=None):
    task = {
        'title': title,
        'description': description,
        'priority': priority.lower(),
        'deadline': deadline,
        'status': 'pending'
    }
    tasks.append(task)
    print(f"Task '{title}' added successfully.")

# List all tasks
def list_tasks():
    if not tasks:  # Check if the list is empty
        print("No tasks available.")
    else:
        print("\n--- Task List ---")
        for i, task in enumerate(tasks, start=1):
            deadline = task['deadline'] if task['deadline'] else "No deadline"
            print(f"{i}. {task['title']} - {task['priority']} priority - {deadline} - {task['status']}")

# Delete a task
def delete_task(task_index):
    try:
        removed = tasks.pop(task_index)
        print(f"Task '{removed['title']}' deleted successfully.")
    except IndexError:
        print("Invalid task number. Please try again.")

# Toggle the status of a task
def toggle_status(task_index):
    try:
        task = tasks[task_index]
        if task['status'] == 'completed':
            task['status'] = 'pending'
        else:
            task['status'] = 'completed'
        print(f"Task '{task['title']}' status updated to {task['status']}.")
    except IndexError:
        print("Invalid task number. Please try again.")

# Filter tasks by priority
def filter_priority(priority_level):
    priority_level = priority_level.lower()
    filtered_tasks = [task for task in tasks if task['priority'] == priority_level]
    if filtered_tasks:
        print("\n--- Filtered Tasks by Priority ---")
        for i, task in enumerate(filtered_tasks, start=1):
            print(f"{i}. {task['title']} - {task['priority']} priority - {task['status']}")
    else:
        print(f"No tasks found with priority '{priority_level}'.")

# Filter tasks by deadline
def filter_deadline(due_date):
    try:
        due_date = dt.datetime.strptime(due_date, '%Y-%m-%d')
        filtered_tasks = [
            task for task in tasks
            if task['deadline'] and dt.datetime.strptime(task['deadline'], '%Y-%m-%d') <= due_date
        ]
        if filtered_tasks:
            print("\n--- Filtered Tasks by Deadline ---")
            for i, task in enumerate(filtered_tasks, start=1):
                print(f"{i}. {task['title']} - {task['deadline']} - {task['status']}")
        else:
            print("No tasks found before the specified deadline.")
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")

# Save tasks to a file
def save_data(filename):
    try:
        with open(filename, 'w') as file:
            json.dump(tasks, file)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Load tasks from a file
def load_data(filename):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("File not found. Starting with an empty task list.")
    except json.JSONDecodeError:
        print("Error reading the file. Starting with an empty task list.")

# Main program loop
def main():
    load_data('tasks.json')  # Load tasks at the start
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Toggle Task Status")
        print("5. Filter Tasks by Priority")
        print("6. Filter Tasks by Deadline")
        print("7. Save Tasks")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (low/medium/high): ")
            deadline = input("Enter task deadline (YYYY-MM-DD) or leave blank: ")
            deadline = deadline if deadline else None
            add_task(title, description, priority, deadline)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                task_index = int(input("Enter task number to delete: ")) - 1
                delete_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            try:
                task_index = int(input("Enter task number to toggle status: ")) - 1
                toggle_status(task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            priority_level = input("Enter priority level (low/medium/high): ")
            filter_priority(priority_level)
        elif choice == '6':
            due_date = input("Enter deadline (YYYY-MM-DD): ")
            filter_deadline(due_date)
        elif choice == '7':
            save_data('tasks.json')
        elif choice == '8':
            save_data('tasks.json')  # Save tasks before exiting
            print("Goodbye!, See u next Time.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
