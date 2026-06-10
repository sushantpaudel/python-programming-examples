"""Lab 1 - Question 6: Simple calculator using functions."""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition:       {add(a, b)}")
    print(f"Subtraction:    {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")

    try:
        print(f"Division:       {divide(a, b)}")
    except ValueError as e:
        print(f"Division:       {e}")


if __name__ == "__main__":
    main()
