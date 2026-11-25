import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
        return

    name_of_operation = sys.argv[1]

    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Please provide valid numbers for the operation.")
        return

    if name_of_operation == "add":
        print(add(num1, num2))
    elif name_of_operation == "multiply":
        print(multiply(num1, num2))
    elif name_of_operation == "subtract":
        print(subtract(num1, num2))
    elif name_of_operation == "divide":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(divide(num1, num2))
    else:
        print("Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'.")

if __name__ == "__main__":
    main()