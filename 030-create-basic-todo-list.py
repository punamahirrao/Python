def display_todo_list(todo_list):
    print("To-Do List:")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)

todo_list = []
while True:
    print("\n1. Add Task\n2. View To-Do List\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        task = input("Enter a task: ")
        add_task(todo_list, task)
    elif choice == '2':
        display_todo_list(todo_list)
    elif choice == '3':
        break
    else:
        print("Invalid choice!")
