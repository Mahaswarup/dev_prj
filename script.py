# script.py
def add_task():
    print("Task added!")

def view_tasks():
    print("Viewing tasks!")

def remove_task():
    print("Task removed!")

def main():
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    # Instead of asking for user input, use a predefined choice
    choice = 1  # Predefined value (e.g., Add Task)

    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        print("Exiting...")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
