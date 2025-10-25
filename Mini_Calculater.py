#Simple calculater

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator"

print("--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

result = calculate(num1, num2, op)
print("Result:", result)