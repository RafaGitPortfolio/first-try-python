def add_note():
    note = input("Enter note: ")
    with open("../../../AppData/Roaming/JetBrains/PyCharm2025.2/scratches/notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def show_notes():
    try:
        with open("../../../AppData/Roaming/JetBrains/PyCharm2025.2/scratches/notes.txt", "r") as file:
            content = file.read()
            if content:
                print("\n--- Your notes ---")
                print(content)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes file exists yet!")

while True:
    print("\n1. Add Note\n2. View Notes\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")