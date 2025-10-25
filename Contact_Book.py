# Simple Contact Book

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")

def show_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

while True:
    print("\n1. Add Contact\n2. Show Contacts\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")