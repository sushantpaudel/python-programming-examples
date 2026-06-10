"""Lab 1 - Question 3: Largest of three numbers using if-elif-else."""

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print(f"The largest number is: {largest}")


if __name__ == "__main__":
    main()
