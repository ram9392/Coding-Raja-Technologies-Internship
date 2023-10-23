import json
import datetime
# Task class
class Task:
    def init(self, task_id, description, priority, due_date, completed=False):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed
# Initialize an empty list to store tasks
tasks = []
# Function to add a task
def add_task():
    description = input("Enter task description: ")
    priority = input("Enter task priority (high, medium, low): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    task_id = len(tasks) + 1
    task = Task(task_id, description, priority, due_date)
    tasks.append(task)
    print("Task added successfully!")
# Function to remove a task
def remove_task():
    task_id = int(input("Enter the ID of the task to remove: "))
    task_to_remove = None

    for task in tasks:
        if task.task_id == task_id:
            task_to_remove = task
            break

    if task_to_remove:
        tasks.remove(task_to_remove)
        print("Task removed successfully!")
    else:
        print("Task not found.")
# Function to mark a task as completed
def mark_completed():
    task_id = int(input("Enter the ID of the task to mark as completed: "))
    for task in tasks:
        if task.task_id == task_id:
            task.completed = True
            print("Task marked as completed!")
            return
    print("Task not found.")
# Function to display tasks
def view_tasks():
    for task in tasks:
        print(f"ID: {task.task_id}, Description: {task.description}, Priority: {task.priority}, Due Date: {task.due_date}, Completed: {task.completed}")
# Load tasks from a file if available
try:
    with open("tasks.json", "r") as file:
        tasks_data = json.load(file)
        tasks = [Task(**task) for task in tasks_data]
except FileNotFoundError:
    pass
# Main menu loop
while True:
    print("\nTo do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark as Completed")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        view_tasks()
    elif choice == "5":
        # Save tasks to a file before exiting
        with open("tasks.json", "w") as file:
            json.dump([task.dict for task in tasks], file)
        print("Goodbye!")
        break