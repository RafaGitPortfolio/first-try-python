import json

contacts = []

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})
    save_contacts()
    print("Contact saved!")

def show_contacts():
    if not contacts:
        print("No contacts yet!")
    else:
        for i, c in enumerate(contacts, start=1):
            print({i}, {c["name"]} - {c["phone"]})

contacts = load_contacts()

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")