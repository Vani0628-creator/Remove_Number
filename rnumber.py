
todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        removed = todo_list.pop(task_num - 1)
        print(f"Task '{removed}' removed.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
