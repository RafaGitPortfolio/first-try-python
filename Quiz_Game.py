questions = {
    "What is the capital of Germany? ": "berlin",
    "What is 10 + 5? ": "15",
    "What is the color of the sky? ": "blue"
}

def start_quiz():
    score = 0
    for question, answer in questions.items():
        user_answer = input(question).lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"\nYou got {score} out of {len(questions)} questions correct.")

while True:
    print("\n1. Start Quiz\n2. Exit")
    choice = input("Choose: ")

    if choice == "1":
        start_quiz()
    elif choice == "2":
        break
    else:
        print("Invalid choice.")