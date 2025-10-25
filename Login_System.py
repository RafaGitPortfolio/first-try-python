users = {
    "alice": "1234",
    "bob": "abcd",
}

def login():
    for attempt in range(3):
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
    print("Too many attempts. Acess denied.")
    return False

while True:
    print("\n1. Login\n2. Exit")
    choice = input("Choose: ")

    if choice == "1":
        login()
    elif choice == "2":
        break
    else:
        print("Invalid choice.")