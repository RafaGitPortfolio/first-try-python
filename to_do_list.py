#simple to-do list

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Exit")

tasks = []

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task {task} added!")
    elif choice == "2":
        print("\nYour tasks")
        for i, task in enumerate(tasks, start=1):
            print(f"Task {i}. {task}")
    elif choice == "3":
        print("\nExiting...")
        break
    else:
        print("\nInvalid choice!")