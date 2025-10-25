# A shopping list with remove option

shopping_list = []

def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list.")

def show_items():
    if not shopping_list:
        print("No items in the list.")
    else:
        print("\n--- Shopping List ---")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"\n{item} removed from the list.")
    else:
        print("Item not found.")

while True:
    print("\n1. Add item\n2. View items\n3. Remove item\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        show_items()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        break
    else:
        print("Invalid option.")