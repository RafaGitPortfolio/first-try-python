# Simple Expense Tracker

expenses = []

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    expenses.append({"name": name, "amount": amount})
    print("Expense added")

def show_expenses():
    total = 0
    print("\n--- Expenses ---")
    for expense in expenses:
        print(f"{expense['name']}: ${expense['amount']}")
        total += expense['amount']
    print(f"Total: ${total}")

while True:
    print("\n1. Add Expense\n2. Show Expenses\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice")