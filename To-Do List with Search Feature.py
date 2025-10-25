tasks = []

def add_task():
    task = input("New task: ")
    tasks.append(task)
    print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def search_tasks():
    word = input("Search for: ").lower()
    print("\nMatching tasks:")
    for i, task in enumerate(tasks, start=1):
        if word in task.lower():
            print(f"{i}. {task}")

while True:
    print("\n1. Add task\n2. View tasks\n3. Search task\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        search_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
