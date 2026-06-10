"""Lab 1 - Question 2: Check if a number is even or odd."""

def main():
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")


if __name__ == "__main__":
    main()
