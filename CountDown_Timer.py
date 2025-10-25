import time

def countdown():
    seconds = int(input("Enter seconds to count down: "))
    for i in range(seconds, 0, -1):
        print(f"Time left: {i} seconds")
        time.sleep(0.5)
    print("Time's up!")

while True:
    print("\n1. Start Timer\n2. Exit")
    choice = input("Choose: ")

    if choice == "1":
        countdown()
    elif choice == "2":
        break
    else:
        print("Invalid choice.")