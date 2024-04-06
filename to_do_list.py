class Task:
    def __init__(self, description):
        self.description = description

class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("To-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.description}")

    def add_task(self):
        task_description = input("Enter the task: ")
        task = Task(task_description)
        self.tasks.append(task)
        print("Task added successfully.")

    def update_task(self):
        self.view_tasks()
        task_index = int(input("Enter the task number to update: ")) - 1
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task number.")
        else:
            new_task_description = input("Enter the new task: ")
            self.tasks[task_index].description = new_task_description
            print("Task updated successfully.")

    def delete_task(self):
        self.view_tasks()
        task_index = int(input("Enter the task number to delete: ")) - 1
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task number.")
        else:
            deleted_task = self.tasks.pop(task_index)
            print(f"Task '{deleted_task.description}' deleted successfully.")

todo_list = ToDoList()

while True:
    todo_list.display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        todo_list.view_tasks()
    elif choice == "2":
        todo_list.add_task()
    elif choice == "3":
        todo_list.update_task()
    elif choice == "4":
        todo_list.delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


