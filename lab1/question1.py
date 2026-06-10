"""Lab 1 - Question 1: Arithmetic on two numbers."""

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition:       {a + b}")
    print(f"Subtraction:    {a - b}")
    print(f"Multiplication: {a * b}")

    if b == 0:
        print("Division:       Cannot divide by zero")
    else:
        print(f"Division:       {a / b}")


if __name__ == "__main__":
    main()
