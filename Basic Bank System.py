accounts = {"Alice": 100.0, "Bob": 50.0}

def deposit(name, amount):
    accounts[name] += amount
    return accounts[name]  # returning new balance

def withdraw(name, amount):
    if accounts[name] >= amount:
        accounts[name] -= amount
        return accounts[name]
    else:
        return "Not enough money"

def show_accounts():
    print("\n--- Accounts ---")
    for name, balance in accounts.items():
        print(f"{name}: ${balance}")

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Show Accounts\n4. Exit")
    choice = input("Choose: ")

    if choice in ["1", "2"]:
        name = input("Name: ")
        if name not in accounts:
            print("Account not found.")
            continue
        amount = float(input("Amount: "))

        if choice == "1":
            new_balance = deposit(name, amount)
            print("New balance:", new_balance)
        else:
            result = withdraw(name, amount)
            print("Result:", result)

    elif choice == "3":
        show_accounts()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
