students = []

def add_student():
    name = input("Student name: ")
    try:
        grade = float(input("Student grade (0-100: "))
        students.append({"name": name, "grade": grade})
        print(f"Added {name} with grade {grade}")
    except ValueError:
        print("Invalid grade! Must be a number.")

def show_students():
    if not students:
        print("No students added yet.")
    else:
        print("\n--- Student List ---")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student['name']} - {student['grade']}")

while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")