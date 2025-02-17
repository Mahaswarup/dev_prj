todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please select a valid option.")
